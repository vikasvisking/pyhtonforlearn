#Demostrating the work of __enter__  and __exit__ methods

class Vikas:

	def some_work(self):
		print('this is some work fucntion')

	def __enter__(self):
		print('Enter')

	def __exit__(self, a1, a2, a3):
		print("Exit")

o=Vikas()
with o:
	# as soon as we have 'with', we need __enter__ and __exit__

	o.some_work()