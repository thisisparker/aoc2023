from collections import defaultdict

def main(input_lines): 
    running_total = 0
    possible_gears = defaultdict(list)
    for i, line in enumerate(input_lines):
        current_num = ''
        for j, c in enumerate(line):
            if not current_num and c.isdigit():
                current_num = c
                adj_blocks = [(j-1,i-1), (j-1,i), (j-1,i+1),
                              (j,  i-1), (j,i+1)]
            elif current_num and c.isdigit():
                current_num += c
                adj_blocks.extend([(j, i-1), (j, i+1)])
            elif current_num and not c.isdigit():
                adj_blocks.extend([(j, i-1), (j, i), (j, i+1)])

            if current_num and (not c.isdigit() or j == len(line) - 1):
                adj_blocks = [coord for coord in adj_blocks 
                                if 0 <= coord[0] < len(line)
                                and 0 <= coord[1] < len(input_lines)]

                for b in adj_blocks:
                    if input_lines[b[1]][b[0]] not in '.0123456789':
                        running_total += int(current_num)
                    if input_lines[b[1]][b[0]] == '*':
                        possible_gears[(b[0], b[1])].append(int(current_num))

                current_num = ''
                adj_blocks = []

    print(running_total)
    gears = {k: possible_gears[k] for k in possible_gears if len(possible_gears[k]) == 2}
    ratio_total = 0
    for g in gears:
        ratio_total += gears[g][0] * gears[g][1]
    print(ratio_total)

with open('input.txt') as f:
    main([l.strip() for l in f.readlines()])
