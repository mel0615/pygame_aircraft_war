"""end.py"""

import pygame,sys
import gameproject.conf.setting as st

class Endpage:
    def __init__(self,bgfile,screen):
        self.screen=screen
        self.bgfile=bgfile
        self.bg = pygame.image.load(self.bgfile)

        if self.bgfile=='gameproject\\images\\2019.png': #背景上的小图片
            self.bg = pygame.transform.scale(self.bg, (300, 300))
        self.r_bg=self.bg.get_rect()

        # 结束界面的背景图移动的相关变量
        if self.bgfile=='gameproject\\images\\bg2.jpeg': #背景
            self.y=0
        elif self.bgfile=='gameproject\\images\\2019.png': #背景上的小图片
            self.r_bg.centerx=st.length//2
            self.r_bg.top=200

    def process(self,myfont1_text): #结束界面处理函数
        if self.bgfile=='gameproject\\images\\bg2.jpeg': #背景
            if self.y > -(1920 - st.width):
                self.y -= 1
            self.screen.blit(self.bg, (0, self.y))
        if self.bgfile=='gameproject\\images\\2019.png': #背景上的小图片
            self.screen.blit(self.bg, self.r_bg)
            self.screen.blit(myfont1_text, (400, 500))  # 写endgame文字
