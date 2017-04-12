def readFromFile(fileName):
	array = []
	with open(fileName, "r") as ins:
		for line in ins:
			array.append(line)
	return array


list =readFromFile("train_data") 
for row in list:
	print("row : ",row)