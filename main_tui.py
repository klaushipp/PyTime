# encoding: utf-8

import curses
import time

def print_banner(window):
    pytime_ascii_str = (" ___     _____ _           \n"
                        "| _ \_  |_   _(_)_ __  ___ \n"
                        "|  _/ || || | | | '  \/ -_)\n"
                        "|_|  \_, ||_| |_|_|_|_\___|\n"
                        "     |__/                  \n"
                        )

    window.addstr(pytime_ascii_str)

    return window

def init_screen():
    main_screen = curses.initscr()
    height, width = main_screen.getmaxyx()
    
    banner_window = curses.newwin(6, width, 0, 0)
    banner_window = print_banner(banner_window)
    banner_window.refresh()

    main_screen.clear()
    main_screen.refresh()

def main():
    init_screen()

    curses.napms(2000)

if __name__ == "__main__":
    main()

# curses.napms(2000)
curses.endwin()