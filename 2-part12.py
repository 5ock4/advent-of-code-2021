import re

with open('./input.txt') as f:
	lines = [line.strip() for line in f]

loc = {
	'depth': 0,
	'horizontal': 0,
	'aim': 0
}

for line in lines:
	match = re.search(r'(\D+)\s(\d+)', line)
	dir = match[1].strip()
	val = int(match[2])

	if dir == 'forward':
		loc['horizontal'] += val
		loc['depth'] += (loc['aim']*val)
	elif dir == 'up':
		loc['aim'] -= val
	elif dir == 'down':
		loc['aim'] += val

print(loc['horizontal']*loc['depth'])