#version 330 core
layout(location = 0) in vec3 vPos;
//uniform mat4 u_view;
uniform mat4 u_projection;
uniform mat4 u_model;
void main()
{

    gl_Position = vec4(vPos, 1.0);
}