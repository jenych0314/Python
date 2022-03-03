import pygame

class Font:
    def __init__(self, type, size):
        self.type = type
        self.size = size
    
    def set_font(self):
        return pygame.font.SysFont(self.type, self.size)

class Message:
    def __init__(self, color, font, string):
        self.color = color
        self.font = font
        self.message = string
        self.smooth = True

    def set_msg(self, screen, rect):
        msg = self.font.render(self.message, self.smooth, self.color)
        screen.blit(msg, rect)

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

# pygame.font.get_fonts() 순서
korean_font = {
    25: 'malgungothicsemilight',
    82: 'batang',
    83: 'batangche',
    84: 'gungsuh',
    85: 'gungsuhche',
    86: 'gulim',
    87: 'gulimche',
    88: 'dotum',
    89: 'dotumche',
    151: 'hy그래픽m',
    152: 'hy궁서b',
    153: 'hy견고딕',
    154: 'hy중고딕',
    155: 'hy헤드라인m',
    156: 'hy견명조',
    157: 'hy신명조',
    158: 'hy목각파임b',
    159: 'hy엽서l',
    160: 'hy엽서m',
    161: 'hy얕은샘물m',
    165: '휴먼옛체',
    166: '휴먼편지체',
    167: '휴먼아미체',
    168: '휴먼매직체',
    169: '휴먼둥근헤드라인',
    199: '새굴림',
    234: '휴먼모음t',
    235: '휴먼엑스포',
    236: 'hcrdotum',
    238: 'hcrbatang',
    245: 'hancomgothicregular'
}

big_font = Font(korean_font[168], 60)
small_font = Font(korean_font[168], 25)

# screen 크기
screen_width = 1000 # 가로 크기
screen_height = 800 # 세로 크기