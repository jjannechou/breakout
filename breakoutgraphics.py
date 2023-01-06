"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)

BALL_RADIUS = 10       # Radius of the ball (in pixels)

PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,
                             x=(self.window.width-paddle_width)/2, y=self.window.height-paddle_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2,
                           x=(self.window.width-ball_radius*2)/2, y=(self.window.height-ball_radius*2)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        self.br = ball_radius
        self.num_brick = 0
        self.click = False

        # Default initial velocity for the ball
        self.ball__dy = INITIAL_Y_SPEED
        self.ball__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.ball__dx = - self.ball__dx

        # Initialize our mouse listeners
        onmouseclicked(self.move_ball)
        onmousemoved(self.move_paddle)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                if i == 0 or i == 1:
                    brick.fill_color = 'red'
                if i == 2 or i == 3:
                    brick.fill_color = 'orange'
                if i == 4 or i == 5:
                    brick.fill_color = 'yellow'
                if i == 6 or i == 7:
                    brick.fill_color = 'green'
                if i == 8 or i == 9:
                    brick.fill_color = 'blue'
                self.window.add(brick, x=j*(brick_width+brick_spacing), y=brick_offset+i*(brick_height+brick_spacing))
                self.num_brick += 1

    def move_paddle(self, mouse):
        if mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def move_ball(self):
        self.click = True

    def get_dy(self):
        return self.ball__dy

    def get_dx(self):
        return self.ball__dx

    def set_dy(self):
        self.ball__dy = - self.ball__dy

    def set_dx(self):
        self.ball__dx = - self.ball__dx

    def collisions(self):
        for i in range(2):
            for j in range(2):
                obj = self.window.get_object_at(self.ball.x+i*2*self.br, self.ball.y+j*2*self.br)
                if obj is not None:
                    if obj is self.paddle:
                        if self.ball__dy > 0:
                            self.set_dy()
                    else:
                        self.set_dy()
                        self.window.remove(obj)
                        self.num_brick -= 1
                    return

    def reset(self):
        self.window.add(self.ball, x=(self.window.width-self.br)/2, y=(self.window.height-self.br)/2)
        self.click = False
        self.ball__dy = INITIAL_Y_SPEED
        self.ball__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.ball__dx = - self.ball__dx


