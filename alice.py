import random
from PIL import Image
import math

equal_to = {"upl":"u_plus", "EPR":"u_minus", "vpl":"v_plus", "vmin":"v_minus"} #bell state

im = Image.open("lena256_bw.pbm")
p = im.size[0]*im.size[1] #length of generated binary

cnv = lambda c: math.trunc(c/255)

g = ((x, y) for x in range(im.size[0]) for y in range(im.size[1]))
lg = list(g)
lg_px = [im.getpixel((l)) for l in lg]
key1 = [cnv(lg) for lg in lg_px]


# key1 = [] #list of generated binary 
# for i in range(p): 
# 	temp = random.randint(0,1)
# 	key1.append(temp) 

bell_state = [] #list of random sample_letters
for i in range(p):
    while True:
        attempt = str(random.choice(list(equal_to)))
        bell_state.append(attempt)

        if attempt == 'EPR':
            break

# for i in range(im.size[0]*im.size[1]):
#     found = False
#     while found == False:
#         x = random.choice(list(equal_to))
#         # print(x)

#         if x == 'EPR':
#             found = True

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

if __name__ == "__main__":
    print("random binary strings:", key1)
    print("bell states:", bell_state)
    print("encrypted strings:", for_bob)

    with open('for_bob.txt', 'w') as f:
        print("random binary strings:\n{}\n".format(key1), file=f)
        print("random bell states ({:,} characters):\n{}\n".format(len(bell_state), bell_state), file=f)

    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'


    with open('bob_encrIMG.pbm', 'wb') as f:
        f.write('P4\n256\n256\n')
        f.write("encrypted strings ({:,} characters):\n{}\n".format(len(for_bob), for_bob), file=f)