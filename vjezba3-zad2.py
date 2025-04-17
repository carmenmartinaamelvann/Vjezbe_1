def racunaj(A):
    broj=0
    for i in range(A):
        broj=broj+1/3
    for i in range(A):
        broj=broj-1/3
    konačni_rezultat=5+broj
    print(konačni_rezultat)
racunaj(200)
racunaj(2000)
racunaj(20000)
