from alice import bell_state, for_bob
from operator import itemgetter
import math

cnvTo255 = lambda c2: c2*255
for_bobDecry = list(map(cnvTo255, for_bob))

epr_idx = [idx for idx, element in enumerate(bell_state) if element == 'EPR']
print(epr_idx)
finalResult = list(itemgetter(*epr_idx)(for_bob))

from PIL import Image

file_name = r"encryptedIMG.pbm"

im = Image.open(file_name)
# print(im.format, im.size, im.mode)

#track memory usage
# import psutil
# print(psutil.virtual_memory())

with open('decryptedIMG.pbm', 'w') as d:
    d.write(f'P4\n')
    