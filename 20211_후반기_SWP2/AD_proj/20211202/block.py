import pygame
import math
import random

class Block:
    def __init__(self, color, rect, speed = 0):
        self.color = color
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270

    def move(self): # radians를 사용해서 방향(dir)을 라디안으로 변환, X축과 Y축의 방향 성분 구분
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw_circle(self, screen): # 원으로 그리기
        pygame.draw.ellipse(screen, self.color, self.rect)
        
    def draw_rectangle(self, screen): # 사각형으로 그리기
        pygame.draw.rect(screen, self.color, self.rect)

if __name__ == "__main__":
    WHITE = (0, 0, 0)
    ball = Block(WHITE, pygame.Rect(1, 1, 1, 1), 15)
    print(ball.speed)