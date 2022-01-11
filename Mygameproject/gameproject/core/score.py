"""score.py"""

import pygame,sys
import gameproject.conf.setting as st

class S:
    def __init__(self,screen):
        self.screen=screen
        self.f = pygame.font.SysFont('simsunnsimsun', 25)  # 射击界面得分数文字的font

    def update(self):
        st.s_now+=st.s_add[st.round_flag-1]

    def draw(self):
        self.s_text = self.f.render('总分(至少)：' + str(st.s_total[st.round_flag-1]) + ' 当前得分：' + str(st.s_now), True, (255, 255, 255))
        self.screen.blit(self.s_text, (0, 0))

#第二关 总分变 敌人变 子弹个数变
