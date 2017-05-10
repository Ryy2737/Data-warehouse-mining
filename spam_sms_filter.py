## import modules here 

################# Question 1 #################

def multinomial_nb(training_data, sms):# do not change the heading of the function
	spam_dict={}
	ham_dict={}
	spam_total_freq=0
	ham_total_freq=0
	spam_training_num=0
	ham_training_num=0
	#save texts with its freq into spam_dict and ham_dict
	for i in training_data:
		if i[1]=="spam":
			spam_training_num+=1
			for j in i[0]:
				if not j in spam_dict:
					spam_dict[j]=i[0][j]
				else:
					spam_dict[j]+=i[0][j]
		if i[1]=="ham":
			ham_training_num+=1
			for j in i[0]:
				if not j in ham_dict:
					ham_dict[j]=i[0][j]
				else:
					ham_dict[j]+=i[0][j]
	#add-1 smooth unobserved words
	for i in spam_dict:
		if not i in ham_dict:
			ham_dict[i]=0
	for i in ham_dict:
		if not i in spam_dict:
			spam_dict[i]=0
	for i in spam_dict:
		spam_dict[i]+=1
		spam_total_freq+=spam_dict[i]#update total freq
	for i in ham_dict:
		ham_dict[i]+=1
		ham_total_freq += ham_dict[i]

	#freq to freq ratio
	for i in spam_dict:
		spam_dict[i]=spam_dict[i]/spam_total_freq
	for i in ham_dict:
		ham_dict[i]=ham_dict[i]/ham_total_freq
	#ratio=[spam_training_num/total_num]/[ham_training_num/total_num]
	ratio=spam_training_num/ham_training_num
	#multiply prob ratio for each words in sms
	for i in sms:
		if i in spam_dict:
			ratio *= spam_dict[i]/ham_dict[i]

	return(ratio)
