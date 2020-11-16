import functools

forbob = open('for_bob.txt', 'r')
forbob.readlines()[4]
forbob.close()

forbob = open('for_bob.txt', 'r')
forbob.readlines()[7]
forbob.close()

def get_epr_ele():
    forbob = open('for_bob.txt', 'r')

    for f in forbob.readlines()[4]:
        

        where_epr = f.index('EPR')
        print(where_epr)

        forbob.close()
    return f

get_epr_ele()