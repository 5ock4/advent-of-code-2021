with open('./input1.txt') as f:
	lines = [line.strip() for line in f]

cnt = 0
prev_num = None
for num in lines:
	num = int(num)
	print(type(num))
	if prev_num and num > prev_num:
		cnt += 1
	prev_num = num

print(cnt)
