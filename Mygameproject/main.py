"main.py"

import pygame
from gameproject.conf import setting as st
from gameproject.core import functionsgame,begin,end,score

#初始化pygame
pygame.init()

"""
播放背景音乐

wav音频加载播放
s=pygame.mixer.Sound('...')
s.play()
mp3音频加载播放
s=pygame.mixer.music.load('...')
s.play()
"""
#初始化背景音乐
pygame.mixer.init()
pygame.mixer.music.load('./gameproject/media/glory.mp3')
pygame.mixer.music.play(-1) #第一个参数-1为循环播放

"""
将屏幕的宽和高两个对象单独放到配置文件setting.py中
屏幕的宽高希望能改，全屏/小屏，放到setting中

获取屏幕的值
s=screen.get_rect()
s.center  .centerx  .centery  .top  .bottom  .left  .right

获取图片的值  根据这两个值确定图片在屏幕的位置
r_img=img.get_rect()
r_img.center  。。。
"""
#设置pygame界面的长和宽以及是否全屏
if st.fullflag:
    screen=pygame.display.set_mode((0,0),st.fullflag,32)
else:
    screen=pygame.display.set_mode((st.length,st.width))



"""
加载图片(火箭)
img=pygame.image.load('./gameproject/images/rocket.png')

火箭单独形成一个类
屏幕绘图在火箭类里
调用火箭类的某个方法，图片就能调进来
"""
#创建火箭类对象
from gameproject.core import rocket
r=rocket.R(screen,'./gameproject/images/rocket.png')

"""
要有子弹，子弹有宽 高 颜色 各种属性，子弹是一个对象，还有方法
子弹发射的初始位置-与火箭当时的位置有关
空格发射子弹

子弹形成一个精灵组
"""
#引入子弹精灵组
from pygame.sprite import Group
bs=Group() #创建一个存储子弹的精灵组

"""
敌人：随机出现，满足移动(临界-到边时弹回)，使用精灵
有自己的属性方法，有大有小，移动速度
敌人形成一个精灵组
"""
#引入敌人精灵组
import gameproject.core.enemy as ey
from pygame.sprite import Group
es=Group() #创建一个存储敌人的精灵组
for i in range(st.enemy_num[0]): #创建敌人
    e = ey.E(screen,'./gameproject//images//monster.png')
    es.add(e)



"""
想要支持中文，在windows/font/下面，把字体文件拷进来，拷到gameproject下新建一个font中
然后以文档路径的方式导进来即可

或在设置文字font时把None(默认)改成中文'simsunnsimsun'
"""
#三个界面
bg1 = begin.Beginpage('./gameproject/images/bg1.jpg',screen)  # 开始界面背景
bg2 = begin.Beginpage('./gameproject/images/go.png',screen)  # 开始界面前景图
background = begin.Beginpage('./gameproject/images/bg.jpg',screen)  # 射击界面背景1
background1= begin.Beginpage('./gameproject/images/bg0.jpg',screen) # 射击界面背景2
bg3 = end.Endpage('./gameproject/images/bg2.jpeg',screen)  # 结束界面背景
bg4 = end.Endpage('./gameproject/images/2019.png',screen)  # 结束界面前景图
#显示的游戏文字
myfont = pygame.font.SysFont(None, 30)  # 开始界面文字
myfont_text = myfont.render('ENTER GAME', True, (255, 255, 255))  # True：开启抗锯齿 字边缘光滑
myfont1 = pygame.font.SysFont(None, 30)  # 结束界面文字
myfont1_text = myfont1.render('THANKS FOR PLAYING AND HAPPY NEW YEAR', True, (255, 255, 255))

#游戏积分：总分500 当前得分30 显示的文字累加
#把score形成一个类，设置对象传给碰撞检测函数
s = score.S(screen)



pygame.display.set_caption('My Game~')
pygame.display.update()

while True:
    functionsgame.event_handle(screen,r,bs,es,myfont_text) #事件操作

    if st.page_flag == 0:  # 开始界面 使背景移动
        bg1.process(myfont_text)
        if st.begin_flag==1: # 背景停下后小图片进入 最后显示文字
            bg2.process(myfont_text)

    elif st.page_flag == 1 and st.round_flag==1:  # （按ENTER）切换到射击界面1
        functionsgame.fun_update(screen, background, r, bs, es, s)  # 更新测绘
        functionsgame.fun_collide(screen, r, bs, es, s)  # 碰撞检测

    elif st.page_flag ==1 and st.round_flag==2: # 射击界面2
        functionsgame.fun_update(screen, background1, r, bs, es, s)  # 更新测绘
        functionsgame.fun_collide(screen, r, bs, es, s)  # 碰撞检测

    elif st.page_flag==2:  # enemy没有了 切换到结束界面
        bg3.process(myfont1_text)
        bg4.process(myfont1_text)

    pygame.display.update() #更新屏幕
