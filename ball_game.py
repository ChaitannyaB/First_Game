import pygame
import random
pygame.init()
#colurs
yellow = (255, 191, 0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#direction movement var
vel_l=0
vel_r=0
vel_d=0
vel_u=0
#score
score=0
#random box coords
sp_x = random.randint(50,400)
sp_y = random.randint(100,300)
#create window
gameWindow=pygame.display.set_mode((700,500))
pygame.display.set_caption("Ball Game")
pygame.display.update()
#initial value
exit_game=False
game_over=False
ball_x=500
ball_y=400

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,50)
#text display
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
#game loop
while not exit_game:
    gameWindow.fill(green)
    text_screen("Score: "+str(score),red,10,20)
    if game_over:
        text_screen("GAME OVER!",red,220,210)
        text_screen("Press R to restart.",red,220,300)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        #if keyboard is used
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                game_over=False
                score=0
                ball_x=500
                ball_y=400
                vel_u=0
                vel_d=0
                vel_l=0
                vel_r=0
                sp_x = random.randint(50,400)
                sp_y = random.randint(100,300)
            if event.key==pygame.K_SPACE:
                vel_u=0
                vel_d=0
                vel_l=0
                vel_r=0
            if event.key==pygame.K_UP or event.key==pygame.K_w:
                vel_u=-10
                vel_l=0
                vel_r=0
                vel_d=0
            if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                vel_l=-10
                vel_r=0
                vel_d=0
                vel_u=0
            if event.key==pygame.K_DOWN or event.key==pygame.K_s:
                vel_d=10
                vel_l=0
                vel_r=0
                vel_u=0
            if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                vel_r=10
                vel_l=0
                vel_d=0
                vel_u=0
    #change ball coords and update score
    if not game_over:
        ball_x=ball_x+vel_l+vel_r
        ball_y=ball_y+vel_d+vel_u
        if(ball_x<0 or ball_x>700):
            game_over=True
        if(ball_y<0 or ball_y>500):
            game_over=True
        if((ball_x>=0 and ball_x<=sp_x) and (ball_y>=sp_y and ball_y<=sp_y+60)):
            game_over=True
        if((ball_x>=sp_x+60 and ball_x<=700) and (ball_y>=sp_y and ball_y<=sp_y+60)):
            game_over=True
        if abs(sp_x+22-ball_x)<20 and abs(sp_y+22-ball_y)<20:
            score +=10
            c_y = sp_y
            #bugfix 1: random board generated farther from Ball
            if(vel_u!=0):
                sp_x = random.randint(50,500)
                #bugfix 2: fixed board going out of bounds
                if(sp_y+50<=350):
                    sp_y = random.randint(sp_y+50,350)
                else:
                    sp_y = random.randint(60,sp_y-100)
            else:
                sp_x = random.randint(50,500)
                #bugfix 2
                if(sp_y-50>=60):
                    sp_y = random.randint(60,sp_y-50)
                else:
                    sp_y = random.randint(sp_y+100,350)
        #draw ojects in window
        pygame.draw.rect(gameWindow,yellow,[0,sp_y,sp_x,60])
        pygame.draw.rect(gameWindow,yellow,[sp_x+60,sp_y,700-60-sp_x,60])
        pygame.draw.rect(gameWindow,blue,[sp_x,sp_y,60,60])
        pygame.draw.circle(gameWindow,red,[ball_x,ball_y],20,0)
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()