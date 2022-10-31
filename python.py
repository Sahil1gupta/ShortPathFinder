import curses
from curses import wrapper
from operator import ne 
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

def print_maze(maze,stdscr,path=[]):
    BLUE=curses.color_pair(1)
    RED=curses.color_pair(2)

    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if(i,j) in path:
               stdscr.addstr(i,j*2,"X",RED)
            else:
               stdscr.addstr(i,j*2,value,BLUE)

def find_start(maze,start): #here we are finding start position 
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if value== start:
                return i,j
    return None

def find_path(maze,stdscr):
    start="O"
    end="X"
    start_pos=find_start(maze,start)  #here we will get or know the starting position now we will find neighbours

    q=queue.Queue()  #it is a first come ,first out data structure means, the element first    come in will be the first element to comes out 
    #we want to process the node that's been in queue  the longest
    q.put((start_pos,[start_pos])) # in tuple we are passing two elemennts in the queue bcoz in the queue i want to keep track of the node that i want to process next as well as the path to get to that node

    visited=set()  # this will contain all the position that we ahve visited 

    while not q.empty():
        current_pos,path=q.get()  #q.get() will going to give me most recent elemnt from the queue and it's path 
        row,col=current_pos # now we are breaking down the current postion into two components row and coloumn , and now i'm going to find all of the neighbours of this position and start processing them if they are not the end node

        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col]==end:  #if this position equal to an X(end) ,if it is means we have found the current path and return them
            return path
        
        #now if we haven't fiund the end node we need to continue branching out wo we need to find out all neighbours of the current node and expand towards them.

            #after defiing def find_neighbors(maze,row,col) function
        neighbors=find_neighbors(maze,row,col)  #here we are passing the row and column of the current postion that we are processing (findind all of their neighors)
        for neighbor in neighbors: #here we are going to check obstacles 
            if neighbor in visited: #if it is alrrady visited we don't need to check it
                continue

            r,c=neighbor
            if maze[r][c]=="#":
                continue

            new_path=path+[neighbor] #new_path is whatever the current path is plus current neighbor that i'm considering 
            q.put((neighbor,new_path))
            visited.add(neighbor)#we put this into visited so that we can't process it again




def find_neighbors(maze,row,col):  #here we need to make sure that the neighbor that we're finding is no an obstacle and that it is a valid position in the case
     neighbors=[]  #now we are going to determine neighbor of this (row,col) ureent position-->left,right,down

     if row >0: #UP
        neighbors.append((row-1,col))
     if row+1<len(maze):#DOWN
        neighbors.append((row+1,col))
     if col>0:#left
        neighbors.append((row,col-1))
     if col+1<len(maze[0]):#RIGHT
         neighbors.append((row,col+1))
     return neighbors



def main(stdscr):
    # curses.init_pair(id,foreground_color,background_color)
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    find_path(maze,stdscr)
    # stdscr.clear()
    # print_maze(maze,stdscr)
    # stdscr.refresh()
    stdscr.getch()
wrapper(main)