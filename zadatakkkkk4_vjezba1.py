def jednadžba_pravca(x1, y1, x2, y2):
    koeficijent_smjera=round((y2-y1)/(x2-x1))
    c=(y1-koeficijent_smjera*x1)
    print(f'Jednadžba pravca je: y= {koeficijent_smjera}x+ {c}')
x1=int(input()) # recimo neka budu koordinate cijeli brojevi.
x2=int(input())
x3=int(input())
x4=int(input())
jednadžba_pravca(x1, y1, x2, y2)







