import pygame
import sys
from pygame.constants import KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_KP_ENTER, K_RETURN, K_SPACE, MOUSEBUTTONUP, K_a, K_d, K_r, K_ESCAPE, K_s, K_w
from pygame.locals import QUIT, Rect
from block import *
from message import Message
from colors import *
from objects import *
from font import *

# 레벨에 맞게 설정
def setup(stage):
    global time_limit, BALL

    time_limit = 60000 - (5000 * (stage - 1))
    BALL.speed += stage
    BALL = Block(GRAY, Rect(screen_width // 2, 680, 20, 20), BALL.speed)
    
    draw_blocks()

# 게임 모드 설정 화면 보여주기
def display_primitive_screen():
    msg_classic = Message(BLACK, big_font, "Classic Mode")
    msg_timer = Message(BLACK, big_font, "Timer Mode")
    msg_arcade = Message(BLACK, big_font, "Arcade Mode")

    msg_classic.set_msg(SCREEN, (80, 180))
    msg_timer.set_msg(SCREEN, (80, 280))
    msg_arcade.set_msg(SCREEN, (80, 380))

    draw_buttons()

# 버튼 그리기
def draw_buttons():
    classic_button.draw_rectangle(SCREEN, 3)
    timer_button.draw_rectangle(SCREEN, 3)
    arcade_button.draw_rectangle(SCREEN, 3)

# 게임 모드 설정
# 수정 필요
def set_game_mode(mode_num):
    if mode_num == 1: # classic
        pass
    elif mode_num == 2: # timer
        pass
    elif mode_num == 3: # arcade
        pass
    pass

# pos에 해당하는 버튼 확인
# 수정 필요
def check_buttons(pos):
    global game_set_mode

    if classic_button.rect.collidepoint(pos):
        game_set_mode = False
        set_game_mode(1)
        print(pos)
    elif timer_button.rect.collidepoint(pos):
        game_set_mode = False
        set_game_mode(2)
        print(pos)
    elif arcade_button.rect.collidepoint(pos):
        game_set_mode = False
        set_game_mode(3)
        print(pos)

# 시작 화면 보여주기
def display_start_screen():
    msg_stage = Message(BLACK, big_font, f"stage : {curr_stage}")
    msg_start = Message(BLACK, big_font, "Press Enter or Space to Start")

    msg_stage.set_msg(SCREEN, (80, 280))
    msg_start.set_msg(SCREEN, (80, 380))

# blocks 생성
def draw_blocks():
    colors = [RED, ORANGE, YELLOW, GREEN, BLUE, NAVY, PURPLE]
    for y, color in enumerate(colors, start = 0):
        for x in range(0, 9):
            BLOCKS.append(Block(color, Rect(x * 80 + 150, y * 40 + 40, 60, 20)))

# 오브젝트 그리기
def draw_objects():
    global SCREEN, BALL, PADDLE, BLOCKS

    BALL.draw_circle(SCREEN)
    PADDLE.draw_rectangle(SCREEN)

    for block in BLOCKS:
        block.draw_rectangle(SCREEN)

# 게임 화면 보여주기
def display_game_screen():
    global start_tick, elapsed_time, time_limit, BLOCKS

    elapsed_time = int((time_limit - (pygame.time.get_ticks() - start_tick)) / 1000)

    msg_score = Message(BLACK, small_font, f"SCORE : {score}")
    msg_time = Message(BLACK, small_font, f"Time: {elapsed_time}")
    msg_heart = Message(BLACK, small_font, f"HEART : {heart}")
    msg_stage = Message(BLACK, small_font, f"STAGE : {curr_stage}")
    msg_restart = Message(BLACK, small_font, f"Press R to Restart")

    msg_score.set_msg(SCREEN, (50, 10))
    msg_time.set_msg(SCREEN, (350, 10))
    msg_heart.set_msg(SCREEN, (650, 10))
    msg_stage.set_msg(SCREEN, (50, 750))
    msg_restart.set_msg(SCREEN, (600, 750))

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
        if turn_key == [K_w, K_a]:
        # w, a -> 위
            pass
        elif turn_key == [K_s, K_d]:
        # s, d -> 아래
            pass

# 게임 오버 이벤트
# 수정 필요
def check_game_over():
    global heart, elapsed_time

    if heart == 0 or (len(BLOCKS) > 0 and elapsed_time == 0):
        game_over()

# 오브젝트 초기화
def object_initialize():
    global game_start, game_set_mode, score, heart, curr_stage, time_limit, start_tick, elapsed_time, classic_button, timer_button, arcade_button, BLOCKS, BALL, PADDLE

    game_start = False
    game_set_mode = True

    curr_stage = 1 # 현재 스테이지
    score = 0 # 현재 점수
    heart = 3 # 현재 목숨
    time_limit = 60000 # 화면에 표시할 시간
    start_tick = 0 # 시작 시간 저장
    elapsed_time = 0 # 남은 시간

    BLOCKS = []
    BALL = Block(BLACK, Rect(screen_width // 2, 680, 20, 20), 15)
    PADDLE = Block(GRAY, Rect(screen_width // 2, 700, 100, 30))

    classic_button = Block(YELLOW, Rect(80, 180, 500, 50))
    timer_button = Block(ORANGE, Rect(80, 280, 500, 50))
    arcade_button = Block(RED, Rect(80, 380, 500, 50))

    draw_blocks()

# 게임 종료 처리
def game_over():
    global running
    
    running = False

    msg_failed = Message(WHITE, big_font, "FAILED")
    msg_score = Message(WHITE, big_font, f"Score : {score}")

    SCREEN.fill(BLACK)

    msg_failed.set_msg(SCREEN, (380, 400))
    msg_score.set_msg(SCREEN, (380, 500))

# 초기화
pygame.init()
SCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Breaker")
pygame.key.set_repeat(10, 10) # (지연 시간, 간격)
TIMETICK = pygame.time.Clock()

# font
big_font = big_font.set_font()
small_font = small_font.set_font()

running = True # 게임이 실행중인가?
def main():
    global running, game_start, score, heart, curr_stage, start_tick, BALL, BLOCKS, PADDLE

    object_initialize()

    while running:        
        # 이벤트 루프
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == KEYUP:
                if event.key in [K_RETURN, K_KP_ENTER, K_SPACE]:
                    if not game_set_mode:
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

            elif event.type == pygame.MOUSEBUTTONUP:
                click_pos = pygame.mouse.get_pos()
                check_buttons(click_pos)
        
        # 화면 전체를 하얗게 칠함
        SCREEN.fill(WHITE)

        if not game_start:
            if game_set_mode:
                display_primitive_screen()
            else:
                display_start_screen()
        else:
            display_game_screen()

        # 화면 업데이트
        pygame.display.update()
        TIMETICK.tick(30)
    
    # 유다희씨 5초 동안 보여줌
    pygame.time.delay(5000)

    # 게임 종료
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
