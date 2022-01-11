"""begin.py"""

import pygame,sys
import gameproject.conf.setting as st

class Beginpage:
    def __init__(self,bgfile,screen):
        # 设置游戏时界面的背景图片
        # screen.fill((221,244,255)) #屏幕纯色背景
        self.screen=screen
        self.bgfile=bgfile
        self.bg = pygame.image.load(self.bgfile)

        if self.bgfile=='gameproject\\images\\go.png': #背景上的小图片
            self.bg = pygame.transform.scale(self.bg, (286, 164))
        self.r_bg=self.bg.get_rect()

        # 开始界面的背景图移动的相关变量
        if self.bgfile=='gameproject\\images\\bg1.jpg': #背景
            self.y=0
        elif self.bgfile=='gameproject\\images\\go.png': #背景上的小图片
            self.r_bg.right=0
            self.r_bg.top=st.width//2

    def process(self,myfont_text): #处理函数
        if self.bgfile == 'gameproject\\images\\bg1.jpg':  # 背景
            if self.y > -(1920 - st.width):
                self.y -= 1
            if self.y == -(1920 - st.width):
                st.begin_flag=1
            self.screen.blit(self.bg, (0, self.y))

        if self.bgfile=='gameproject\\images\\go.png': #背景上的小图片
            if st.begin_flag==1:
                if self.r_bg.right < st.length // 2 + 143:
                    self.r_bg.right += 1
                self.screen.blit(self.bg, self.r_bg)
                if self.r_bg.right == st.length // 2 + 143:  # 写entergame文字
                    self.screen.blit(myfont_text, (780, 400))
