"""
--- Day 1: Sonar Sweep ---
"""
import os
CWD = os.getcwd()
INPUT = 'https://adventofcode.com/2021/day/1/input'

if __name__ == "__main__":
    with open("{}/2021/inputs/day-1.txt".format(CWD), "r") as file:
        # part 1
        lines = file.readlines()
        depth = ['increased' if float(x) < float(y) else 'decreased' for x, y in zip(lines, lines[1:] + [0])]
        depth.sort(reverse=True)
        print('part 1: {}'.format(depth.index('decreased')))
        # part 2
        depth_window = ['increased' if float(one)+float(two)+float(three) < float(two)+float(three)+float(four) else 'decreased' for one, two, three, four in zip(lines, lines[1:], lines[2:], lines[3:])]
        depth_window.sort(reverse=True)
        print('part 2: {}'.format(depth_window.index('decreased')))
