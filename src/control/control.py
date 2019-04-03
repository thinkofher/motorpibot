import curses
from .curses import msgClicked, curEndSession


class ScreenController:

    _default_distance = 0.030

    def __init__(self, screen, driver):
        self.screen = screen
        self.driver = driver
        self._distance = self._default_distance

    def set_distance(self, distance):
        self._distance = distance

    def run(self):
        try:
            while True:
                char = self.screen.getch()
                if char == ord('q'):
                    break
                elif char == curses.KEY_UP:
                    msgClicked(self.screen, 'UP')
                    self.driver.forward(self._distance)
                elif char == curses.KEY_DOWN:
                    msgClicked(self.screen, 'DOWN')
                    self.driver.backward(self._distance)
                elif char == curses.KEY_LEFT:
                    msgClicked(self.screen, 'LEFT')
                    self.driver.turnLeftForward(self._distance)
                elif char == curses.KEY_RIGHT:
                    msgClicked(self.screen, 'RIGHT')
                    self.driver.turnRightForward(self._distance)
                else:
                    msgClicked(self.screen, "")
        finally:
            self.driver.endSession()
            curEndSession(self.screen)
