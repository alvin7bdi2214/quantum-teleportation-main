import random
from PIL import Image
import math

file_path = r"sample_images/lena256_bw.pbm"

equal_to = {"upl":"u_plus", "EPR":"u_minus", "vpl":"v_plus", "vmin":"v_minus"} #bell state

im = Image.open(file_path)
imList = list(im.getdata(band=None))

p = len(imList)

cnv = lambda c: math.trunc(c/255) #convert 0 and 255 to 0 and 1

key1 = list(map(cnv, imList))

bell_state = [] #list of random sample_letters
for i in range(p):
    while True:
        attempt = str(random.choice(list(equal_to)))
        bell_state.append(attempt)

        if attempt == 'EPR':
            break

#generating random bell states without appending to empty list
"""for i in range(im.size[0]*im.size[1]):
   found = False
    while found == False:
        x = random.choice(list(equal_to))
        print(x)

        if x == 'EPR':
            found = True"""

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
_tmp = bell_state[:]
for k in key1:
    while _tmp:
        if _tmp[:1] != ['EPR']:
            for_bob.append(eva(k, _tmp[0]))
            _tmp = _tmp[1:]
        else:
            for_bob.append(eva(k, *_tmp[:1]))
            _tmp = _tmp[1:]
            break

#transform list as num times nested list
"""def chunkIt(seq, num): 
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out"""

set_encrImPx = lambda p: round(math.sqrt(p))
newLen = set_encrImPx(len(for_bob))


print("image pixel data:", key1)
print("bell states:", bell_state)
print("encrypted strings:", for_bob)

with open('shared_key/for_bob.txt', 'w') as f:
    print("random binary strings:\n{}\n".format(key1), file=f)

with open('shared_key/key.txt', 'w') as f:
    print("random bell states ({:,} characters):\n".format(len(bell_state)), file=f)
    for k,v in enumerate(bell_state):
        print(k, v, file=f)
    

with open('shared_key/encryptedIMG.pbm', 'w') as f:
    f.write(f'P4\n{newLen}\n{newLen}\n')
    for line in range(newLen):
        for col in range(newLen):
            if i < len(for_bob):
                print(for_bob[i], end=' ', file=f)
                i+=1
            else:
                i=0
                print(for_bob[i], end=' ', file=f)
        print(file=f)