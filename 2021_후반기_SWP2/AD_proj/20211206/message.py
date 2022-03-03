class Message:
    def __init__(self, color, font, string):
        self.color = color
        self.font = font
        self.message = string
        self.smooth = True

    def set_msg(self, screen, rect):
        msg = self.font.render(self.message, self.smooth, self.color)
        screen.blit(msg, rect)