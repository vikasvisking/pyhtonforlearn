# Parsing Json from File
import json

#open the file
with open('test.json') as f:
	# parse json
	data =json.loads(f.read())

# print
print(data)
print(data['language'])
print(data['letters'][2])