# extract the excerpt and the tag to build a tsv file
import json
import sys

def main():
	FO = open('data.tsv', 'w')
	with open ('entrepreneur.json') as data_file1:
		data1 = json.load(data_file1)
		line = ""
		size = len(data1['results'])
		for i in range(size):
			line =  ('Entrepreneur' + "	" + data1['results'][i]['excerpt']).encode('utf-8').strip() + '\n'
			FO.write(line)
			line = ""
	with open ('interviews.json') as data_file2:
		data2 = json.load(data_file2)
		line = ""
		size = len(data2['results'])
		for i in range(size):
			line = ('Interviews' + "	" + data2['results'][i]['excerpt']).encode('utf-8').strip() + '\n'
			FO.write(line)
			line = ""
	with open('food.json') as data_file3:
		data3 = json.load(data_file3)
		line = ""
		size = len(data3['results'])
		for i in range(size):
			line = ('Food' + "	" + data3['results'][i]['excerpt']).encode('utf-8').strip() + '\n'
			FO.write(line)
			line = ""
	with open ('networking.json') as data_file4:
		data4 = json.load(data_file4)
		line = ""
		size = len(data4['results'])
		for i in range(size):
			line = ('Networking' + "	" + data4['results'][i]['excerpt']).encode('utf-8').strip() + '\n'
			FO.write(line)
			line = ""
	FO.close()
main()
