vertex_shader = """
    #version 450 core
    layout (location = 0) in vec3 position;
    layout (location = 1) in vec3 inColor;
    layout (location = 1) in vec2 texCoords;
    layout (location = 2) in vec3 normals;
    
    uniform mat4 modelMatrix;
    uniform mat4 viewMatrix;
    uniform mat4 projectionMatrix;
    
    out vec4 outColor;
    out vec2 UVs;
    out vec3 normal;
    
    void main() {
        gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
        outColor = vec4(inColor, 1.0);        
        UVs = texCoords;
        normal = (modelMatrix * vec4(normals, 0.0)).xyz;
    }
"""

bug_shader = """
#version 450 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 inColor;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float time;

out vec4 outColor;
out vec2 UVs;
out vec3 normal;

void main() {
    // Varía la distorsión según el tiempo
    float distortion = 0.1 * sin(time);

    vec3 distortedPosition = position + distortion * vec3(sin(position.y), cos(position.x), sin(position.z));

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(distortedPosition, 1.0);

    outColor = vec4(inColor, 1.0);
    UVs = texCoords;
    normal = (modelMatrix * vec4(normals, 0.0)).xyz;
}


"""

exploding_vertex_shader = """
    #version 450 core
    layout (location = 0) in vec3 inPosition;
    layout (location = 1) in vec3 inColor;
    layout (location = 1) in vec2 inTexCoords;
    layout (location = 2) in vec3 inNormals;
    
    uniform mat4 modelMatrix;
    uniform mat4 viewMatrix;
    uniform mat4 projectionMatrix;

    uniform float time;
    
    out vec4 outColor;
    out vec2 UVs;
    out vec3 normal;
    
    void main() {
        vec3 pos = inPosition;

        pos.y += sin(time * pos.y);
        pos.x += sin(time * pos.x)/2;
        pos.z += sin(time * pos.z)/3;

        gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(pos, 1.0);
        outColor = vec4(inColor, 1.0);        
        UVs = inTexCoords;
        normal = (modelMatrix * vec4(inNormals, 0.0)).xyz;
    }
"""

coloring_wave_shader = """
#version 450 core
    uniform float time;
    
    in vec2 UVs;
    out vec4 fragColor;
void main() {

    float r = 0.5 + 0.5 * sin(UVs.x * 10.0 + time);
    float g = 0.5 + 0.5 * sin(UVs.y * 10.0 + time);
    float b = 0.5 + 0.5 * cos(UVs.x * 10.0 - UVs.y * 10.0 + time);

    fragColor = vec4(r, g, b, 1.0);
}

"""

water_texture_shader = """
#version 450 core

layout (binding = 0) uniform sampler2D tex;
uniform float time;

in vec2 UVs;
in vec3 normal;
out vec4 fragColor;

void main() {
    vec2 uv = UVs;
    uv.y += 0.1 * sin(uv.x * 10.0 + time);
    vec4 color = texture2D(tex, uv);
    fragColor = color;
}
"""


fragment_shader = """
    #version 450 core
    in vec4 outColor;
    
    layout (binding = 0) uniform sampler2D tex;
    
    in vec2 UVs;
    in vec3 normal;
    out vec4 fragColor;
    
    void main() {
        fragColor = outColor;
        fragColor = texture(tex, UVs);
    }
"""