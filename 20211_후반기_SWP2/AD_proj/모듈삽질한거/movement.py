from status import *
from block import *
from main import *

def check_movement(game_start, score, heart, curr_stage, BLOCKS, BALL, PADDLE):
    # global game_start, score, heart, curr_stage, BLOCKS, BALL, PADDLE

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
        BALL = Block(BALL.color, Rect(PADDLE.rect.centerx, PADDLE.rect.centery - 30, 20, 20), BALL.speed)