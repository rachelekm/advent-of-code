"""
--- Day 3: Binary Diagnostic ---
"""
import os
CWD = os.getcwd()
INPUT = 'https://adventofcode.com/2021/day/3/input'

def getRate(lines, index, criteria):
    if(len(lines) == 1):
        return int(lines[0], 2)
    sum_bit_at_index = sum(list(int(line[index]) for line in lines))
    mostCommonBit, conditional = 0, 0
    if criteria:
        mostCommonBit = 1 if sum_bit_at_index >= (len(lines)/float(2)) else 0
        conditional = mostCommonBit
    else:
        mostCommonBit = 1 if sum_bit_at_index > (len(lines)/float(2)) else 0
        conditional = 0 if sum_bit_at_index == (len(lines)/float(2)) else 1 - mostCommonBit
    filteredLines = [line for line in lines if conditional == int(line[index])]
    return getRate(filteredLines, index+1, criteria)

if __name__ == "__main__":
    with open("{}/2021/inputs/day-3.txt".format(CWD), "r") as file:
        lines = file.readlines()
        bitSums = [sum(list(int(line[char]) for line in lines)) for char in range(len(lines[0])-1)] 
        # part 1
        gammaBinary = ['1' if bit_sum >= (len(lines)/2) else '0' for bit_sum in bitSums]
        epsilonBinary = [str(1-int(bit)) for bit in gammaBinary]
        power = int(''.join(gammaBinary), 2)*int(''.join(epsilonBinary), 2)
        print('part 1: {}'.format(power))
        # part 2
        oxyGen = getRate(lines, 0, 1)
        co2Scrub = getRate(lines, 0, 0)
        print('part 2: {}'.format(oxyGen*co2Scrub))


