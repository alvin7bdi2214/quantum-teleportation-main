from copy_if_kernel_busy import tmplist2, for_bob
from operator import itemgetter

epr_out = [idx for idx, element in enumerate(tmplist2) if element == 'EPR']
print(epr_out)

print(list(itemgetter(*epr_out)(for_bob)))

# class Flexlist(list):
#     def __getitem__(self, keys):
#         if isinstance(keys, (int, slice)):
#             return list.__getitem__(self, keys)
#         return [self[k] for k in keys]

from PIL import Image
import numpy

