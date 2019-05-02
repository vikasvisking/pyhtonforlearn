# Test if all or any  items are true or not

data = ['True', 'True', 'False']

if any(data):
	print('some are true')
else:
	print('Not a Single True')

if all(data):
	print('All are true')

else:
	print('Not all are true')


# it only check if there is any true or false value in the list