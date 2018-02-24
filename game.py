import random
import pygame
import time
from pygame.locals import *

class Base(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.bullet_list = []	


class BasePlane(Base):
    def __init__(self,screen_temp,x,y,image_name_temp):
        Base.__init__(self,screen_temp,x,y,image_name_temp)
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
    
#        print(len(self.bullet_list))

class BaseBullet(Base):
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

class HeroPlane(BasePlane):
    def __init__(self,screen_temp,enemy_temp):
        BasePlane.__init__(self,screen_temp,210,700,"./image/hero1.png")
        self.enemy = enemy_temp #需要获取的位置
    
    def move_left(self):
        self.x -=5
    def move_right(self):
        self.x +=5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y,self.enemy))

class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y,enemy_temp): 
        self.x = x+47
        self.y = y-20
        self.screen = screen_temp
        self.image = pygame.image.load("./image/bullet1.png")
        self.enemy = enemy_temp#获取敌机的位置
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y-=5
        if self.y<39 and (self.x>=self.enemy.x and self.x <= self.enemy.x+51):
            #print("boooooooooooooooooooooooom!!!!")
            self.enemy.destroy = 1
        #print("addr is %d"%self.y)

    def judge(self):
        if self.y<0:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    def __init__(self,screen_temp,x,y): 
        self.x = x+25
        self.y = y+40
        self.screen = screen_temp
        self.image = pygame.image.load("./image/bullet2.png")

    def move(self):
        self.y+=5
    def judge(self):
        if self.y>852:
            return True
        else:
            return False

class EnemyPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,0,0,"./image/enemy1.png") 
        self.direction="right"
        self.destroy = 0 #判断飞机是否摧毁
        #敌机毁坏四连
        self.down1_image_small = pygame.image.load("./image/enemy1_down1.png")

        self.down2_image_small = pygame.image.load("./image/enemy1_down2.png")

        self.down3_image_small = pygame.image.load("./image/enemy1_down3.png")

        self.down4_image_small = pygame.image.load("./image/enemy1_down4.png")

    
    def bomb(self):
        count = 1
        i = random.randint(1,400)
        while count <=4:
            if i == 9 :
                if count ==1:
                    self.screen.blit(self.down1_image_small,(self.x,self.y))
                    count +=1
                if count ==2:
                    self.screen.blit(self.down2_image_small,(self.x,self.y))
                    count +=1
                if count ==3:
                    self.screen.blit(self.down3_image_small,(self.x,self.y))
                    count +=1
                if count ==4:
                    self.screen.blit(self.down4_image_small,(self.x,self.y))
                    count +=1
                i = random.randint(1,400)
            else:
                i = random.randint(1,400)
        """
        print("bobobobobo!!!!!!!!!!!!!!!")
        print("121111111111111111111")
        print("2222222222222222222222")
        print("33333333333333333333333333")
        """

    
    def move(self):
        if self.destroy == 0:
            if self.direction == "right":
                self.x +=5
            else:
                self.x -= 5

            if self.x >430:
                self.direction="left"
            elif self.x<0:
                self.direction="right"
        elif self.destroy == 1:
            self.bomb()
            self.destroy = 2
        else:
            pass
    def fire(self):
        ran_num=random.randint(1,100)
        if ran_num==78 or ran_num==9:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))
        
def key_control(hero_temp):
    
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                #print('left')
                hero_temp.move_left()

            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                #print('right')
                hero_temp.move_right()

            #检测按键是否是空格键
            elif event.key == K_SPACE:
                #print('space')
                hero_temp.fire()

def main():
    screen = pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load("./image/background.png")
    enemy1 = EnemyPlane(screen)
    
    hero = HeroPlane(screen,enemy1)

    while True:
        screen.blit(background,(0,0))
        hero.display()

        enemy1.display()
        enemy1.move()
        enemy1.fire()

        pygame.display.update() 
        key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()
