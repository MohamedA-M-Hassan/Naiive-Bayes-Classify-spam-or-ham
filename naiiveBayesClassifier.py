import numpy as np

def readFromFile(fileName):
	array = []
	with open(fileName, "r") as ins:
		for line in ins:
			array.append(line)
	return array

def prior_calculation(string_stream):
	no_of_spam=0
	no_of_ham=0 # not spam

	for row in string_stream:
		for word in row.split():
			if word == "spam":
				no_of_spam = no_of_spam+1
			elif word == "ham":
				no_of_ham = no_of_ham+1
	total = no_of_ham + no_of_spam
	return no_of_spam/total , no_of_ham/total





myList =readFromFile("train_data") 
spam , ham,= prior_calculation(myList)
print ("spam: " ,spam, " ham: ", ham)	