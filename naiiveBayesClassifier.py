import numpy as np
import operator


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

# 2 tables : spam_table, ham_table (dictionary)
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
				next_input_is_vocabulary = True
			elif word == "ham":
				spam_flag = False
				no_of_ham = no_of_ham+1
				next_input_is_vocabulary =True
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
	return spam_table ,ham_table, no_of_spam , no_of_ham , total


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
			mail_type = word
		elif next_input_is_vocabulary:
			all_words |= {word}
			next_input_is_vocabulary =False
		elif next_input_is_vocabulary==False:
			next_input_is_vocabulary =True
	return mail_type,all_words



def prob_feature_given_class (all_words_in_mail,words_in_class,no_of_class):
	# all_words_in_mail is set , words_in_class is dictionary
	prob_feature_give_class = 1 # initialy
	sum_ = sum(words_in_class.values())
	for word in all_words_in_mail:
		if (word in words_in_class)==False:
			prob_feature_give_class=0
			break
		elif word in words_in_class:
			prob_feature_give_class *= words_in_class[word]/len(words_in_class)
			#prob_feature_give_class *= words_in_class[word]/no_of_class
			#prob_feature_give_class *= words_in_class[word]/sum_

	# Laplace smoothed
	if prob_feature_give_class == 0:
		prob_feature_give_class = 1 / ( len(all_words_in_mail) + sum_ )
		#prob_feature_give_class *= 1/(len(words_in_class)+sum_)
	return prob_feature_give_class

def max_5_words_value(calss_table):
	total_no_of_repetition = sum(calss_table.values())
	temp= sorted(calss_table.items(), key=operator.itemgetter(1), reverse=True)
	i=0
	for r in temp:
		print("word_",i," is : ", r[0] )
		print("		it's no_of_repetition : ", r[1])
		print("		it's probability : ", r[1]/total_no_of_repetition)
		
		i +=1
		if i==5:
			break 
	pass

#############
# main
############

#*** training 
emails =readFromFile("train_data") 
spam_table ,ham_table, no_of_spam , no_of_ham , total  = data_table_and_prior(emails)
#print ( " ham: ", len(ham_table), "spam", len(spam_table))
spam_prior = no_of_spam/total
ham_prior = no_of_ham/total
#print("no_of_spam: ",no_of_spam," len(spam_table) : ", len(spam_table))


print("--- question_1: priors?? ---")
print("spam_prior = ", spam_prior)
print("ham_prior  = ",ham_prior)
print("		")
print("		")
print("--- question_2: 5 most likeley words  ?? ---")
print("		")
#*** most 5 max value
print("5 most likily in ** spam ** ")
max_5_words_value(spam_table)
print(" ")
print("5 most likily in ** not spam ** ")
max_5_words_value(ham_table)






#*** classification: test_data

emails = readFromFile("test_data")
no_of_emails = len(emails)
no_of_correct_classification_mail = 0
for email in emails:
	# get mail_type just to check if your classification is good or not
	mail_type,all_words = all_words_in_mail(email) # set
	prob_words_given_spam = prob_feature_given_class(all_words,spam_table,no_of_spam)
	prob_words_given_ham = prob_feature_given_class(all_words,ham_table,no_of_ham) 
	# print("pr spam: ", prob_words_given_spam)
	# print("pr spam: ", prob_words_given_ham)
	prob_spam_given_words = spam_prior * prob_words_given_spam
	prob_ham_given_words = ham_prior * prob_words_given_ham
	if (prob_ham_given_words >= prob_spam_given_words):
		if mail_type=='ham':
			no_of_correct_classification_mail += 1
	else:
		if mail_type=='spam':
			no_of_correct_classification_mail += 1

print("--- question_3: classification part and calculate accuracy  ?? ---")
print(" ")
print("no of correct: ", no_of_correct_classification_mail)
print("total mails to test: ", no_of_emails)
print("accuracy : ", no_of_correct_classification_mail/no_of_emails)
print(" ")
print("If I were a spammer,I would like to use the 5 most likely words in *not spam* many times in my spam emails")	 