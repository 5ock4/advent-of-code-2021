with open('./input1.txt') as f:
	lines = [ int(line.strip()) for line in f]

cnt = 0
prev_s = None
for i in range(len(lines)-2):
	s = sum(lines[i:i+3])
	if (i - 1) >= 0:
		prev_s = sum(lines[i-1:i+2])
	if prev_s and s > prev_s:
		cnt += 1
print(cnt)
