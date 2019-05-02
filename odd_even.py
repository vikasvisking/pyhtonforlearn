# splititng the data in odd even list


data = [43 , 56, 67, 87, 90, 655, 100 , 3232324]

odd = []

even = []

for n in data:
	if n%2:
		print(type(n%2))
		odd.append(n)

	else:
		even.append(n)

print(f'Odd = {odd}')
print(f'Even = {even}')