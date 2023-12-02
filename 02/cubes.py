from collections import Counter

def main(input_lines):
    running_sum = 0
    power_sum = 0

    for l in input_lines:
        meta, data = l.split(':')
        round_no = int(meta.split()[1])

        c = Counter()
        for r in data.split(';'):
            dc = Counter({draw.split()[1]: int(draw.split()[0])
                          for draw in r.split(',')})
            for k in dc:
                c[k] = dc[k] if dc[k] > c[k] else c[k]


        if c['green'] <= 13 and c['red'] <= 12 and c['blue'] <= 14:
            running_sum += round_no 
        
        power = c['green'] * c['red'] * c['blue']
        power_sum += power

    print(running_sum)
    print(power_sum)
                

with open('input.txt') as f:
    main([l.strip() for l in f.readlines()])
