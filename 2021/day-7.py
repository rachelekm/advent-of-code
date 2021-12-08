"""
--- Day 7: The Treachery of Whales ---
"""
import os
import numpy as np
CWD = os.getcwd()
INPUT = 'https://adventofcode.com/2021/day/7/input'

def applyRate(row):
    rate = 1
    for i, step in enumerate(row):
        if step == 0:
            pass
        else:
            row[i] = step*rate
            rate += 0.5
    return row

def getCheapestFuel(constant):
    initial = np.loadtxt("{}/2021/inputs/day-7.txt".format(CWD), dtype='int', delimiter=',')
    max = initial.max()
    min = initial.min()
    plane = np.zeros((initial.size, max))
    for i, crab in enumerate(initial):
        if crab == max:
            row = np.arange(min, (max), dtype='int')
            if not constant:
                row = applyRate(row)
            row = row[::-1]
        if crab == min:
            row = np.arange(min+1, max+1, dtype='int')
            if not constant:
                row = applyRate(row)
        else:
            pos = np.arange(min, crab, dtype='int')
            neg = np.arange(crab-(pos.size)+1, max, dtype='int')
            if not constant:
                pos = applyRate(pos)
                neg = applyRate(neg)
            pos = pos[::-1]
            row = np.concatenate((pos, neg), axis=None)[:max]
        plane[i] = row
    return np.sum(plane, axis=0).min()

if __name__ == "__main__":
    print('part 1: {}'.format(getCheapestFuel(1)))
    print('part 2: {}'.format(getCheapestFuel(0)))
