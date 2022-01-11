"""enemy.py"""

import pygame,sys
from pygame.sprite import Sprite
import random

class E(Sprite):
    def __init__(self,screen,filepath):
        super().__init__() #调用父类初始化方法
        self.screen = screen
        self.s=self.screen.get_rect() #屏幕

        self.img = pygame.image.load(filepath)
        self.img = pygame.transform.scale(self.img, (45, 45))
        self.rect = self.img.get_rect()  #敌人

        #随机确定当前enemy对象的初始位置
        self.rect.top=random.randint(1,self.s.bottom-80-45-1)
        self.rect.left=random.randint(1,self.s.right-45-1)

        #随机确定当前enemy对象运动的初始方向
        self.a=random.choice([1,-1])
        self.b=random.choice([-1,1])



    def draw(self):
        self.screen.blit(self.img, self.rect)

    def update(self):
        self.rect.left += self.a
        self.rect.top += self.b
        if self.rect.right == self.s.right:
            self.a = -1
        if self.rect.left == 0:
            self.a = 1
        if self.rect.top == 0:
            self.b = 1
        if self.rect.bottom == self.s.bottom-80-1:
            self.b = -1
