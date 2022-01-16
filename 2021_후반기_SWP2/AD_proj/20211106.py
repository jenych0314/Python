import pygame
import sys
import random
import math
from pygame.constants import KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_KP_ENTER, K_RETURN, K_SPACE, K_a, K_d, K_r, K_ESCAPE, K_s, K_w
from pygame.locals import QUIT, Rect

class Block:
    def __init__(self, color, rect, speed = 0):
        self.color = color
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270

    def move(self): # radians를 사용해서 방향(dir)을 라디안으로 변환, X축과 Y축의 방향 성분 구분
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw_circle(self): # 원으로 그리기
        pygame.draw.ellipse(SCREEN, self.color, self.rect)
        
    def draw_rectangle(self): # 사각형으로 그리기
        pygame.draw.rect(SCREEN, self.color, self.rect)

# 레벨에 맞게 설정
def setup(stage):
    global time_limit, BALL

    time_limit = 60000 - (5000 * (stage - 1))
    BALL.speed += stage
    BALL = Block(GRAY, Rect(screen_width // 2, 680, 20, 20), BALL.speed)
    draw_blocks()

# 시작 화면 보여주기
def display_start_screen():
    msg_stage = big_font.render(f"stage : {curr_stage}", True, BLACK)
    msg_start = big_font.render("Press Enter or Space to Start", True, BLACK)

    SCREEN.blit(msg_stage, (80, 280))
    SCREEN.blit(msg_start, (80, 380))

# blocks 생성
def draw_blocks():
    colors = [RED, ORANGE, YELLOW, GREEN, BLUE, NAVY, PURPLE]
    for y, color in enumerate(colors, start = 0):
        for x in range(0, 9):
            BLOCKS.append(Block(color, Rect(x * 80 + 150, y * 40 + 40, 60, 20)))

# 오브젝트 그리기
def draw_objects():
    global BALL, PADDLE, BLOCKS

    BALL.draw_circle()
    PADDLE.draw_rectangle()

    for block in BLOCKS:
        block.draw_rectangle()

# 게임 화면 보여주기
def display_game_screen():
    global start_tick, elapsed_time, time_limit, BLOCKS

    elapsed_time = int((time_limit - (pygame.time.get_ticks() - start_tick)) / 1000)
    msg_score = small_font.render(f"SCORE : {score}", True, BLACK)
    msg_time = small_font.render(f"Time: {elapsed_time}", True, BLACK)
    msg_heart = small_font.render(f"HEART : {heart}", True, BLACK)
    msg_stage = small_font.render(f"STAGE : {curr_stage}", True, BLACK)
    msg_restart = small_font.render(f"Press R to Restart", True, BLACK)

    SCREEN.blit(msg_score, (50, 10))
    SCREEN.blit(msg_time, (350, 10))
    SCREEN.blit(msg_heart, (650, 10))
    SCREEN.blit(msg_stage, (50, 750))
    SCREEN.blit(msg_restart, (600, 750))

    draw_objects()

    check_movement()
    check_game_over()

# 충돌 확인
# 수정 필요
def check_movement():
    global game_start, score, heart, curr_stage, BLOCKS, BALL, PADDLE

    remain_blocks = len(BLOCKS)
    BLOCKS = [x for x in BLOCKS if not x.rect.colliderect(BALL.rect)]

    # 블록과 공이 부딪혔을 때
    if len(BLOCKS) != remain_blocks: 
        score += 10 * curr_stage
        BALL.dir *= -1

    # 공의 위치가 게임창 안에 있을 때
    if BALL.rect.centery < 1000:
        BALL.move()

    #패들과 공이 부딪혔을 때
    if PADDLE.rect.colliderect(BALL.rect):  # colliderect은 볼과 패들의 충돌 여부를 검사합니다.
        BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 100

    #패들이 좌우벽과 맞닿을 때
    if PADDLE.rect.centerx < 55 :
        PADDLE.rect.centerx = 55
    if PADDLE.rect.centerx > 945:
        PADDLE.rect.centerx = 945

    # 공이 side 벽에 닿을 때
    if BALL.rect.centerx < 0 or BALL.rect.centerx > 1000:
        BALL.dir = 180 - BALL.dir  # 반사각만큼 방향 변화
    elif BALL.rect.centery < 0: # 위쪽 벽에 닿을 때
        BALL.dir = -BALL.dir
    
    # 벽돌이 다 지워졌을 때
    if remain_blocks == 0:
        game_start = False
        curr_stage += 1
        setup(curr_stage)

    # 공이 패들 밑으로 내려갔을 경우
    if BALL.rect.centery > 770 and len(BLOCKS) > 0:
        heart -= 1
        BALL = Block(GRAY, Rect(PADDLE.rect.centerx, PADDLE.rect.centery - 30, 20, 20), BALL.speed)

# 패들 이동, 돌리기
# 수정 필요
def turn_paddle(key):
    turn_keys = [K_w, K_a, K_s, K_d]
    for turn_key in turn_keys:
        pass

# 게임 오버 이벤트
# 수정 필요
def check_game_over():
    global heart, elapsed_time

    if heart == 0 or (len(BLOCKS) > 0 and elapsed_time == 0):
        game_over()

# 오브젝트 초기화
def object_initialize():
    global game_start, score, heart, curr_stage, BLOCKS, BALL, PADDLE

    game_start = False

    score = 0
    heart = 3
    curr_stage = 1

    BLOCKS = []
    BALL = Block(GRAY, Rect(screen_width // 2, 680, 20, 20), 15)
    PADDLE = Block(GRAY, Rect(screen_width // 2, 700, 100, 30))

    draw_blocks()

# 게임 종료 처리
def game_over():
    global running
    
    running = False

    msg_failed = big_font.render("FAILED", True, WHITE)
    msg_score = big_font.render(f"Score : {score}", True, WHITE)

    SCREEN.fill(BLACK)
    SCREEN.blit(msg_failed, (380, 400))
    SCREEN.blit(msg_score, (380, 500))

# 초기화
pygame.init()
screen_width = 1000 # 가로 크기
screen_height = 800 # 세로 크기
SCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Block Breaker')
pygame.key.set_repeat(10, 10) # (지연 시간, 간격)
TIMETICK = pygame.time.Clock()

# font
big_font = pygame.font.SysFont(None, 80)
small_font = pygame.font.SysFont(None, 50)

# colors (rgb)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
NAVY = (0, 0, 153)
PURPLE = (201, 0, 167)
GRAY = (160, 160, 160)
BLACK = (0, 0, 0)

# 관리해야 하는 친구들
curr_stage = 1 # 현재 스테이지
score = 0 # 현재 점수
heart = 3 # 현재 목숨
time_limit = None # 화면에 표시할 시간
start_tick = None # 시작 시간 저장
elapsed_time = None # 남은 시간

# objects
BLOCKS = []
BALL = Block(GRAY, Rect(screen_width // 2, 680, 20, 20), 15)
PADDLE = Block(GRAY, Rect(screen_width // 2, 700, 100, 30))

# 게임 시작 여부
game_start = False

running = True # 게임이 실행중인가?
def main():
    global running, game_start, score, heart, curr_stage, start_tick, BALL, BLOCKS, PADDLE

    setup(curr_stage)

    while running:        
        # 이벤트 루프
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key in [K_RETURN, K_KP_ENTER, K_SPACE]:
                    game_start = True
                    start_tick = pygame.time.get_ticks()
                    print(start_tick)
                elif event.key == K_r: # 재시작
                    object_initialize()
                elif event.key == K_ESCAPE: # 종료
                    running = False
                    pygame.quit()
                    sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    PADDLE.rect.centerx -= 10
                elif event.key == K_RIGHT:
                    PADDLE.rect.centerx += 10
                elif event.key in [K_w, K_a, K_s, K_d]:
                    turn_paddle(event.key)
                    pass
        
        # 화면 전체를 하얗게 칠함
        SCREEN.fill(WHITE)

        if not game_start:
            display_start_screen() # 시작 화면 표시
        else:
            display_game_screen() # 게임 화면 표시

        # 화면 업데이트
        pygame.display.update()
        TIMETICK.tick(30)
    
    # 유다희씨 5초 동안 보여줌
    pygame.time.delay(5000)

    # 게임 종료
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
