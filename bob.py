from alice import bell_state, for_bob
from operator import itemgetter
import math

idxWhereEPR = [idx for idx, element in enumerate(bell_state) if element == 'EPR']

finalResult = list(itemgetter(*epr_idx)(for_bob))

from PIL import Image
import random

file_name = r"encryptedIMG.pbm"

im = Image.open(file_name)
# print(im.format, im.size, im.mode)

#track memory usage
# import psutil
# print(psutil.virtual_memory())