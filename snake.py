import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

def main(scr):
    curses.noecho()             # Disable default printing of inputs
    curses.curs_set(0)          # Hiding cursor visibility (https://docs.python.org/2/library/curses.html#curses.curs_set)

    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)  # Init window object
    win.keypad(1)               # enable processing of functional keys by curses (ex. arrow keys)
    win.border(0)               # set a border for the window
    win.nodelay(1)

    key = KEY_RIGHT
    snake = [[4,10]]
    title = ' Hello snake! '
    win.addstr(0, (curses.COLS - len(title)) // 2, title)

    while key != 27:
        win.timeout(100)        # wait 0.1 sec

        event = win.getch()     # get the code of pressed key (if nothing pressed, this returns -1)
        if event in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
            key = event

        # Snake logic ;)

        win.addch(last[0], last[1], ' ')

        win.addch(snake[0][0], snake[0][1], 'x')
        win.refresh()

    game_over = 'Game Over!'
    win.addstr(curses.LINES // 2, (curses.COLS - len(game_over)) // 2, game_over)
    win.refresh()

    time.sleep(3)

curses.wrapper(main)
