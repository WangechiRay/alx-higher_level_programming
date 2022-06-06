#!/usr/bin/python3


def magic_calculation(a, b):

    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))
<<<<<<< HEAD


=======
>>>>>>> 0125f0433ce4f7709de507d3b740969926dbe228
