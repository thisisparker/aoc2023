NUMBERS = {'one':'o1e',
           'two':'t2o',
           'three':'t3e',
           'four':'f4r',
           'five':'f5e',
           'six':'s6x',
           'seven':'s7n',
           'eight':'e8t',
           'nine':'n9e'}

def calibrate(lines, replace_numbers=False):
    calib = 0
    for l in lines:
        if replace_numbers:
            for d in NUMBERS:
                l = l.replace(d, NUMBERS[d])
        cal_str = ''
        for c in l:
            if c.isnumeric():
                cal_str += c
                break
        for c in l[::-1]:
            if c.isnumeric():
                cal_str += c
                break
        if cal_str:
            calib += int(cal_str)

    print(calib)


with open('input.txt') as f:
    input_lines = [l.strip() for l in f.readlines()]

calibrate(input_lines)
calibrate(input_lines, True)
