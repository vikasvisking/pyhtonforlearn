#list comprehension in python

def f(x):
	return x**2

data =[f(x) for x in range(10)]

for x in range(10):
	print(f'{x} = {data[x]}')