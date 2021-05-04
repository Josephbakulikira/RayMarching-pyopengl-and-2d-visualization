VERTEX_SHADER = """
#version 330 core
layout(location = 0) in vec3 vPos;
//uniform mat4 u_view;
uniform mat4 u_projection;
uniform mat4 u_model;
void main()
{

    gl_Position =  vec4(vPos, 1.0);
}
"""

FRAGMENT_SHADER = """
#version 330 core
#define fragCoord gl_FragCoord.xy

uniform vec2  u_mouse;
uniform float u_time;
uniform vec2  u_resolution;

uniform mat4 u_view;
uniform mat4 u_projection;

out vec4 fragColor;

float intersectSDF(float distA, float distB) {
    return max(distA, distB);
}

float unionSDF(float distA, float distB) {
    return min(distA, distB);
}

float differenceSDF(float distA, float distB) {
    return max(distA, -distB);
}

float SDFsphere(vec3 pos, float radius)
{
    return length(pos) - radius;
}


float SDFcube( vec3 p, vec3 b )
{
  vec3 q = abs(p) - b;
  return length(max(q,0.0)) + min(max(q.x,max(q.y,q.z)),0.0);
}

float SDFroundedCube( vec3 p, vec3 b, float r )
{
  vec3 q = abs(p) - b;
  return length(max(q,0.0)) + min(max(q.x,max(q.y,q.z)),0.0) - r;
}

float SDFtorus( vec3 p, vec2 t )
{
  vec2 q = vec2(length(p.xz)-t.x,p.y);
  return length(q)-t.y;
}

float SDFsphereMod (vec3 p, float s) {
    float l = length(p);
    vec3 sphere = vec3(1.0, 1.0,1.0);
    return length(mod(sphere.xyz - p, s) - vec3(s/2.0)) - .5 ;
}



float WeirdDisplacement(vec3 pos, float val){
    float displ = sin(4.0 * pos.x) * cos(4.0 * pos.y) * sin(4.0 * pos.z) * 0.25 * val;
    return displ;
}



//scene informations
float WorldSDF(in vec3 p)
{
    float torus = SDFtorus(p, vec2(1.0, 0.5));
    float sphere = SDFsphere(p, 1.0);
    //float modSphere = SDFsphereMod(p, 5.0);
    //float plane = dot(p + vec3(0, 1, 0), normalize(vec3(0, 1, 0)));
    //float displacements = WeirdDisplacement(p, u_time);
    float sphereTorus = differenceSDF(sphere, torus);
    float c = 5.0;
    vec3 q = mod(p+0.5*c,c)-0.5*c;
    return sphereTorus;
}



mat4 viewMatrix(vec3 eye, vec3 center, vec3 up) {
	vec3 f = normalize(center - eye);
	vec3 s = normalize(cross(f, up));
	vec3 u = cross(s, f);
	return mat4(
		vec4(s, 0.0),
		vec4(u, 0.0),
		vec4(-f, 0.0),
		vec4(0.0, 0.0, 0.0, 1)
	);
}

vec3 surface_normal(in vec3 pos)
{
    const vec3 EPSILON = vec3(0.001, 0.0, 0.0);
    float gradient_x = WorldSDF(pos + EPSILON.xyy) - WorldSDF(pos - EPSILON.xyy);
    float gradient_y = WorldSDF(pos + EPSILON.yxy) - WorldSDF(pos - EPSILON.yxy);
    float gradient_z = WorldSDF(pos + EPSILON.yyx) - WorldSDF(pos - EPSILON.yyx);
    vec3 normal = vec3(gradient_x, gradient_y, gradient_z);
    return normalize(normal);
}



vec3 ray_march(in vec3 ray_origin, in vec3 ray_direction, vec3 gradColor)
{
    float total_distance_traveled = 0.0;
    const int n_steps = 32;
    const float min_hit = 0.0001;
    const float max_distance = 1000.0;

    for (int i = 0; i < n_steps; ++i)
    {
        vec3 current_position = ray_origin + total_distance_traveled * ray_direction;
        float distance_to_closest = WorldSDF(current_position);

        if (distance_to_closest < min_hit) // hit
        {
            // in case we hit something
            vec3 normal = surface_normal(current_position);

            vec3 light_position = vec3(-u_mouse.x, u_mouse.y, 4.0);

            vec3 direction_to_light = normalize(current_position - light_position);

            float diffuse_intensity = max(0.0, pow(dot(normal, direction_to_light), 2.0));

            return normal * 0.5 + 0.5 * diffuse_intensity;
            //return gradColor * diffuse_intensity;

            return vec3(1.0) * diffuse_intensity ;
        }

        if (total_distance_traveled > max_distance) // miss
        {
            break;
        }
        total_distance_traveled += distance_to_closest;
    }

    //didn't hit anything return background
    return vec3(0.0);
    //return gradColor.xyz
}



void main()
{
    vec2 uv = fragCoord / u_resolution.xy * 2.0 - 1.0;
    uv.x *= u_resolution.x / u_resolution.y;

    //vec3 ray_origin = vec3(0.2, 0.1, -5.0 + sin(cos(u_time)));
    vec3 ray_origin = vec3(0.0, 0.0, -3.0 );
    vec3 ray_direction = vec3(uv, 1.0);

    vec3 gradColor = 0.5 + 0.5 * cos(u_time + uv.xyx + vec3(0.0, 2.0, 4.0));

    vec3 color = ray_march(ray_origin , ray_direction, gradColor);
    fragColor = vec4(color, 1.0);
}
"""
