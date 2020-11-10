import random
import numpy as np
from operator import itemgetter

equal_to = {"a":"u_plus", "b":"u_minus", "c":"v_plus", "d":"v_minus"} #bell state
sample_letters = 'abcd' #randomly pick key of bell state dictionary
count = 0 #count until b is found
count1 = 0 #count for nested loop
tmplist2 = [] #list of random sample_letters
p = 8 #length of generated binary
key1 = [] #list of generated binary
for_bob = [] #list of generated binary and bell state through logic gate
 
for i in range(p): 
	temp = str(random.randint(0,1)) 
	key1 += temp 

while True:
    attempt = random.choice(sample_letters)
    tmplist2.append(attempt)

    if attempt == "b":
        break

    count += 1

#evaluate result of alice binary and bell state
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

for k in enumerate(key1):
	for t in enumerate(tmplist2):
		e = eval(k,t)
		for_bob.append(e)
	count1 += 1
for_bob