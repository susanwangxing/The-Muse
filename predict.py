# using a list of excerpts and their corresponding tags to train 
# and predict article tags based on their excerpts.
# The tags selected for training are: Entrepreneur, Interviews, Food, Networking.
# Prints the tag predictions for each X_test entry, the accuracy of predictions and
# the confusion matrix.
import numpy as np
import scipy
import sklearn
import sys
import pandas as pd

def main():
	data = pd.read_table('data.tsv', header = None, names = ['label', 'message'])
	# convert the labels to numeric values
	data['label_num'] = data.label.map({'Entrepreneur' : 0, 'Interviews': 1, 'Food': 2, 'Networking': 3})
	# define our X and y
	X = data.message
	y = data.label_num
	# split X and y into traning and testing sets
	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1)
	# instantiate the vectorizer
	from sklearn.feature_extraction.text import CountVectorizer
	vect = CountVectorizer()
	# learn training data vocabulary to create a document-term matrix
	vect.fit(X_train)
	X_train_dtm = vect.transform(X_train)
	# transfrom testing data into a document-term matrix
	X_test_dtm = vect.transform(X_test)
	# import and instantiate a Multinomial Naive Bayes model
	from sklearn.naive_bayes import MultinomialNB
	nb = MultinomialNB()
	# train the model using X_train_dtm
	nb.fit(X_train_dtm, y_train)
	# make class predictions for X_test_dtm
	y_pred_class = nb.predict(X_test_dtm)
	# print the predictions for each X_test entry
	print(y_pred_class)
	# calculate accuracy of class predictions
	from sklearn import metrics
	print(metrics.accuracy_score(y_test, y_pred_class))
	# print the confusion matrix
	print (metrics.confusion_matrix(y_test, y_pred_class))
main()