import random
import numpy as np

# Function to create the random binary string 
def rand_key(p): 
	
	# Variable to store the string 
	key1 = []

	# Loop to find the string of desired length 
	for i in range(p): 
		
		# randint function to generate 
		# 0, 1 randomly and converting the result into str 
		temp = str(random.randint(0,1)) 

		# Concatenation the random 0, 1 to the final result 
		key1 += temp 
		
	return(key1)

# Driver Code 
n = 8
str1 = rand_key(n) 
print("Desired length random binary string is: ", str1)

from operator import itemgetter

equal_to = {"a":"u_plus", "b":"u_minus", "c":"v_plus", "d":"v_minus"}


def find_epr_state():
    
    sample_letters = 'abcd'
    count = 0
    tmplist2 = []

    while True:
        attempt = random.choice(sample_letters)
        tmplist2.append(attempt)

        if attempt == "b":
            break

        count += 1

    return tmplist2

    #print(tmplist2)
    #print("EPR state occurs after " + str(count) + " attempt(s).")

    #res_list = list(itemgetter(*tmplist2)(equal_to))
    #print(str(res_list))

#create logic gate
#group object, use return https://realpython.com/python-return-statement/
def eval(alice, epr):
    if (alice == 1 and epr == "a"):
        return 1  
    elif (alice == 1 and epr == "b"):
        return 1 
    elif (alice == 0 and epr == "c"):
        return 1 
    elif (alice == 0 and epr == "d"):
        return 1
    elif (alice == 1 and epr == "c"):
        return 0 
    elif (alice == 1 and epr == "d"):
        return 0
    elif (alice == 0 and epr == "a"):
        return 0
    elif (alice == 0 and epr == "b"):
        return 0

for_bob = []

while n <= 8:
    rand_key(n)
    find_epr_state()
    e1 = eval(str1, find_epr_state())
    for_bob.append(e1)
print(for_bob)