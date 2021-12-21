import pygame
import sys
from pygame.constants import KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_KP_ENTER, K_RETURN, K_SPACE, MOUSEBUTTONUP, K_a, K_d, K_r, K_ESCAPE, K_s, K_w
from pygame.locals import QUIT, Rect
from block import *
from message import Message
from colors import *
from objects import *
from font import *
from recordBook import *

# 게임 모드 설정 화면 보여주기
def display_primitive_screen():
    msg_title = Message(BLACK, giant_font, "Block Breaker")
    msg_title.set_msg(SCREEN, (200, 170))

    msg_team = Message(BLACK, small_font, "이하람, 장민우, 전예찬")
    msg_team.set_msg(SCREEN, (30, screen_height - 50))

    msg_classic = Message(BLACK, big_font, "Classic Mode")
    msg_timer = Message(BLACK, big_font, "Timer Mode")
    msg_arcade = Message(BLACK, big_font, "Arcade Mode")

    msg_classic.set_msg(SCREEN, (470, 450))
    msg_timer.set_msg(SCREEN, (475, 550))
    msg_arcade.set_msg(SCREEN, (465, 650))

    draw_buttons()

# 스테이지 넘어갈 때 화면 보여주기
def display_start_screen():
    msg_stage = Message(BLACK, big_font, f"stage : {curr_stage}")
    msg_start = Message(BLACK, big_font, "Press Enter or Space to Start")

    msg_stage.set_msg(SCREEN, (80, 280))
    msg_start.set_msg(SCREEN, (80, 380))

# 게임 화면 보여주기
def display_game_screen():
    global start_tick, elapsed_time, time_limit, BLOCKS

    if game_timer and not game_end:
        elapsed_time = int((time_limit - (pygame.time.get_ticks() - start_tick)) / 1000)
        msg_time = Message(BLACK, small_font, f"Time: {elapsed_time}")
        msg_time.set_msg(SCREEN, (350, 10))

    msg_score = Message(BLACK, small_font, f"SCORE : {score}")
    msg_heart = Message(BLACK, small_font, f"HEART : {heart}")
    msg_stage = Message(BLACK, small_font, f"STAGE : {curr_stage}")
    msg_restart = Message(BLACK, small_font, f"Press R to Restart")

    msg_score.set_msg(SCREEN, (50, 10))
    msg_heart.set_msg(SCREEN, (650, 10))
    msg_stage.set_msg(SCREEN, (50, 750))
    msg_restart.set_msg(SCREEN, (600, 750))

    draw_objects()

    check_movement()
    check_game_over()

# 게임 종료 화면 보여주기
def display_game_over_screen():
    global recordBook, score

    recordBook.doRecord(score)

    SCREEN.fill(BLACK)

    msg_failed = Message(WHITE, big_font, "FAILED")
    msg_rcrecord = Message(WHITE, big_font, f"Current record : {recordBook.record_dic['recent_record']}")
    msg_bstrecord = Message(WHITE, big_font, f"Best record : {recordBook.record_dic['best_record']}")
    msg_restart = Message(WHITE, big_font, "Do you wanna play again?")
    msg_yes = Message(WHITE, big_font, "Yes")
    msg_no = Message(WHITE, big_font, "No")

    msg_failed.set_msg(SCREEN, (80, 100))
    msg_rcrecord.set_msg(SCREEN, (80, 240))
    msg_bstrecord.set_msg(SCREEN, (80, 300))
    msg_restart.set_msg(SCREEN, (80, 500))
    msg_yes.set_msg(SCREEN, (100, 580))
    msg_no.set_msg(SCREEN, (540, 580))

    draw_buttons()

# 버튼 그리기
def draw_buttons():
    global classic_button, timer_button, arcade_button, yes_button, no_button

    if not game_end:
        classic_button = Block(YELLOW, Rect(400, 460, 500, 70))
        timer_button = Block(ORANGE, Rect(400, 560, 500, 70))
        arcade_button = Block(RED, Rect(400, 660, 500, 70))

        classic_button.draw_rectangle(SCREEN, 3)
        timer_button.draw_rectangle(SCREEN, 3)
        arcade_button.draw_rectangle(SCREEN, 3)
    else:
        yes_button = Block(WHITE, Rect(80, 585, 150, 70))
        no_button = Block(WHITE, Rect(500, 585, 150, 70))

        yes_button.draw_rectangle(SCREEN, 3)
        no_button.draw_rectangle(SCREEN, 3)

# blocks 생성
def draw_blocks():
    colors = [RED, ORANGE, YELLOW, GREEN, BLUE, NAVY, PURPLE]

    if not game_arcade:
        for y, color in enumerate(colors, start = 0):
            for x in range(0, 9):
                BLOCKS.append(Block(color, Rect(x * 80 + 150, y * 40 + 40, 60, 20)))
    else:
        for y, color in enumerate(colors, start = 0):
            for x in range(0, 9):
                BLOCKS.append(Block(color, Rect(x * 80 + 150, y * 40 + 200, 60, 20)))

# 오브젝트 그리기
def draw_objects():
    global SCREEN, BALL, PADDLE, BLOCKS

    BALL.draw_circle(SCREEN)
    PADDLE.draw_rectangle(SCREEN)

    for block in BLOCKS:
        block.draw_rectangle(SCREEN)

# pos에 해당하는 버튼 확인 -> 게임 모드 설정
def check_buttons(pos):
    global game_set_mode, game_classic, game_timer, game_arcade, running

    if not game_end:
        if classic_button.rect.collidepoint(pos) or timer_button.rect.collidepoint(pos) or arcade_button.rect.collidepoint(pos):
            game_set_mode = False

        if classic_button.rect.collidepoint(pos): # classic
            game_classic = True
            game_timer = False
            game_arcade = False
        elif timer_button.rect.collidepoint(pos): # timer
            game_classic = False
            game_timer = True
            game_arcade = False
        elif arcade_button.rect.collidepoint(pos): # arcade
            game_classic = False
            game_timer = False
            game_arcade = True
    else:
        if yes_button.rect.collidepoint(pos):
            object_initialize()
            pygame.display.update()
        elif no_button.rect.collidepoint(pos):
            running = False

# 충돌 확인
def check_movement():
    global game_start, game_end, score, heart, curr_stage, BLOCKS, BALL, PADDLE

    remain_blocks = len(BLOCKS)
    BLOCKS = [x for x in BLOCKS if not x.rect.colliderect(BALL.rect)]

    # 블록과 공이 부딪혔을 때
    if len(BLOCKS) != remain_blocks: 
        score += 10 * curr_stage
        BALL.dir *= -1

    # 공의 위치가 게임창 안에 있을 때
    if not game_end:
        if BALL.rect.centery < 1000:
            BALL.move()

    # 패들과 공이 부딪혔을 때
    if not game_arcade:
        if PADDLE.rect.colliderect(BALL.rect):  # colliderect은 볼과 패들의 충돌 여부를 검사합니다.
            BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 100
    else:
        if PADDLE.rect.colliderect(BALL.rect):  # colliderect은 볼과 패들의 충돌 여부를 검사합니다.
            if BALL.rect.centery > screen_height//2:
                BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 100
            else:
                BALL.dir = (90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 100) * -1

    # 패들이 좌우벽과 맞닿을 때, 좌우 벽에 박히지 않도록
    if PADDLE.rect.centerx < 55 :
        PADDLE.rect.centerx = 55
    if PADDLE.rect.centerx > 945:
        PADDLE.rect.centerx = 945

    if BALL.rect.centerx < 0 or BALL.rect.centerx > 1000: # 공이 side 벽에 닿을 때
        BALL.dir = 180 - BALL.dir  # 반사각만큼 방향 변화
    elif not game_arcade and BALL.rect.centery < 0: # 공이 위쪽 벽에 닿을 때
        BALL.dir = -BALL.dir
    
    # 벽돌이 다 지워졌을 때
    if remain_blocks == 0:
        game_start = False
        curr_stage += 1
        setup(curr_stage)

    # 공이 패들 밑으로/위로 넘어갔을 경우
    if not game_arcade:
        if BALL.rect.centery > 770 and len(BLOCKS) > 0:
            heart -= 1
            BALL.rect.center = (PADDLE.rect.centerx, PADDLE.rect.centery - 30)
    else: # 아케이드 모드에서
        if PADDLE.rect.centery > screen_height//2: # 패들이 밑쪽에 있을 때
            if (BALL.rect.centery > 770 and len(BLOCKS) > 0) or (BALL.rect.centery < 20 and len(BLOCKS) > 0):
                heart -= 1
                BALL.rect.center = (PADDLE.rect.centerx, PADDLE.rect.centery - 30)
        else: # 패들이 위쪽에 있을 때
            if (BALL.rect.centery > 770 and len(BLOCKS) > 0) or (BALL.rect.centery < 20 and len(BLOCKS) > 0):
                heart -= 1
                BALL.rect.center = (PADDLE.rect.centerx, PADDLE.rect.centery + 30)

# 게임 오버 이벤트
def check_game_over():
    global heart, elapsed_time

    if game_timer:
        if (heart == 0 and len(BLOCKS) > 0) or elapsed_time == 0:
            game_over()
    else:
        if heart == 0 and len(BLOCKS) > 0:
            game_over()

# 오브젝트 초기화
def object_initialize():
    global game_start, game_set_mode, game_end, score, heart, curr_stage, time_limit, start_tick, elapsed_time, recordBook, BLOCKS, BALL, PADDLE

    game_start = False
    game_set_mode = True
    game_end = False

    curr_stage = 1 # 현재 스테이지
    score = 0 # 현재 점수
    heart = 3 # 현재 목숨
    start_tick = 0 # 시작 시간 저장
    elapsed_time = 0 # 남은 시간

    recordBook = RecordBook() # 점수 DB

    BLOCKS = []
    BALL = Block(DAY_GLO, Rect(screen_width // 2, 680, 20, 20), 15)
    PADDLE = Block(GRAY, Rect(screen_width // 2, 700, 100, 30))

# 레벨에 맞게 설정
def setup(stage):
    global time_limit, BALL

    if game_timer:
        time_limit = 60000 - (5000 * (stage - 1))

    BALL.speed += (stage - 1)
    BALL = Block(BALL.color, Rect(screen_width // 2, 680, 20, 20), BALL.speed)
    
    draw_blocks()

# (arcade mode) 패들 이동
def turn_paddle(input_key):
    global PADDLE

    if game_arcade and game_start:
        if input_key in [K_w, K_a]:
            PADDLE.rect.center = (PADDLE.rect.centerx, 50)
        elif input_key in [K_s, K_d]:
            PADDLE.rect.center = (PADDLE.rect.centerx, 700)

# 게임 종료 처리
def game_over():
    global game_end

    game_end = True

    display_game_over_screen()

# 초기화
pygame.init()
SCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Breaker")
pygame.key.set_repeat(10, 10) # (지연 시간, 간격)
TIMETICK = pygame.time.Clock()

# font
giant_font = giant_font.set_font()
big_font = big_font.set_font()
small_font = small_font.set_font()
tiny_font = tiny_font.set_font()

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
                    if not game_end and game_start:
                        object_initialize()
                elif event.key == K_ESCAPE: # 종료
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.key in [K_w, K_a, K_s, K_d]:
                    print(event.key)
                    turn_paddle(event.key)

            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    PADDLE.rect.centerx -= 10
                elif event.key == K_RIGHT:
                    PADDLE.rect.centerx += 10

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
                setup(curr_stage)
        else:
            display_game_screen()

        # 화면 업데이트
        pygame.display.update()
        TIMETICK.tick(30)
    
    # 유다희씨 5초 동안 보여줌
    # pygame.time.delay(5000)

    # 게임 종료
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()