import random
import numpy as np
from numpy.random import randint
import datetime

equal_to = {"upl":"u_plus", "EPR":"u_minus", "vpl":"v_plus", "vmin":"v_minus"}
amount_of_bit = 8

def alice_bits(n):
    np.random.seed()
    _alice_bits = randint(2, size=n)
    return _alice_bits

alice_bits = alice_bits(amount_of_bit)

bell_state = []

for i in range(amount_of_bit):
    while True:
        attempt = str(random.choice(list(equal_to)))
        bell_state.append(attempt)

        if attempt == 'EPR':
            break

def eva(alice, bell):
    if alice == 1:
        if bell == 'upl' or bell == 'EPR':
            return 1
        elif bell == 'vpl' or bell == 'vmin':
            return 0
    elif alice == 0:
        if bell == 'vpl' or bell == 'vmin':
            return 1
        elif bell == 'upl' or bell == 'EPR':
            return 0

encrypted_bits = []

_tmp = bell_state[:]
for i in alice_bits:
    while _tmp:
        if _tmp[:1] != ['EPR']:
            encrypted_bits.append(eva(i, _tmp[0]))
            _tmp = _tmp[1:]
        else:
            encrypted_bits.append(eva(i, *_tmp[:1]))
            _tmp = _tmp[1:]
            break

if __name__ == "__main__":
    with open('alice_number.txt', 'w') as a:
        print("Alice's numbers:", alice_bits, file=a)
        print("Encrypted Alice numbers:", str(encrypted_bits).replace(',', ''), file=a)
        print(f"\ngenerated on: {datetime.datetime.now()}", file=a)

    with open('key_numbers.txt', 'w') as k:
        print(f"encryption keys ({len(bell_state)} chars):\n", file=k)
        for i,e in enumerate(bell_state):
            print(i, e, file=k)
        print(f"\ngenerated on: {datetime.datetime.now()}", file=k)