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

<<<<<<< Updated upstream
=======
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
    float distortion = 0.4 * sin(time);

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

    uniform int darken_effect;
    uniform float r;
    uniform float g;
    uniform float b;
    
    in vec2 UVs;
    out vec4 fragColor;
void main() {

    float r = 0.5 + 0.5 * sin(UVs.x * 10.0 + time);
    float g = 0.5 + 0.5 * sin(UVs.y * 10.0 + time);
    float b = 0.5 + 0.5 * cos(UVs.x * 10.0 - UVs.y * 10.0 + time);

    fragColor = vec4(r, g, b, 1.0);

    if (darken_effect == 1) {
        fragColor.rgb *= 0.2;  
    }

     if( r > 0.0){
        fragColor.r *= r;
    }
    if( g > 0.0){
        fragColor.g *= g;
    }
    if( b > 0.0){
        fragColor.b *= b;
    }
}

"""

water_texture_shader = """
    #version 450 core

    layout (binding = 0) uniform sampler2D tex;
    uniform float time;
    uniform int darken_effect;
    uniform float r;
    uniform float g;
    uniform float b;

    in vec2 UVs;
    in vec3 normal;
    out vec4 fragColor;

    void main() {
        vec2 uv = UVs;
        uv.y += 0.1 * sin(uv.x * 10.0 + time);

        vec4 color = texture(tex, uv);

        if (darken_effect == 1) {
            color.rgb *= 0.2;  
        }

        if( r > 0.0){
            color.r *= r;
        }
        if( g > 0.0){
            color.g *= g;
        }
        if( b > 0.0){
            color.b *= b;
        }

        fragColor = color;
    }
"""


>>>>>>> Stashed changes
fragment_shader = """
    #version 450 core
    in vec4 outColor;

    uniform int darken_effect;
    uniform float r;
    uniform float g;
    uniform float b;
    
    layout (binding = 0) uniform sampler2D tex;

    in vec2 UVs;
    in vec3 normal;
    out vec4 fragColor;
    
    void main() {
        fragColor = outColor;
        vec4 color = texture(tex, UVs);

        if (darken_effect == 1) {
            color.rgb *= 0.2;  
        }

        if( r > 0.0){
            color.r *= r;
        }
        if( g > 0.0){
            color.g *= g;
        }
        if( b > 0.0){
            color.b *= b;
        }
        fragColor = color;
    }
"""