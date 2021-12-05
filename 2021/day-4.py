"""
--- Day 4: Giant Squid---
"""
import os
import itertools
CWD = os.getcwd()
INPUT = 'https://adventofcode.com/2021/day/4/input'

def organizeBoard(lines):
    board = []
    tables = [lines[x+1:x+6] for x in range(0, len(lines), 6)]
    for table in tables:
        for row in table:
            board.append([num.strip("',/\n") for num in row.split(' ') if num != ''])
        
    return [board[x:x+5] for x in range(0, len(board), 5)]

def sumBoard(board):
    cleanedBoard = []
    for row in board:
        cleanedBoard.append([int(num) for num in row if num != "X"])
    return sum([sum(list) for list in cleanedBoard])

def checkBingo(board):
    score = 0
    for row in board:
        if ''.join(row) == 'XXXXX':
            score = sumBoard(board)
            break
    for column in zip(*board):
        if ''.join(column) == 'XXXXX':
            score = sumBoard(board)
            break
    return score

if __name__ == "__main__":
    with open("{}/2021/inputs/day-4.txt".format(CWD), "r") as file:
        lines = file.readlines()
        numbers_drawn = lines.pop(0).split(',')
        bingoboards_1, bingoboards_2 = organizeBoard(lines), organizeBoard(lines)
        finalscore_part1, finalscore_part2 = 0, 0
        # part 1
        for draw in numbers_drawn:
            for board in bingoboards_1:
                for row in board:
                    row[:] = ["X" if num==draw else num for num in row]
                bingo = checkBingo(board)
                if bingo:
                    finalscore_part1 = bingo*int(draw)
                    break
            if finalscore_part1:
                break
        print('part 1: {}'.format(finalscore_part1))
        # part 2
        completed = []
        for draw in numbers_drawn:
            for board_i, board in enumerate(bingoboards_2):
                for row in board:
                    row[:] = ["X" if num==draw else num for num in row]
                bingo = checkBingo(board)
                if bingo:
                    if board_i not in completed and len(completed) == len(bingoboards_2)-1:
                        finalscore_part2 = sumBoard(board)*int(draw)
                        break
                    else:
                        if board_i not in completed:
                            completed.append(board_i)
            if finalscore_part2:
                break 
        print('part 2: {}'.format(finalscore_part2))
                    



