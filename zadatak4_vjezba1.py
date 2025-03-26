def jednadžba_pravca(x1, y1, x2, y2):
    koeficijent_smjera=round((y2-y1)/(x2-x1))
    c=round(y1-koeficijent_smjera*x1)
    print(f'Jednadžba pravca je: y= {koeficijent_smjera}x+ {c}')
x1=input()
y1=input()
x2=input()
y2=input()
jednadžba_pravca(x1, y1, x2, y2)







