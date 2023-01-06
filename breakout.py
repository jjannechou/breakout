"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.click:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.collisions()
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                graphics.set_dx()
            if graphics.ball.y <= 0:
                graphics.set_dy()
            if graphics.ball.y + graphics.ball.height > graphics.window.height:
                lives -= 1
                graphics.reset()
            if lives == 0 or graphics.num_brick == 0:
                graphics.reset()
                break



if __name__ == '__main__':
    main()
