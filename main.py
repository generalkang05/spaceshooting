import pygame
import random
import time
from datetime import datetime
# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
# size =  [400, 900]
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 400

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

title = "Shooting"
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def put_image(self, address):
        if address[-3:] == "png":
            self.image = pygame.image.load(address).convert_alpha()
        else:
            self.image = pygame.image.load(address)
        
        (self.x_size, self.y_size) =  self.image.get_size()
    
    def change_size(self, size_x, size_y):
        self.image = pygame.transform.scale(self.image, (size_x, size_y))
        (self.x_size, self.y_size) =  self.image.get_size()
    
    def show(self):
        screen.blit(self.image, (self.x, self.y))

def crash(a, b):
    if (a.x - b.x_size <= b.x) and (b.x <= a.x + a.x_size):
        if (a.y - b.y_size <= b.y) and (b.y <= a.y + a.y_size):
            return True
        else:
            return False
    else:
        return False


fighter = obj()
fighter.put_image("img/fighter.png")
fighter.change_size(50, 80)
fighter.x = SCREEN_WIDTH / 2 - fighter.x_size / 2 
fighter.y = SCREEN_HEIGHT - fighter.y_size 
fighter.move = 5

left_go = False
right_go = False
space_go = False
missile_list = []
rock_list = []


color = (0, 0, 0)
k = 0

GO = 0
kill = 0
loss = 0

# 4-0 게임 시작 대기 화면 
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
    screen.fill(color)
    font = pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 15)
    text = font.render("PRESS SPACE KEY TO START THE GAME", True, (255, 255, 255))
    screen.blit(text, (40, SCREEN_HEIGHT / 2 - 50))
    pygame.display.flip()
# 4. 메인 이벤드
start_time = datetime.now()
running = True
while running:
    # 4-1. FPS 설정
    clock.tick(60)
    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # fighter.x -= fighter.move
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
                k = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                # fighter.x -= fighter.move
                left_go = False
            elif event.key == pygame.K_RIGHT:
                # fighter.x += fighter.move
                right_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False
    # 4-3. 입력, 시간에 따른 변화
    now_time = datetime.now()
    delta_time = round((now_time - start_time).total_seconds())      



    if left_go == True:
        fighter.x -= fighter.move
        if fighter.x <= 0:
            fighter.x = 0
    elif right_go == True:
        fighter.x += fighter.move
        if fighter.x >= SCREEN_WIDTH - fighter.x_size:
            fighter.x = SCREEN_WIDTH - fighter.x_size
    
    if space_go == True and k % 10  == 0:
        missile = obj()
        missile.put_image("img/missile.png")
        missile.change_size(5, 15)
        missile.x =  round(fighter.x + fighter.x_size / 2 - missile.x_size / 2)
        missile.y = fighter.y - missile.y_size - 10
        missile.move = 15
        missile_list.append(missile)
    k += 1
    
    d_list = []
    for i in range(len(missile_list)):
        m = missile_list[i]
        m.y -= m.move
        if m.y <= -m.y_size:
            d_list.append(i)
    
    for d in d_list:
        del missile_list[d]

    if random.random() > 0.98:
        rock = obj()
        rock.put_image("img/rock01.png")
        rock.change_size(40, 40)
        rock.x =  random.randrange(0, SCREEN_WIDTH - rock.x_size) 
        rock.y = 10
        rock.move = 5
        rock_list.append(rock)
    d_list = []
    for i in range(len(rock_list)):
        r = rock_list[i]
        r.y += r.move
        if r.y >= SCREEN_HEIGHT:
            d_list.append(i)
    
    for d in d_list:
        del rock_list[d]
        loss += 1

    dm_list = []
    dr_list = []
    for i in range(len(missile_list)):
        for j in range(len(rock_list)):
            m = missile_list[i]
            r = rock_list[j]
            if crash(m, r) == True:
                dm_list.append(i)
                dr_list.append(j)
    dm_list = list(set(dm_list))
    dr_list = list(set(dr_list))

    for dm in dm_list:
        del missile_list[dm]
    for dr in dr_list:
        del rock_list[dr]
        kill += 1
    
    for i in range(len(rock_list)):
        r = rock_list[i]
        if crash(r, fighter) == True:
            running = False
            GO = 1




    # 4-4. 그리기
    screen.fill(color)
    fighter.show()
    for m in missile_list:
        m.show()
    for m in rock_list:
        m.show()    

    font = pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 20)
    text_kill = font.render("killed : {} loss: {}".format(kill, loss), True, (255, 255, 0))
    screen.blit(text_kill, (10, 5))

    text_time = font.render("time : {}".format(delta_time), True, (255, 255, 255))
    screen.blit(text_time, (SCREEN_WIDTH - 100, 5))

    # 4-5. 업데이트
    pygame.display.flip()
# 5. 게임 종료
while GO == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GO = 0
    font = pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 40)
    text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text, (80, SCREEN_HEIGHT / 2 - 50))
    pygame.display.flip()
pygame.quit()