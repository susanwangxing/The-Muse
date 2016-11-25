# read the json file and save all the tags in an array. Extract features
# from the tags and count the frequency of each tag from the entries.
# Print a list of features extracted from the tags.
# Plot the frequencies to explore the content of the posts.
import numpy as np
import sklearn
import sys
import matplotlib.pyplot as plt
import json

def main():
	with open('posts.json') as data_file:
		data = json.load(data_file)
		line = ""
		size = len(data['results'])
		tags = []
		for i in range(size):
			for j in range(len(data['results'][i]['tags'])):
				line = data['results'][i]['tags'][j]['name']
				tags.append(line)
		from sklearn.feature_extraction.text import CountVectorizer
		vect = CountVectorizer()
		vect.fit(tags)
		# a list of features
		print(vect.get_feature_names())
		# locations of non-zero values and what is the value at that location
		tags_dtm = vect.transform(tags)
		# a matrix: row: entries in data; column: frequency of occurance of each feature
		array = tags_dtm.toarray()
		# find the sums of rows
		sumArray= array[0]
		for i in range(1, len(array)):
			temp = array[i]
			sumArray = sumArray + array[i]
		fig,ax = plt.subplots()
		fig.suptitle('Explore Content', fontsize=20)
		y = np.array(sumArray)
		x = np.arange(len(np.asarray(vect.get_feature_names())))
		plt.xticks(x, np.asarray(vect.get_feature_names()), rotation='vertical')
		plt.tight_layout(pad=2)
		ax.plot(x,y)
		plt.show()
main()