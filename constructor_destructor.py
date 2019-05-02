#creating a custom constructor and destructor in a class

class Vikas:

	def __init__(self):
		print(' this is constructor')

	def __del__(self):
		print('this is destructor')

o = Vikas() #constructor callled
print("hello world")

# destructor will be called at the end of the program
