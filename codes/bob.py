from alice import *
from operator import itemgetter
import math
from PIL import Image

epr_idx = [idx for idx, element in enumerate(bell_state) if element == 'EPR']

finalResult = list(itemgetter(*epr_idx)(for_bob))
finalResult_flip = [1 if f == 0 else 0 for f in finalResult]


file_name = r"shared_key/encryptedIMG.pbm"
img_decr = Image.open(file_name)

with open('result_images/decryptedIMG.pbm', 'w') as d:
    d.write(f'P1\n{im.size[1]} {im.size[0]}\n')
    i = 0
    for line in range(im.size[1]):
        for col in range(im.size[0]):
            if i < len(finalResult_flip):
                print(finalResult_flip[i], end=' ', file=d)
                i += 1
            else:
                i = 0
                print(finalResult_flip[i], end=' ', file=d)
        print(file=d)

#track memory usage
# import psutil
# print(psutil.virtual_memory())