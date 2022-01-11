"""rocket.py"""

import pygame,sys
import gameproject.conf.setting as st

class R:
    def __init__(self,screen,filepath):
        #图片缩放：self.img=pygame.transform.scale(self.img,(90,150))
        self.img=pygame.image.load(filepath)
        self.img=pygame.transform.scale(self.img,(40,80))

        self.screen=screen
        self.s=self.screen.get_rect()
        self.rect=self.img.get_rect() #火箭长110，宽246
        #print(i.center, i.centerx, i.centery, i.top, i.bottom, i.left, i.right)
        #      (55,123)      55         123      0       246       0       110
        self.rect.centerx=self.s.centerx
        self.rect.bottom=self.s.bottom

        #判断键盘按是否长按 设置为连续移动标志
        self.moveright=False
        self.moveleft=False
        self.moveup=False
        self.movedown=False

        #图片旋转：self.img=pygame.transform.rotate(self.img,30)
        #self.img = pygame.transform.rotate(self.img, 20)
        #旋转 标志
        #self.formerdir=0
        #self.dirleft=False
        #self.dirright=False



    def draw(self): #显示火箭
        self.screen.blit(self.img,self.rect)

    def update(self): #移动火箭 移动速度放到配置文件setting中
        if self.moveright==True:
            if self.rect.right<=self.s.right-st.speed:
                self.rect.right+=st.speed
            else:
                self.rect.right=self.s.right
        if self.moveleft==True:
            if self.rect.left>=st.speed:
                self.rect.left-=st.speed
            else:
                self.rect.left=0
        if self.moveup==True:
            if self.rect.top>=st.speed:
                self.rect.top-=st.speed
            else:
                self.rect.top=0
        if self.movedown==True:
            if self.rect.bottom<=self.s.bottom-st.speed:
                self.rect.bottom+=st.speed
            else:
                self.rect.bottom=self.s.bottom
