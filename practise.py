import curses
from curses import wrapper 
import queue
import time



maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def main(stdscr):
    # curses.init_pair(id,foreground_color,background_color)
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_RED)
    blue_and_balck=curses.color_pair(1)
    stdscr.clear()
    stdscr.addstr(5,5,"hello world!",blue_and_balck)
    stdscr.getch()
wrapper(main)