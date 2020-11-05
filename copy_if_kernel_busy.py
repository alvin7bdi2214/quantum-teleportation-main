import random
sample_letters = 'abcd'

iter = 0
tmplist2 = []

while True:
    attempt = random.choice(sample_letters)
    tmplist2.append(attempt)

    if tmplist2[iter] == "b":
        break
    else:
        pass
print(tmplist2)