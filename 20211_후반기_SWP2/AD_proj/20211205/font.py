import pygame

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

class Font:
    def __init__(self, type, size):
        self.type = type
        self.size = size
    
    def set_font(self):
        return pygame.font.SysFont(self.type, self.size)

giant_font = Font(korean_font[168], 90)
big_font = Font(korean_font[168], 60)
small_font = Font(korean_font[168], 25)
tiny_font = Font(korean_font[168], 12)

font_lst = [giant_font, big_font, small_font, tiny_font]