import random
def randomnumbers():
    r = 0
    r = random.randrange(0,5)
    return r

abc = ["a", "b", "c", "d", "e"]

List = []
while True:
    rand_number = randomnumbers()
    List.append(abc[rand_number])
    if rand_number <3:
        break


for i in List:
    print (i)