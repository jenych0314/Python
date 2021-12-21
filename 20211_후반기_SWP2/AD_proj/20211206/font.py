import pygame

class Font:
    def __init__(self, size):
        self.type = 'CookieRun Regular.ttf'
        self.size = size
    
    def set_font(self):
        return pygame.font.Font(self.type, self.size)

giant_font = Font(90)
big_font = Font(60)
small_font = Font(25)
tiny_font = Font(12)

font_lst = [giant_font, big_font, small_font, tiny_font]

if __name__ == '__main__':
    print()