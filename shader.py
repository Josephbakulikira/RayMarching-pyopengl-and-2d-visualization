VERTEX_SHADER = """
#version 330 core
layout(location = 0) in vec3 vPos;
void main()
{
    gl_Position = vec4(vPos, 1.0);
}
"""

FRAGMENT_SHADER = """
#version 330 core
#define fragCoord gl_FragCoord.xy
uniform vec2  u_mouse;
uniform float u_time;
uniform vec2  u_resolution;
out vec4 fragColor;

float SDFsphere(vec3 pos, float radius)
{
    return length(pos) - radius;
}

float WorldSDF(in vec3 pos)
{
    float sphere_0 = SDFsphere(pos, 2.5);
    return sphere_0;
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

vec3 ray_march(in vec3 ray_origin, in vec3 ray_direction)
{
    float total_distance_traveled = 0.0;
    const int n_steps = 32;
    const float min_hit = 0.001;
    const float max_distance = 1000.0;

    for (int i = 0; i < n_steps; ++i)
    {
        vec3 current_position = ray_origin + total_distance_traveled * ray_direction;
        float distance_to_closest = WorldSDF(current_position);

        if (distance_to_closest < min_hit) // hit
        {
            // in case we hit something
            vec3 normal = surface_normal(current_position);

            vec3 light_position = vec3(-u_mouse.x, u_mouse.y, 3.0);

            vec3 direction_to_light = normalize(current_position - light_position);

            float diffuse_intensity = max(0.0, pow(dot(normal, direction_to_light), 14.0));

            return normal * 0.5 + 0.5 * diffuse_intensity;
        }

        if (total_distance_traveled > max_distance) // miss
        {
            break;
        }
        total_distance_traveled += distance_to_closest;
    }

    //didn't hit anything return background
    return vec3(0.0);
}
void main()
{
    vec2 uv = fragCoord / u_resolution.xy * 2.0 - 1.0;
    uv.x *= u_resolution.x / u_resolution.y;

    vec3 camera_position = vec3(0.0, 0.0, -5.0);
    vec3 ray_origin = camera_position;
    vec3 ray_direction = vec3(uv, 1.0);

    vec3 color = ray_march(ray_origin, ray_direction);
    fragColor = vec4(color, 1.0);
}
"""
