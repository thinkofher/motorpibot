import curses


def curNewScreen():
    screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    return screen


def msgClicked(screen, button):
    if len(button) == 0:
        msgString = "CANT RECOGNIZE!\n"
    else:
        msgString = 'Clicked: {}!\n'.format(
            button
        )
    try:
        screen.addstr(msgString,
                      curses.A_REVERSE)
        screen.refresh()
    except curses.error:
        screen.clear()


def curEndSession(screen):
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
