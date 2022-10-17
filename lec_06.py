#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 08:00:13 2022

@author: swx
"""

import pygame

def draw_picture(screen, x, y, width, height):
        """  
        Рисует картинку с домиком на фоне травы и неба.
        
        :param screen: дисплей pygame, на котором будет изображение
        :param x: левая координата рисуемого прямоугольника с рисунком
        :param y: верхняя координата прямоугольника с рисунком
        :param widht: ширина прямоугольника
        :param height: высота прямоугольника
        """
        print("Типа рисую картинку", x, y, width, height)

width, height = screen_size = (500, 400)
pygame.init()
screen = pygame.display.set_mode(screen_size)

# здесь будут рисоваться фигуры
draw_picture(screen, 0, 0, width, height)
# ...

pygame.display.update()

work_flag = True
while work_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            work_flag = False

print("Программа благополучно завершена.")