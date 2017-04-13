import numpy as np


# *** read from file
def readFromFile(fileName):
	array = []
	with open(fileName, "r") as ins:
		for line in ins:
			array.append(line)
	return array

# *** calculate prior only
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

# *** create the table: (3 functions)
def sort_table(list):
	list = sorted(list,key=lambda l:l[0], reverse=False)
	return list

def binary_search(L, target,class_type=None):
	L=sort_table(L)
	traget_is_found = True
	start = 0
	end = len(L) - 1
	if class_type == None: 
		while start <= end:
			middle = int((start + end)/ 2)
			midpoint = L[middle]
			if midpoint > target:
				end = middle - 1
			elif midpoint < target:
				start = middle + 1
			elif middle ==target:
				return traget_is_found, middle , midpoint
			else:
				traget_is_found = False
				return traget_is_found, -1 , 'not found' 
		else:
			while start <=end:
				middle = int((start + end)/ 2)

# 2 tables : spam_table, ham_table
# all words will be in a set

def data_table_and_prior(emails):
	word_no=0
	no_of_spam=0
	no_of_ham=0 # not spam
	spam_flag = True
	spam_table={} # initialize dictionary
	ham_table={} 
	all_words=set() # initialize set
	next_input_is_vocabulary = True # if False: then it is not vacabulary but no_of_repetation
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
			elif spam_flag and next_input_is_vocabulary:
				if not(word in spam_table):
					spam_table[word]= 0 	# append to dictionary
				next_input_is_vocabulary = False # next element not vacabulary
				the_word_to_use_next_iteration = word
				all_words |= {word} # append to set
				'''
				iterate 3la el vocabulary in table
				lw msh mogod yb2a 23ml append
				lw mogoda yb2b mt3mlsh 7aga 
				w b3d kda 2rf3 el flag 2n el next iteration hna5od number
				'''
			elif spam_flag==False and next_input_is_vocabulary==True:
				if not(word in ham_table):
					ham_table[word]= 0		# append to dictionary
				next_input_is_vocabulary = False # next element not vacabulary
				the_word_to_use_next_iteration = word
				all_words |= {word} # append to set
			elif spam_flag==True and next_input_is_vocabulary== False:
				word = int(word)
				spam_table[the_word_to_use_next_iteration] += word
				next_input_is_vocabulary = True
			elif spam_flag==False and next_input_is_vocabulary==False:
				word=int(word)
				ham_table[the_word_to_use_next_iteration] += word
				next_input_is_vocabulary= True            	
	total = no_of_ham + no_of_spam
	return spam_table ,ham_table, no_of_spam , no_of_ham , total , all_words


# *** to make classification
def list_of_mails(emails):
	list = []
	for email in emails:
		list.append(email)
	return list

def all_words_in_mail(mail):
	all_words =set()
	next_input_is_vocabulary = True
	for word in email.split():
		if word[0]== '/':
			continue
		elif word == 'spam' or word=='ham':
			all_words |= {word}
		elif next_input_is_vocabulary:
			all_words |= {word}
			next_input_is_vocabulary =False
		elif next_input_is_vocabulary==False:
			next_input_is_vocabulary =True
	return all_words


def prob_feature_given_class (all_words_in_mail,words_in_class_1,words_in_class_2):
	prob_feature_give_class_1 = 1 # initialy
	prob_feature_give_class_2 = 1 # initialy
	for word in all_words_in_mail:
		# for class 1
		if (word in words_in_class_1)==False:
			prob_feature_give_class_1=0
		elif (word in words_in_class_1) and (not(prob_feature_give_class_1==0)):
			prob_feature_give_class_1 *= words_in_class_1[word]/len(words_in_class_1)
		# for class 2
		if (word in words_in_class_2)==False:
			prob_feature_give_class_2=0
		elif (word in words_in_class_2) and (not(prob_feature_give_class_2==0)):
			prob_feature_give_class_2 *= words_in_class_2[word]/len(words_in_class_2)
	return prob_feature_give_class_1 , prob_feature_give_class_2 
	

emails =readFromFile("train_data") 
spam_table ,ham_table, no_of_spam , no_of_ham , total , all_words = data_table_and_prior (emails)
#print ("all " ,len(all_words), " ham: ", len(ham_table), "spam", len(spam_table))
