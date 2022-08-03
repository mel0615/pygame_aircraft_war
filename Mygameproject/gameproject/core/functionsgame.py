"""functionsgame.py"""

import pygame,sys,time
import gameproject.core.bullet as bt
import gameproject.conf.setting as st
import gameproject.core.enemy as ey
from gameproject.core import rocket

def event_handle(screen,r,bs,es,myfont_text): #事件处理函数
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #退出
            pygame.quit()
            sys.exit()

        # 改变火箭位置   事件不要放到rocket.py的方法中
        if event.type == pygame.KEYDOWN:  # 按下了某个键
            if event.key == pygame.K_ESCAPE: #Esc
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT: #右
                r.moveright = True
            if event.key == pygame.K_LEFT: #左
                r.moveleft = True
            if event.key == pygame.K_UP: #上
                r.moveup = True
            if event.key == pygame.K_DOWN: #下
                r.movedown = True
            if event.key == pygame.K_SPACE: #空格
                if len(bs)<st.bullet_num[st.round_flag-1]: #子弹数限制 不同关卡不一样
                    b = bt.B(screen, r)  # 创建一枚子弹
                    bs.add(b)  # 将子弹加入精灵组
                    b.music() # 发射子弹音效
            if event.key == pygame.K_RETURN: #回车
                st.page_flag=1
        if event.type == pygame.MOUSEBUTTONDOWN: #鼠标点击
            mousex,mousey=pygame.mouse.get_pos() #获取鼠标落点坐标
            r_mf = myfont_text.get_rect()  # 获取开始界面文字的矩形
            if mousex>780 and mousex<780+r_mf.right and mousey>400 and mousey<400+r_mf.bottom:
                st.page_flag=1
        if event.type == pygame.KEYUP:  # 松开了某个键
            r.moveright = False
            r.moveleft = False
            r.moveup = False
            r.movedown = False



def fun_update(screen,background,r,bs,es,s): #更新和绘制函数

    screen.blit(background.bg,(0,0))  #对齐的坐标

    # 显示分数文字
    s.draw()

    r.update()  # 火箭更新位置

    # 显示图片 screen.blit(img,(250,250)) 后面的元组表示img左上角那一点的位置
    # 调用火箭类中-导入火箭图片-的方法
    r.draw()

    # 子弹要到边界消失，并限制子弹的数量
    bs.update()  # 精灵组调用了update()，实际上是调用了每个子弹的update()
    for i in bs:
        if i.rect.bottom <= 0:
            bs.remove(i)
        i.draw()

    es.update()  # 敌人更新绘制
    for j in es:
        j.draw()



def fun_collide(screen,r,bs,es,s): #碰撞检测函数
    # 子弹组与敌人组的碰撞检测
    collide = pygame.sprite.groupcollide(bs, es, True, True)  # (组1,组2,1死,2死)
    if any(collide):  #是否为空。只要有内容就为True
        # 碰撞时的音效
        pygame.mixer.Sound('./gameproject/media/fire.wav').play()
        # 碰撞的图片效果
        '''
        img = pygame.image.load('gameproject\\images\\boom.png')
        img = pygame.transform.scale(img, (50, 50))
        i_rect = img.get_rect()
        i_rect.centerx = r.rect.centerx
        i_rect.bottom = r.rect.top
        screen.blit(img, i_rect)
        pygame.display.update()
        time.sleep(1)
        '''
        # 子弹消灭enemy一次则更新一次分数
        s.update()

    if len(es)==0: #打完全部enemy
        if st.round_flag==1: #进入第二关
            st.round_flag=2
            for i in range(st.enemy_num[st.round_flag-1]):  # 创建第二关的敌人
                e = ey.E(screen,'./gameproject/images/chicken.png')
                es.add(e)
            #r = rocket.R(screen, 'gameproject\\images\\ghost.png')
        else: #进入结束界面
            st.page_flag=2

    # 火箭与敌人组的碰撞检测
    collide1 = pygame.sprite.spritecollide(r, es, True)
    if any(collide1): #火箭碰到一个enemy则游戏结束
        print('GAME OVER')
        st.page_flag=2
