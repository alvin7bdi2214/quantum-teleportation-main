from alice import bell_state, for_bob
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

cnv = lambda c: math.trunc(c/255)

g = ((x, y) for x in range(im.size[0]) for y in range(im.size[1]))
lg = list(g)
lg_px = [im.getpixel((l)) for l in lg]
lg_px_01 = [cnv(lg) for lg in lg_px]

# for coord in g:
#     c = im.getpixel((coord))
#     cnv(c)

#track memory usage
import psutil
print(psutil.virtual_memory())