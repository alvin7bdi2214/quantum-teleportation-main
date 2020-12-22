from alice_number import *
from operator import itemgetter

epr_index = [i for i,e in enumerate(bell_state) if e == 'EPR']

bob_bits = list(itemgetter(*epr_index)(encrypted_bits))

print(epr_index)
print(str(bob_bits).replace(',', ''))