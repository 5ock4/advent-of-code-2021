    
with open('./input.txt') as f:
	lines = [line.strip() for line in f]
    

def calc_arr(lines):
    arr = ['']*len(lines[0])

    for bin in lines:
        for i, char in enumerate(bin):
            arr[i] += char

    return arr

arr = calc_arr(lines)

def calc(arr, lines):
    l = []
    for i, pos in enumerate(arr):
        if pos.count('1') >= pos.count('0'):
            for bin in lines:
                if bin[i] == '1':
                    l.append(bin)
    
    if len(lines) == 1:
        return lines

    calc_arr(lines)
    return calc(arr, lines)

print(calc(arr, lines))