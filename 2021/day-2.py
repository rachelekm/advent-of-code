"""
--- Day 2: Dive! ---
"""
import os
CWD = os.getcwd()
INPUT = 'https://adventofcode.com/2021/day/2/input'

def cleanLine(line):
    num = line.split(' ')[1]
    return float(num)

if __name__ == "__main__":
    with open("{}/2021/inputs/day-2.txt".format(CWD), "r") as file:
        # part 1
        lines = file.readlines()
        course_part_1 = {'horizontal': 0, 'depth': 0}
        course_part_2 = {'horizontal': 0, 'depth': 0, 'aim': 0}
        # part 1
        for x in lines:
            if 'forward' in x:
                course_part_1['horizontal'] += cleanLine(x)
            if 'down' in x:
                course_part_1['depth'] += cleanLine(x)
            if 'up' in x:
                course_part_1['depth'] -= cleanLine(x)
        print('part 1: {}'.format(course_part_1['horizontal']*course_part_1['depth']))
        # part 2
        for x in lines:
            if 'forward' in x:
                course_part_2['horizontal'] += cleanLine(x)
                if course_part_2['aim'] != 0:
                    course_part_2['depth'] += (cleanLine(x)*course_part_2['aim'])
            if 'down' in x:
                course_part_2['aim'] += cleanLine(x)
            if 'up' in x:
                course_part_2['aim'] -= cleanLine(x)
        print('part 1: {}'.format(course_part_2['horizontal']*course_part_2['depth']))
