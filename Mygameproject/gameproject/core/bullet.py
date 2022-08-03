"""bullet.py"""

import pygame,sys
#子弹当作精灵，需要一个精灵组，统一管理。子弹类变成精灵子弹类-继承精灵类
from pygame.sprite import Sprite

class B(Sprite):
    def __init__(self,screen,r):
        super().__init__() #调用父类的初始方法
        self.screen=screen

        # 创建矩形子弹
        """
        self.rect=pygame.Rect(0,0,st.bullet_w,st.bullet_h) 
        self.color=st.bullet_color

        # 子弹的相对位置
        self.rect.centerx=r.rect.centerx
        self.rect.centery=r.rect.top-st.bullet_h//2
        """

        # 创建图形子弹
        self.img = pygame.image.load('./gameproject/images/bullet.png')
        self.img = pygame.transform.scale(self.img, (10,10))
        self.rect = self.img.get_rect()  #子弹
        self.length = self.rect.centerx*2 #子弹的长
        self.width = self.rect.centery*2 #子弹的宽

        # 子弹的相对位置
        self.rect.centerx = r.rect.centerx
        self.rect.centery = r.rect.top - self.width//2

        #wav音频加载
        #播放是在music()时
        self.r_sound = pygame.mixer.Sound('./gameproject/media/gun.wav')
        #mp3音频加载
        #pygame.mixer.music.load('gameproject\\media\\gun.mp3')

    def music(self):
        # wav音频播放
        self.r_sound.play()
        # mp3音频播放
        # pygame.mixer.music.play()

    def draw(self): #显示子弹
        # 画矩形子弹
        #pygame.draw.rect(self.screen,self.color,self.rect)

        # 画图形子弹
        self.screen.blit(self.img,self.rect)

    def update(self): #接口 父类的update没有执行体，必须在子类里进行重写
        self.rect.top -= 1
