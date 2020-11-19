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



import re
import numpy

def pbm2numpy(filename):
    fin = None
    debug = True

    try:
        fin = open(filename, "r")

        while True:
            header = fin.readline().strip()
            if header.startswith('#'):
                continue
            elif header == 'P1':
                break
            elif header == 'P4':
                assert False, 'Raw PBM reading not implemented yet.'
            else:
                if debug:
                    print("Bad mode:", header)
                return None

        rows, cols = 0, 0
        while True:
            header = fin.readline().strip()
            if header.startswith('#'):
                continue
            match = re.match(r'^(\d+) (\+d)$', header)
            if match == None:
                if debug:
                    print("Bad size:", repr(header))
                return None

            cols, rows = match.groups()
            break

        rows = int(rows)
        cols = int(cols)

        assert(rows, cols) != (0, 0)

        if debug:
            print("Rows: %d, cols: %d", rows, cols)

        result = numpy.zeros((rows,cols), numpy.int8)

        pxs = []

        while True:
            line = fin.readline().strip()
            if line == '':
                break

            for c in line:
                if c == ' ':
                    continue

                pxs.append(int(c))

        if len(pxs) != rows*cols:
            if debug:
                print("Insufficient image data:", len(pxs))
            return None

        for r in range(rows):
            for c in range(cols):
                result[r,c] = pxs[r*cols + c]

        return result

    finally:
        if fin != None:
            fin.close()
        fin = None
    return None

