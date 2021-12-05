"""
--- Day 5: Hydrothermal Venture ---
"""
import os
CWD = os.getcwd()
INPUT = 'https://adventofcode.com/2021/day/5/input'

if __name__ == "__main__":
    with open("{}/2021/inputs/day-5.txt".format(CWD), "r") as file:
        lines = file.readlines()
        part2Input = []
        map = [[0]]

        def expand_map_y(y):
            for _ in range(y - (len(map)-1)):
                map.append([0 for _ in range(len(map[0]))])

        def expand_map_x(x):
            for _ in range(x - (len(map[0])-1)):
                    for row in map:
                        row.append(0)

        def plotPart1(y1, y2, x1, x2):
            if y1 != y2:
                plotColumn(y1, y2, x1)
            else:
                plotRow(y1, x1, x2)

        def plotPart2(y1, y2, x1, x2):
            y_movement = [(y1-diff) if y1 >= y2 else (y1+diff) for diff in range(0, abs(y1-y2)+1)]
            x_movement = [(x1-diff) if x1 >= x2 else (x1+diff) for diff in range(0, abs(x1-x2)+1)]
            diagonals = [(x, y) for x, y in zip(x_movement, y_movement)]
            for point in diagonals:
                map[point[1]][point[0]] += 1

        def plotColumn(y1, y2, x):
            map[y1][x] += 1
            map[y2][x] += 1
            if y1 != y2:
                for diff in range(1, abs(y1-y2)):
                    if y1 >= y2:
                        map[y1-diff][x] += 1
                    if y1 < y2:
                        map[y1+diff][x] += 1

        def plotRow(y, x1, x2):
            map[y][x1] += 1
            map[y][x2] += 1
            if x1 != x2:
                for diff in range(1, abs(x1-x2)):
                    if x1 >= x2:
                        map[y][x1-diff] += 1
                    if x1 < x2:
                        map[y][x1+diff] += 1

        lines[:] = [line.split(' -> ')for line in lines]
        for coords in lines:
            x1, x2 = int(coords[0].split(',')[0]), int(coords[1].split(',')[0])
            y1, y2 = int(coords[0].split(',')[1]), int(coords[1].split(',')[1])
            expand_y = y1 if y1 > y2 else y2
            expand_x = x1 if x1 > x2 else x2
            if len(map)-1 < expand_y:
                expand_map_y(expand_y)
            if len(map[0])-1 < expand_x:
                expand_map_x(expand_x)
            # part 1 no diagonal lines
            if x1 != x2 and y1 != y2:
                part2Input.append([[x1, y1], [x2, y2]])
            else:
                plotPart1(y1, y2, x1, x2)
        filter_map = [_ for _ in [ list(i for i in x if i>1) for x in map ] if len(_)>0]
        count = sum([len(_) for _ in filter_map])
        print('part 1: {}'.format(count))

        for coords in part2Input:
            x1, x2 = coords[0][0], coords[1][0]
            y1, y2 = coords[0][1], coords[1][1]
            expand_y = y1 if y1 > y2 else y2
            expand_x = x1 if x1 > x2 else x2
            if len(map)-1 < expand_y:
                expand_map_y(expand_y)
            if len(map[0])-1 < expand_x:
                expand_map_x(expand_x)
            # part 2 diagonal lines
            plotPart2(y1, y2, x1, x2)
        filter_map = [_ for _ in [ list(i for i in x if i>1) for x in map ] if len(_)>0]
        count = sum([len(_) for _ in filter_map])
        print('part 2: {}'.format(count))
