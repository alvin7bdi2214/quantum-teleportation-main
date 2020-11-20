from copy_if_kernel_busy import tmplist2, for_bob
from operator import itemgetter
import math

epr_out = [idx for idx, element in enumerate(tmplist2) if element == 'EPR']
# print(epr_out)

# print(list(itemgetter(*epr_out)(for_bob)))

# class Flexlist(list):
#     def __getitem__(self, keys):
#         if isinstance(keys, (int, slice)):
#             return list.__getitem__(self, keys)
#         return [self[k] for k in keys]

from PIL import Image
im = Image.open("lena_bw.pbm")

def gen_all_coor(l,h):  
    g = ((x, y) for x in range(l) for y in range(h))
    for coord in g:
        print(im.getpixel((coord)))
    return g

conv_0_or_1 = lambda c: math.trunc(c/255)