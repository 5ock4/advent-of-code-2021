    
with open('./input.txt') as f:
	lines = [line.strip() for line in f]

arr = ['']*len(lines[0])

for bin in lines:
    for i, char in enumerate(bin):
        arr[i] += char

gamma = ''
epsilon = ''
for pos in arr:
    if pos.count('1') > pos.count('0'):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma,2)*int(epsilon,2))