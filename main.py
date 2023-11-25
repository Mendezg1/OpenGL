import pygame
import glm
from pygame.locals import *
import math

from renderer import Renderer
from model import Model
from shaders import *
from obj import Obj
def getFShader(id):
    shaders = [fragment_shader, coloring_wave_shader, water_texture_shader]
    return shaders[id]

def getVShader(id):
    shaders = [vertex_shader, bug_shader]
    return shaders[id]

def setShader(renderer, active_v, active_f):
    renderer.setShader(active_v, active_f)

def main():
    width = 960
    height = 540

    darken_effect = False
    rgb = [0,0,0]
    fs_index = 0
    vs_index = 0

    pygame.init()
    screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
    clock = pygame.time.Clock()

    renderer = Renderer(screen)

    active_f = fragment_shader
    active_v = vertex_shader

    renderer.setShader(active_v, active_f)

    #Hay 3 fragment Shaders y 2 vertex Shaders
    menu = """
    ------------PROGRAM MENU------------

    → = next fragment Shader
    ← = previous fragment Shader
    ↑↓ = change vertex Shader
    1 = House 3D Model
    2 = Dog 3D Model
    3 = Ovni 3D Model
    4 = Horse 3D Model
    L = Darken Effect
    R = Increase 'r' in model texture
    G = Increase 'g' in model texture
    B = Increase 'b' in model texture
    N = Reset Shaders, darken effect and rgb
    C = Print Menu
    ESC = Quit
"""

    #Caballo
    obj = Obj("Models/HORSE/caballo.obj")
    objinfo = []
    for face in obj.faces:
            for info in face:
                vertexs, textcords, normals = info
                vertex = obj.vertices[vertexs - 1]
                uv = obj.texcoords[textcords - 1]
                uv = [uv[0], uv[1]]
                normal = obj.normals[normals - 1]
                objinfo.extend(vertex + uv + normal)
    horse = Model(objinfo)
    horsetext = "Models/HORSE/caballo.png"
    #Ovni
    obj = Obj("Models/OVNI/ovni.obj")
    objinfo = []
    for face in obj.faces:
            for info in face:
                vertexs, textcords, normals = info
                vertex = obj.vertices[vertexs - 1]
                uv = obj.texcoords[textcords - 1]
                uv = [uv[0], uv[1]]
                normal = obj.normals[normals - 1]
                objinfo.extend(vertex + uv + normal)
    ovni = Model(objinfo)
    ufo = "Models/OVNI/Ufo.bmp"
    #Perro
    obj = Obj("Models/DOG/Perrito.obj")
    objinfo = []
    for face in obj.faces:
            for info in face:
                vertexs, textcords, normals = info
                vertex = obj.vertices[vertexs - 1]
                uv = obj.texcoords[textcords - 1]
                uv = [uv[0], uv[1]]
                normal = obj.normals[normals - 1]
                objinfo.extend(vertex + uv + normal)
    perrito = Model(objinfo)
    perritotext = "Models/DOG/Perrito.jpg"
    #Casa
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
    casa = Model(objinfo)
    casatext = "Models/H/casita.bmp"
    model = casa
    model.loadTexture(casatext)
    model.position = glm.vec3(0,0,-6)
    model.scale = glm.vec3(0.20, 0.20, 0.20)
    renderer.scene.append(model)
    renderer.center = model.position

    pygame.mixer.music.load("Sounds/Wind.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)

    def changeModel(id):
        renderer.scene.clear()
        if id == 1:
            model = casa
            model.loadTexture(casatext)
            model.position = glm.vec3(0,0,-6)
            model.scale = glm.vec3(0.20, 0.20, 0.20)
            renderer.scene.append(model)
            renderer.center = model.position
            pygame.mixer.music.load("Sounds/Wind.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.4)
        if id == 2:
            model = perrito
            model.loadTexture(perritotext)
            model.position = glm.vec3(0,9,-6)
            model.scale = glm.vec3(0.15, 0.15, 0.15)
            renderer.scene.append(model)
            renderer.center = model.position
            pygame.mixer.music.load("Sounds/Bark.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.4)
        if id == 3:
            model = ovni
            model.loadTexture(ufo)
            model.position = glm.vec3(0,0,-7)
            model.scale = glm.vec3(0.4, 0.4, 0.4)
            renderer.scene.append(model)
            renderer.center = model.position

            pygame.mixer.music.load("Sounds/Ovni.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.4)
        if id == 4:
            model = horse
            model.loadTexture(horsetext)
            model.position = glm.vec3(0,-12,-30)
            model.scale = glm.vec3(0.05, 0.05, 0.05)
            renderer.scene.append(model)
            renderer.center = model.position
            pygame.mixer.music.load("Sounds/Horse.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.4)

    isRunning = True
    dist = abs(renderer.cameraPosition.z - model.position.z)
    rad = dist
    theta = 0.0
    pressed = False

    print(menu)
    while isRunning:
        deltaTime = clock.tick(60) / 1000.0
        renderer.elapsedTime += deltaTime

        renderer.cameraPosition.x = model.position.x + rad * math.sin(theta)
        renderer.cameraPosition.z = model.position.z + rad * math.cos(theta)
        # Handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isRunning = False

                if event.key == K_1:
                    changeModel(1)
                if event.key == K_2:
                    changeModel(2)
                if event.key == K_3:
                    changeModel(3)
                if event.key == K_4:
                    changeModel(4)

                if event.key == K_RIGHT:
                    if fs_index < 2:
                        fs_index += 1
                    else:
                        fs_index = 0
                    
                    active_f = getFShader(fs_index)
                    setShader(renderer, active_v, active_f)
                    
                if event.key == K_LEFT:
                    if fs_index == 0:
                        fs_index = 2
                    else:
                        fs_index -= 1
                    
                    active_f = getFShader(fs_index)
                    setShader(renderer, active_v, active_f)
                if event.key == K_UP:
                    if vs_index < 1:
                        vs_index += 1
                    else: 
                        vs_index = 0
                    active_v = getVShader(vs_index)
                    setShader(renderer, active_v, active_f)
                if event.key == K_DOWN:
                    if vs_index == 1:
                        vs_index -= 1
                    else: 
                        vs_index = 1
                    active_v = getVShader(vs_index)
                    setShader(renderer, active_v, active_f)

                if event.key == K_d:
                    model.rotation.y += deltaTime * 50
                if event.key == K_a:
                    model.rotation.y -= deltaTime * 50
                if event.key == K_w:
                    model.rotation.x += deltaTime * 50
                if event.key == K_s:
                    model.rotation.x -= deltaTime * 50
                
                if event.key == K_l:
                    darken_effect = not darken_effect
                    renderer.setDarkenEffect(darken_effect)

                if event.key == K_r:
                    rgb[0] += 0.1
                    renderer.setRGB(rgb[0], 1)
                if event.key == K_g:
                    rgb[1] += 0.1
                    renderer.setRGB(rgb[1], 2)
                if event.key == K_b:
                    rgb[2] += 0.1
                    renderer.setRGB(rgb[2], 3)
                if event.key == K_n:
                    rgb = [0,0,0]
                    renderer.setRGB(0, 1)
                    renderer.setRGB(0, 2)
                    renderer.setRGB(0, 3)

                    darken_effect = False
                    renderer.setDarkenEffect(darken_effect)

                    active_f = fragment_shader
                    active_v = vertex_shader
                    setShader(renderer, active_v, active_f)

                    model.rotation.y = 0
                    model.rotation.x = 0

                if event.key == K_c:
                    print(menu)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    pressed = True
                    prev_pos = pygame.mouse.get_pos()

                elif event.button == 4:
                    rad -= 0.15
                    if rad < model.zin:
                        rad = model.zin            

                elif event.button == 5:
                    rad += 0.15
                    if rad > model.zout:
                        rad = model.zout

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  
                    pressed = False

            elif event.type == pygame.MOUSEMOTION:
                if pressed:
                    actual_pos = pygame.mouse.get_pos()
                    dx = actual_pos[0] - prev_pos[0]
                    theta += dx * 0.01
                    dy = actual_pos[1] - prev_pos[1]
                    renderer.cameraPosition.y -= dy * 0.01

                    if renderer.cameraPosition.y > model.ytop:
                        renderer.cameraPosition.y = model.ytop
                    if renderer.cameraPosition.y < model.ybot:
                        renderer.cameraPosition.y = model.ybot

                    prev_pos = actual_pos

        renderer.updateViewMatrix()
        renderer.render()
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()