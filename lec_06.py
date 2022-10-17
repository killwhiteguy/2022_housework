#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 08:00:13 2022

@author: swx
"""

import pygame
width, height = screen_size = (500, 400)
pygame.init()
screen = pygame.display.set_mode(screen_size)

# здесь будут рисоваться фигуры
# draw_picture(screen)
# ...

pygame.display.update()

work_flag = True
while work_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            work_flag = False

print("Программа благополучно завершена.")