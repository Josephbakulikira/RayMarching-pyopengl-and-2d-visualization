from __future__ import division
import sys
import pygame
from pygame.locals import *
from shader import *
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy import array, linalg, frombuffer, fromstring, short
from OpenGL.GL import shaders
from sys import exit as exitsystem
from math import cos, sin, pi
from Vector import *
from utils import *


class Main(object):
    def __init__(self):
        pygame.init()
        self.resolution = 800, 600
        #self.camera = Camera(Vector3(0.0, 0.0, 0.0), Vector3(0.0, 1.0, 0.0), -90.0, 0.0, 5.0, 0.2)
        #self.projectionMatrix = perspective_fov(45.0, self.resolution[0]/self.resolution[1], 0.1, 100.0)
        self.identity = np.array([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        pygame.display.set_mode(self.resolution, DOUBLEBUF | OPENGL)
        pygame.display.set_caption('Ray Marching')

        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        
        # quad vertices
        self.vertices = array([-1.0, -1.0, 0.0,
                                1.0, -1.0, 0.0,
                                1.0,  1.0, 0.0,
                               -1.0,  1.0, 0.0], dtype='float32')
        # compile and attach Shaders
        self.vertex_shader = shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
        self.fragment_shader = shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
        self.shader = shaders.compileProgram(self.vertex_shader, self.fragment_shader)

        # Uniform variables
        self.uniformMouse = glGetUniformLocation(self.shader, 'u_mouse')
        self.uniformTime = glGetUniformLocation(self.shader, 'u_time')
        self.uniformValue = glGetUniformLocation(self.shader, 'u_value')
        #self.uniformProjection = glGetUniformLocation(self.shader, 'u_projection')
        self.uniformModel = glGetUniformLocation(self.shader, 'u_model')
        glUseProgram(self.shader)


        # self.uniformCameraPosition = glGetUniformLocation(self.shader, "u_camPosition")
        # self.uniformOrientation = glGetUniformLocation(self.shader, 'u_orientation')
        # self.uniformViewDistance = glGetUniformLocation(self.shader, 'u_viewDistance')
        #self.uniformView = glGetUniformLocation(self.shader, "u_view")
        self.uniformResolution = glGetUniformLocation(self.shader, 'u_resolution')
        glUniform2f(self.uniformResolution, *self.resolution)

        # generate Vertex array objects
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)



    def mainloop(self):

        while 1:
            #print(visualizer(self.num, self.wave_data, self.nframes))
            delta = self.clock.tick(8192)
            deltaTime = delta/1000.0
            glClearColor(0.0, 0.0, 0.0, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)

            for event in pygame.event.get():
                if (event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    exitsystem()

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 4:
                        pass


            glUseProgram(self.shader)

            # mouse coordinate in range of (-1, 1)
            mx, my = pygame.mouse.get_pos()

            mx = (1.0 / self.resolution[0] * mx) * 2.0 - 1.0
            my = (1.0 / self.resolution[1] * my) * 2.0 - 1.0


            glUniform2f(self.uniformMouse, mx, my)
            glUniform1f(self.uniformTime, pygame.time.get_ticks() / 1000.0)
            # binding vertex arrays objects
            glBindVertexArray(self.vao)
            glDrawArrays(GL_QUADS, 0, 4)

            pygame.display.set_caption("Program FPS: {}".format(self.clock.get_fps()))
            pygame.display.flip()



if __name__ == '__main__':
    Main().mainloop()
