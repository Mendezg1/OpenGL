import pygame
import glm
from pygame.locals import *

from renderer import Renderer
from model import Model
from shaders import *
from obj import Obj

def main():
    width = 960
    height = 540

    pygame.init()
    screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
    clock = pygame.time.Clock()

    renderer = Renderer(screen)
    renderer.setShader(vertex_shader, fragment_shader)
    # x, y, z, U, V, normal(x, y, z)
    
    obj = Obj("Models/H/casita.obj")
    objinfo = []
    for face in obj.faces:
            for info in face:
                vertexs, textcords, normals = info
                vertex = obj.vertices[vertexs - 1]
                uv = obj.texcoords[textcords - 1]
                uv = [uv[0], uv[1]]
                normal = obj.normals[normals - 1]
                objinfo.extend(vertex + uv + normal)
    model = Model(objinfo)
    model.loadTexture("Models/H/casita.bmp")
    model.position.z = -10
    model.position.y = 0
    model.rotation.x = 0
    model.scale = glm.vec3(0.20, 0.20, 0.20)
    renderer.scene.append(model)

    isRunning = True
    while isRunning:
        deltaTime = clock.tick(60) / 1000.0
        renderer.elapsedTime += deltaTime
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT]:
            renderer.clearColor[0] += deltaTime
        if keys[K_LEFT]:
            renderer.clearColor[0] -= deltaTime
        if keys[K_UP]:
            renderer.clearColor[1] += deltaTime
        if keys[K_DOWN]:
            renderer.clearColor[1] -= deltaTime
        if keys[K_SPACE]:
            renderer.clearColor[2] += deltaTime
        if keys[K_LSHIFT]:
            renderer.clearColor[2] -= deltaTime

        if keys[K_d]:
            obj.model.rotation.y += deltaTime * 50
        if keys[K_a]:
            obj.model.rotation.y -= deltaTime * 50
        if keys[K_w]:
            obj.model.rotation.x += deltaTime * 50
        if keys[K_s]:
            obj.model.rotation.x -= deltaTime * 50


        # Handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isRunning = False

        renderer.render()
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()