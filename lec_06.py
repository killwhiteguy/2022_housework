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
        #print("Типа рисую картинку", x, y, width, height)
        draw_background(screen, x, y, width, height)
        
        house_x = x + width // 2
        house_y = y + 3 * height // 4
        house_height = min(height, width) * 2 // 3
        house_width = int(house_height * 1.5)
        draw_house(screen, house_x, house_y, house_width, house_height)
        
        sun_radius = min(width, height) // 10
        draw_sun(screen, x, y, sun_radius)

def draw_background(screen, x, y, width, height):
    """  
        Рисует прямоугольный фон для картинки с травой и небом.
        
        :param screen: дисплей pygame, на котором будет изображение
        :param x: левая координата рисуемого прямоугольника с фоном
        :param y: верхняя координата прямоугольника с фоном
        :param widht: ширина прямоугольника
        :param height: высота прямоугольника
        """
    print("Типа рисую фон", x, y, width, height)
    
def draw_house(screen, x, y, widht, height):
    """  
        Рисует домик заданных размеров от точки (x, y).
        Внимание! Опорная точка находится посередине внизу основания
        
        :param screen: дисплей pygame, на котором будет изображение
        :param x: горизонтальная координата опорной точки
        :param y: вертикальная координата опорной точки
        :param widht: полная ширина домика
        :param height: полная высота домика
        """
    print("Типа рисую домик", x, y, width, height)
    
def draw_sun(screen, x, y, radius):
    """  
        Рисует солнышко в виде четверти круга справа снизу от опорной точки
        
        :param screen: дисплей pygame, на котором будет изображение
        :param x: горизонтальная координата опорной точки
        :param y: вертикальная координата опорной точки
        :param radius: радиус
        """
    print("Типа рисую солнышко", x, y, radius)

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