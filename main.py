
import random
import time
import curses
from curses import wrapper

def main(stdscr):
  curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_YELLOW)
  curses.init_pair(2,curses.COLOR_CYAN,curses.COLOR_MAGENTA)
  curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_RED)

  color1 = curses.color_pair(1)
  color2 = curses.color_pair(2)
  color3 = curses.color_pair(3)

  list_of_colors = [color1,color2,color3]

  stdscr.clear()
  height,width = stdscr.getmaxyx()
  stdscr.addstr(0,0,f"Terminal size: {height} rows,{width}cols")
  stdscr.addstr(5,5,"Hello world",color1)
  stdscr.addstr(10,10,"good night",color2| curses.A_BOLD)
  stdscr.addstr(3,20,"good night",color3)
  stdscr.refresh()
  stdscr.getch()

 
  for i in range(100):
    x = random.randint(0,height-1)
    y = random.randint(0,width-len("Catch me here"))
    c = random.choice(list_of_colors)
    stdscr.clear()
    stdscr.addstr(x,y,"Catch me here",c)
    stdscr.refresh()
    time.sleep(1)


wrapper(main)