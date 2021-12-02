"""
--- Day 1: Sonar Sweep ---
"""
import os
CWD = os.getcwd()
INPUT = 'https://adventofcode.com/2021/day/1/input'

if __name__ == "__main__":
    with open("{}/2021/inputs/day-1.txt".format(CWD), "r") as file:
        lines = file.readlines()
        depth = ['increased' if float(x) < float(y) else 'decreased' for x, y in zip(lines, lines[1:] + [0])]
        depth.sort(reverse=True)
        print(depth.index('decreased'))

