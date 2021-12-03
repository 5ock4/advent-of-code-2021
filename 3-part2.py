	
with open('./input.txt') as f:
	lines = [line.strip() for line in f]

def most_common(arr, pos):
	pos_str = ''
	for num in arr:
		pos_str += num[pos]

	if pos_str.count('1') > pos_str.count('0'):
		return '1'
	elif pos_str.count('1') < pos_str.count('0'):
		return '0'
	else:
		return None

def least_common(arr, pos):
	pos_str = ''
	for num in arr:
		pos_str += num[pos]

	if pos_str.count('1') < pos_str.count('0'):
		return '1'
	elif pos_str.count('1') > pos_str.count('0'):
		return '0'
	else:
		return None

oxygen = ''
co2 = ''
row_len = len(lines[0])
most = ''

for i in range(row_len):
	most = most_common(lines, i) or '1'
	lines = [ line for line in lines if line[i] == most ]

	if len(lines) == 1:
		oxygen = int(lines[0], 2)

print(oxygen)

with open('./input.txt') as f:
	lines = [line.strip() for line in f]

for i in range(row_len):
	least = least_common(lines, i) or '0'
	lines = [ line for line in lines if line[i] == least ]

	if len(lines) == 1:
		co2 = int(lines[0], 2)

print(co2)

print(oxygen*co2)