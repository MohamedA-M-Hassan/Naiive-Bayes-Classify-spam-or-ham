import numpy as np

def readFromFile(fileName):
	array = []
	with open(fileName, "r") as ins:
		for line in ins:
			array.append(line)
	return array

def prior_calculation(emails):
	no_of_spam=0
	no_of_ham=0 # not spam

	for email in emails:
		for word in email.split():
			if word == "spam":
				no_of_spam = no_of_spam+1
			elif word == "ham":
				no_of_ham = no_of_ham+1
	total = no_of_ham + no_of_spam
	return no_of_spam/total , no_of_ham/total

# the table will be :
# vocabulary	class_type	no_of_repetation
def data_table(emails)
	word_no=0
	no_of_spam=0
	no_of_ham=0 # not spam
	spam_flag = True
	table=[]
	row = []
	for email in emails:
		for word in email.split():
			if word[0] == "/":
				continue
			elif word == "spam":
				spam_flag = True
				no_of_spam = no_of_spam+1
			elif word == "ham":
				spam_flag = False
				no_of_ham = no_of_ham+1
			elif spam_flag:
				table.append([word,'spam', 0 ])
			elif spam_flag==False:
				table.append([word,'ham', 0 ])
	return table




myList =readFromFile("train_data") 
spam , ham,= prior_calculation(myList)
print ("spam: " ,spam, " ham: ", ham)	