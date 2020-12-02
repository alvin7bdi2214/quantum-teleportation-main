from alice import *
from operator import itemgetter
import math
from PIL import Image

cnvTo255 = lambda c2: c2*255
for_bobDecry = list(map(cnvTo255, for_bob))

epr_idx = [idx for idx, element in enumerate(bell_state) if element == 'EPR']
print(epr_idx)
finalResult = list(itemgetter(*epr_idx)(for_bobDecry))


file_name = r"encryptedIMG.pbm"

img_decr = Image.open(file_name)
# print(im.format, im.size, im.mode)

with open('decryptedIMG.pbm', 'w') as d:
    d.write(f'P4\n')
    i = 0
    for line in range(im.size[1]):
        for col in range(im.size[0]):
            if i < len(finalResult):
                print(finalResult[i], end=' ', file=d)
                i += 1
            else:
                i = 0
                print(finalResult[i], end=' ', file=d)
        print(file=d)

#track memory usage
# import psutil
# print(psutil.virtual_memory())