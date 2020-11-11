import random
import numpy as np
from operator import itemgetter

equal_to = {"a":"u_plus", "b":"u_minus", "c":"v_plus", "d":"v_minus"} #bell state
count = 0 #count until b is found
count1 = 0 #count for nested loop
tmplist2 = [] #list of random sample_letters
p = 8 #length of generated binary
key1 = [] #list of generated binary
for_bob = [] #list of generated binary and bell state through logic gate
 
for i in range(p): 
	temp = str(random.randint(0,1)) 
	key1.append(temp) 

while True:
    attempt = str(random.choice(list(equal_to)))
    tmplist2.append(attempt)

    if attempt == 'b':
        break

    count += 1

#evaluate result of alice binary and bell state
def eval(alice, bell):
    if alice == '1':
        if bell == 'a' or 'b':
            return 1
        elif bell == 'c' or 'd':
            return 0
    else:
        if bell == 'c' or 'd':
            return 1
        elif bell == 'a' or 'b':
            return 0

for k in key1:
	for t in tmplist2:
		e = str(eval(k, t))
		for_bob.append(e)
	count1 += 1

#tr = [[eval(k,t) for t in tmplist2] for k in key1] #list comprehension split the key properly
print("generated random binary strings:", key1)
print("generated bell states:", tmplist2)
print(for_bob)
