"""
--- Day 6: Lanternfish ---
"""
import os
import numpy as np
CWD = os.getcwd()
INPUT = 'https://adventofcode.com/2021/day/6/input'

def calcLanternfish(days):
    initial = np.loadtxt("{}/2021/inputs/day-6.txt".format(CWD), dtype='int', delimiter=',')
    timeline = np.zeros(9)
    for fish in initial:
        timeline[fish] += 1
    
    for _ in range(0, days):
        newborns = timeline[0]
        timeline[:-1] = timeline[1:]
        timeline[6] += newborns
        timeline[8] = newborns
    return sum(timeline)

if __name__ == "__main__":
    print('part 1: {}'.format(calcLanternfish(80)))
    print('part 2: {}'.format(calcLanternfish(256)))
