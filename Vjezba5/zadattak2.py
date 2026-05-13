N=[200, 2000, 20000]
for i in N:
    a=5.0
    b=1/3
    for m in range(i):
        a+=b
    for m in range(i):
        a-=b
    print(a)


