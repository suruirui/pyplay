# -*- coding:utf-8 -*-

import time
import pygame, sys
from pygame.locals import *

pygame.init()

def main():
    #1. 创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    pygame.display.set_caption('AircraftWars')
    # 2.设置背景图片
    # background = pygame.image.load('./images/background.png')
    background = pygame.image.load("background.png")

    # 3.创建一个飞机图片
    # hero = pygame.image.load("./images/hero1.png")
    #hero = pygame.image.load("hero1.png")
    while True:
        screen.blit(background, (0, 0))

        # window.blit(hero, (210, 700))

        pygame.display.update()

        time.sleep(0.01)

if __name__ == "__main__":
    main()