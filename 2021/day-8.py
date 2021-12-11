"""
--- Day 8: Seven Segment Search ---
"""
import os
import numpy as np
CWD = os.getcwd()
INPUT = 'https://adventofcode.com/2021/day/8/input'

if __name__ == "__main__":
    input = np.loadtxt("{}/2021/inputs/day-8.txt".format(CWD), dtype='str', delimiter='/n')

    def uniqueCheck(digit):
        if len(digit) == 2: return (1, [1, 2])
        if len(digit) == 4: return (4, [1, 2, 5, 6])
        if len(digit) == 3: return (7, [0, 1, 2])
        if len(digit) == 7: return (8, [0, 1, 2, 3, 4, 5, 6])
        else:
            return False
    
    def segmentsToNumber(s):
        sorted_s = sorted(s)
        if sorted_s == [0, 1, 2, 3, 4, 5]: return 0
        if sorted_s == [1, 2]: return 1
        if sorted_s == [0, 1, 3, 4, 6]: return 2
        if sorted_s == [0, 1, 2, 3, 6]: return 3
        if sorted_s == [1, 2, 5, 6]: return 4
        if sorted_s == [0, 2, 3, 5, 6]: return 5
        if sorted_s == [0, 2, 3, 4, 5, 6]: return 6
        if sorted_s == [0, 1, 2]: return 7
        if sorted_s == [0, 1, 2, 3, 4, 5, 6]: return 8
        if sorted_s == [0, 1, 2, 3, 5, 6]: return 9
    
    def decodeDigit(d, k):
        true_segments = []
        for item in d:
            true_segments.append(k.index(item))
        return(segmentsToNumber(true_segments))

    def decodeDisplay(d):
        segments = [[],[],[],[],[],[],[]]
        all = ''
        unknown_5s = []
        unknown_6s = []
        #get uniques
        for segs in d.split(' '):
            i = uniqueCheck(segs)
            if i:
                if i[0] != 8:
                    for position in i[1]:
                        if len(segments[position]) == 0:
                            segments[position] = list(segs)
                else:
                    all = segs
            else:
                if len(segs) == 5:
                    unknown_5s.append(segs)
                else:
                    unknown_6s.append(segs)
        # start using 7, 4 or 1 knowns
        commons = list(set(segments[0]).intersection(*[seg for seg in segments if len(seg) > 0]))
        for s in segments:
            for option in commons:
                if option in s:
                    s.remove(option)
        segments[1] = commons
        segments[2] = commons
        # refine
        def getNextSegment(val):
            remaining_nums = unknown_5s if val == 6 else unknown_6s
            current_knowns = ''.join(sum([list(x) for x in set(tuple(x) for x in segments)if len(x) > 0], []))
            if val == 2:
                current_knowns = current_knowns.replace(segments[1][0], '')
                current_knowns = current_knowns.replace(segments[1][1], '')
            if val == 4:
                modified_all = all
                for char in current_knowns:
                    modified_all = modified_all.replace(char, '')
                return [modified_all] if modified_all else []  
            if val == 5 or val == 1:
                if len(segments[val + 1]) == 1:
                    segments[val].remove(str(segments[val+1][0]))
                    return segments[val]
            if val == 6:
                seg_1 = ''
                if len(segments[1]) == 2:
                    seg_1 = ''.join(segments[1])
                current_knowns = ''.join([segments[0][0], seg_1, segments[3][0]])
            for unknown in remaining_nums:
                match_list = [characters in current_knowns for characters in unknown]
                if match_list.count(True) == len(current_knowns):
                    for char in current_knowns:
                        unknown = unknown.replace(char, '')
                    return [unknown] if unknown else []
        # refine for seg 4
        segments[3] = getNextSegment(3)
        # refine for seg 7
        segments[6] = getNextSegment(6)
        # refine for seg 6
        segments[5] = getNextSegment(5)
        # refine for seg 5
        segments[4] = getNextSegment(4)
        # refine for seg 3
        segments[2] = getNextSegment(2)
        # refine for seg 2
        segments[1] = getNextSegment(1)
        return [letter[0] for letter in segments]

    def getOutputValue(x, k):
        sorted_signals = ["".join(sorted(pattern)) for pattern in k]
        y = "".join(sorted(x))
        return sorted_signals.index(y)
    
    unique_segments = [[],[],[],[],[],[],[],[],[],[],[]]
    outputs = []
    for string in input:
        (display, output) = string.split(' | ')
        digits = output.split(' ')
        # part 1 get uniques
        for digit in digits:
            index = uniqueCheck(digit)
            if index: 
                unique_segments[index[0]].append(digit)

        #part 2
        key = decodeDisplay(display)
        output_value = []
        for digit in digits:
            output_value.append(str(decodeDigit(digit, key)))
        outputs.append(int(''.join(output_value)))
        
    unique_sums = [len(uniques) for uniques in unique_segments]
    print('part 1: {}'.format(sum(unique_sums)))
    print('part 2: {}'.format(sum(outputs)))
