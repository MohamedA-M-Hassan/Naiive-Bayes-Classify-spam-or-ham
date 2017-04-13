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
			else 
				traget_is_found = False
				return traget_is_found, -1 , 'not found' 
		else:
			while start <=end:
				middle = int((start + end)/ 2)

# the table will be :
# vocabulary    class_type  no_of_repetation
def data_table(emails):
	word_no=0
	no_of_spam=0
	no_of_ham=0 # not spam
	spam_flag = True
	table={} 
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
				#ret , index , value = binary_search(first_col_table,word)
				if np.array([word,'spam']):
					# don't do any thing
				elif np.array([word,'spam'])==False:
					table[np.array([word,'spam'])]= 0
				next_input_is_vocabulary = False # next element not vacabulary
				the_word_to_use_next_iteration = np.array([word,'spam'])
				'''
				iterate 3la el vocabulary in table
				lw msh mogod yb2a 23ml append
				lw mogoda yb2b mt3mlsh 7aga 
				w b3d kda 2rf3 el flag 2n el next iteration hna5od number
				'''
			elif spam_flag==False and next_input_is_vocabulary==True:
				if np.array([word,'ham']):
					# don't do any thing
				elif np.array([word,'ham'])==False:
					table[np.array([word,'ham'])]= 0
				next_input_is_vocabulary = False # next element not vacabulary
				the_word_to_use_next_iteration = np.array([word,'spam'])
			elif spam_flag==True and next_input_is_vocabulary== False:
				word = int(word)
				table[the_word_to_use_next_iteration] += word
				next_input_is_vocabulary = True
			elif spam_flag==False and next_input_is_vocabulary==False:
				word=int(word)
				table[the_word_to_use_next_iteration] += word
				next_input_is_vocabulary= True            	
	return table




myList =readFromFile("train_data") 
spam , ham,= prior_calculation(myList)
print ("spam: " ,spam, " ham: ", ham)   