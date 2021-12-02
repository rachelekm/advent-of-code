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
        depth = [x for x, y in zip(lines, lines[1:] + [0]) if int(x) < int(y)]
        print('part 1: {}'.format(len(depth)))
        # part 2
        depth_window = [one for one, two, three, four in zip(lines, lines[1:], lines[2:], lines[3:]) if int(one)+int(two)+int(three) < int(two)+int(three)+int(four)]
        print('part 2: {}'.format(len(depth_window)))
