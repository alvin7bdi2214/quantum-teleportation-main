import random

equal_to = {"upl":"u_plus", "EPR":"u_minus", "vpl":"v_plus", "vmin":"v_minus"} #bell state

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

        if attempt == 'EPR':
            break

#evaluate result of alice binary and bell state
def eva(alice, bell):
    if alice == 1:
        if bell == 'upl' or bell == 'EPR':
            return 1
        elif bell == 'vpl' or bell == 'vmin':
            return 0
    elif alice == 0:
        if bell == 'vpl' or bell == 'vmin':
            return 1
        elif bell == 'upl' or bell == 'EPR':
            return 0


for_bob = [] #list of generated binary and bell state through logic gate
_tmp = tmplist2[:]

for k in key1:
    while _tmp:
        if _tmp[:1] != ['EPR']:
            for_bob.append(eva(k, _tmp[0]))
            _tmp = _tmp[1:]
        else:
            for_bob.append(eva(k, *_tmp[:1]))
            _tmp = _tmp[1:]
            break

if __name__ == "__main__":
    print("random binary strings:", key1)
    print("bell states:", tmplist2)
    print("encrypted strings:", for_bob)

with open('for_bob.txt', 'w') as f:
    print("random binary strings:\n{}\n".format(key1), file=f)
    print("random bell states ({} characters):\n{}\n".format(len(tmplist2), tmplist2), file=f)
    print("encrypted strings ({} characters):\n{}\n".format(len(for_bob), for_bob), file=f)