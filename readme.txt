Files included:
	posts.json: a json file containing data set of articles using the “Posts” endpoint using the public API of The Muse

	ExploreDataAnalysis.py: a python script that prints a list of features extracted from the tags and plots the frequencies of tags to explore the content of the posts

	image.png: the plot obtained after running ExploreDataAnalysis.py

	extract.py: extract the tags and excerpt of articles with specific tags to build a tsv file for training and predicting tags

	data.tsv: the file produced by running extract.py

	predict.py: a script that predicts article tags and prints the accuracy of the predictions as well as the confusion matrix

	entrepreneur.json: a list of posts with the tag 'entrepreneur'

	interviews.json: a list of posts with the tag 'interviews'

	food.json: a list of posts with the tag 'food'

	networking.json: a list of posts with the tag 'networking'

Analysis of predictive performance:
	The accuracty is 0.75. The accuracy is not extremely high due to the fact that many articles have multiple tags instead of
	one clear-cut category. 

Improvements that I would include to improve performance:
	1. Include more training data. Currently, there are 20 entries for each tag category. The more training data we include the
	better the performance. 
	2. Allow for multiple tags. Many posts have more than one tags, which are not accounted for in this prediction algorithm. 
	Allowing a post to correspond to more than one tags will also improve the performance.