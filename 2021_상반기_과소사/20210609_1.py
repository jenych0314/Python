from typing import Sized


class Ball:
    # color
    # size
    direction = "default"

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

ball = Ball()
ball.direction = "down"
ball.bounce()
ball.size = 10
ball.__class__.direction = "stop"