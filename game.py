import pygame
pygame.init()
screen=pygame.display.set_mode((1037,518))
pygame.display.set_caption('GIẤC MỘNG IDOL(tuanpr)')
BLUE=(0,0,0)
RED=(255,0,0)
background_x=0
background_y=1
dinosaur_x=200
dinosaur_y=345
tree_x=750
tree_y=412
x_verocity=6
y_verocity=3
score=(0)
font=pygame.font.SysFont('san',40)
font1=pygame.font.SysFont('san',41)
background=pygame.image.load('nenok.jpg')
dinosaur=pygame.image.load('ratok.jpg')
tree=pygame.image.load('okroi.jpg')
sound=pygame.mixer.Sound('tit.wav')
sound1=pygame.mixer.Sound('tieng.wav')
clock=pygame.time.Clock()
jump=False
pausing=False
running=True
while running:
    clock.tick(60)
    screen.fill(BLUE)
    background1_rect=screen.blit(background,(background_x,background_y))
    background2_rect=screen.blit(background,(background_x+1037,background_y))
    score_txt=font.render("yêu em:"+str(score),True,RED)
    screen.blit(score_txt,(5,480))
    gameover_txt=font1.render("(game)",True,RED)
    screen.blit(gameover_txt,(450,480))
    if background_x+1037<=0:
        background_x=0
    tree_x-=x_verocity
    if tree_x<=-50:
        tree_x=1000
        score+=5
    if 345>=dinosaur_y>=200:
        if jump==True:
            dinosaur_y-=y_verocity
    else:
        jump=False 
    if dinosaur_y<345:
        if jump==False:
            dinosaur_y+=y_verocity
    dinosaur_rect=screen.blit(dinosaur,(dinosaur_x,dinosaur_y))
    tree_rect=screen.blit(tree,(tree_x,tree_y))
    background_x-=x_verocity
    if dinosaur_rect.colliderect(tree_rect):
        pausing=True
        gameover_txt=font1.render("gãy cánh!!",True,RED)
        screen.blit(gameover_txt,(370,250)) 
        x_verocity=0.5
        y_verocity=0  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                gameover_txt=font1.render("LÊNNN!!",True,RED)
                screen.blit(gameover_txt,(360,250))
                if dinosaur_y==345:
                    pygame.mixer.Sound.play(sound1)
                    pygame.mixer.Sound.play(sound)
                    jump=True
                    
                    
                    
                    
    pygame.display.flip()
pygame.quit
Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pygame
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pygame
ImportError: No module named 'pygame'
def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

list = [129, 831 ,014]
length = len(list)
i = 0

# Iterating using while loop
while i < length:
    a = list[i]
    print(permute_string(str(a)))
    i += 1;
