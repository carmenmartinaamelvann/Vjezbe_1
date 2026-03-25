def jedn_pravca(x_1, x_2, y_1, y_2):
    if x_1==x_2:
        return 'Ne smiju x_1 i x_2 biti isti'
    k= (y_2 - y_1) / (x_2 - x_1)
    ods=y_2 - k*x_2
    return 'y= {}*x + {}'.format(k, ods)
def unosenje_koord(unos):
    pise=''
    while pise=='':
        pise=input(unos)
        if pise=='':
            print('Ovo nije dobro . Potrebno je unijeti.')
    konacno=float(pise)
    return konacno
x_1=unosenje_koord('Unesi x_1:')
x_2=unosenje_koord('Unesi x_2:')
y_1=unosenje_koord('Unesi y_1:')
y_2=unosenje_koord('Unesi y_2:')
ispis=jedn_pravca(x_1, x_2, y_1, y_2)
print(f' Jednadzba pravca je : {ispis} ')
        

