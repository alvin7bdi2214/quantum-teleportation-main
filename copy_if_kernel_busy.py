import random
import numpy as np
from operator import itemgetter
import sys

equal_to = {"a":"u_plus", "b":"u_minus", "c":"v_plus", "d":"v_minus"} #bell state

p = 8 #length of generated binary

key1 = [] #list of generated binary 
for i in range(p): 
	temp = random.randint(0,1)
	key1.append(temp) 

tmplist2 = [] #list of random sample_letters
for i in range(p):
    while True:
        attempt = str(random.choice(list(equal_to)))
        tmplist2.append(attempt)

        if attempt == 'b':
            break

#evaluate result of alice binary and bell state
def eva(alice, bell):
    if alice == 1:
        if bell == 'a' or bell == 'b':
            return 1
        elif bell == 'c' or bell == 'd':
            return 0
    elif alice == 0:
        if bell == 'c' or bell == 'd':
            return 1
        elif bell == 'a' or bell == 'b':
            return 0


for_bob = [] #list of generated binary and bell state through logic gate
_tmp = tmplist2[:]

for k in key1:
    while _tmp:
        if _tmp[:1] != ['b']:
            for_bob.append(eva(k, *_tmp[:1]))
            _tmp = _tmp[1:]
        else:
            for_bob.append(eva(k, *_tmp[:1]))
            _tmp = _tmp[1:]
            break


#tr = [[eva(k,t) for t in tmplist2] for k in key1] #list comprehension split the key properly
print("generated random binary strings:", key1)
print("generated bell states:", tmplist2)
print("encrypted strings:", for_bob)

with open('for_bob.txt', 'w') as f:
    print("generated random binary strings:\n", key1, file=f)
    print("generated bell states:\n", tmplist2, file=f)
    print("encrypted strings:\n", for_bob, file=f)