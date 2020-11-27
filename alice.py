import random
from PIL import Image
import math

equal_to = {"upl":"u_plus", "EPR":"u_minus", "vpl":"v_plus", "vmin":"v_minus"} #bell state

file_path = r"lena256_bw.pbm"

im = Image.open(file_path)
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

# def chunkIt(seq, num): #function to transform list as num times nested list
#     avg = len(seq) / float(num)
#     out = []
#     last = 0.0

#     while last < len(seq):
#         out.append(seq[int(last):int(last + avg)])
#         last += avg

#     return out

set_encrImPx = lambda p: round(math.sqrt(p))

# n = chunkIt(for_bob, set_encrImPx(len(for_bob)))

if __name__ == "__main__":
    print("random binary strings:", key1)
    print("bell states:", bell_state)
    print("encrypted strings:", for_bob)

    with open('for_bob.txt', 'w') as f:
        print("random binary strings:\n{}\n".format(key1), file=f)
        print("random bell states ({:,} characters):\n{}\n".format(len(bell_state), bell_state), file=f)

    with open('bob_encrIMG.pbm', 'w') as f:
        f.write(f'P4\n{set_encrImPx(len(for_bob))}\n{set_encrImPx(len(for_bob))}\n')
        # for xs in n:
        #     f.write(" ".join(map(str, xs)) + '\n')
        print(for_bob, file=f)

#windows clrf to unix lf
windows_line_ending = b'\r\n'
linux_line_ending = b'\n'

with open('bob_encrIMG.pbm', 'rb') as open_file:
    content = open_file.read()

content = content.replace(windows_line_ending, linux_line_ending)

with open('bob_encrIMG.pbm', 'wb') as open_file:
    open_file.write(content)