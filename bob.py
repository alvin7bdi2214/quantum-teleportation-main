from copy_if_kernel_busy import bell_state, for_bob
from operator import itemgetter
import math

epr_idx = [idx for idx, element in enumerate(bell_state) if element == 'EPR']

res = list(itemgetter(*epr_idx)(for_bob))

# class Flexlist(list):
#     def __getitem__(self, keys):
#         if isinstance(keys, (int, slice)):
#             return list.__getitem__(self, keys)
#         return [self[k] for k in keys]

from PIL import Image
import random
im = Image.open("lena_bw.pbm")
# print(im.format, im.size, im.mode)

#using cartesian product to generate all coordinates
# import itertools
# def cartesian_prod(cx,cy):
#     for ix, iy in itertools.product((range(cx), range(cy)))

  
g = ((x, y) for x in range(im.size[0]) for y in range(im.size[1]))
cnv = lambda c: math.trunc(c/255)
for coord in g:
    c = im.getpixel((coord))
    cnv(c)


for i in range(im.size[0]*im.size[1]):
    found = False
    while found == False:
        x = random.choice(list(equal_to))
        # print(x)

        if x == 'EPR':
            found = True

#track memory usage
import psutil
print(psutil.virtual_memory())
