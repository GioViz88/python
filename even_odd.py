def even_odd(x):
    ia = 0
    ib = 0
    ic = 0
    for i in x:
        ia = ((3 * i) + 2)
        ib = (i + 5)
        ic = (i * i)
        if (ia % 2 == 0):
            ia = str(ia)
            ia = 'even'
        else:
            ia = str(ia)
            ia = 'odd'
        if (ib % 2 == 0):
            ib = str(ib)
            ib = 'even'
        else:
            ib = str(ib)
            ib = 'odd'
        if (ic % 2 == 0):
            ic = str(ic)
            ic = 'even'
        else:
            ic = str(ic)
            ic = 'odd'
    return ia, ib, ic
    
x = [1,2,3,4]

print(even_odd(x))