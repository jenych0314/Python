# status
from pygame.constants import NOEVENT


curr_stage = None # 현재 스테이지
score = None # 현재 점수
heart = None # 현재 목숨
time_limit = None # 화면에 표시할 시간
start_tick = None # 시작 시간 저장
elapsed_time = None # 남은 시간

# objects
BLOCKS = None
BALL = None
PADDLE = None

# buttons
classic_button = None
timer_button = None
arcade_button = None

# setting
game_start = None
game_set_mode = None
game_classic = None
game_timer = None
game_arcade = None

# screen 크기
screen_width = 1000 # 가로 크기
screen_height = 800 # 세로 크기