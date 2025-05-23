import matplotlib.pyplot as plt
def crtanje(x1, y1, x2, y2):
    k=(y2-y1)/(x2-x1)
    c=y1-k*x1
    print(f'Jednadžba pravca je : y ={k:.0f}x + {c:.of}')

    x=[x1, x2]
    y=[k*i + c for i in x]
    plt.scatter([x1, x2], [y1, y2], color='green', label='Točke')
    plt.plot(x, y, label=f'Pravac: y={k:.of}x + {c:.0f}', color='blue')
    plt.title('Točke i pravac kroz te točke')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    if ekran:
        plt.show()
    if spremanje_PDF:
        plt.savefig(ime_datoteke)
        print(f'Spremljeno kao {ime_datoteke}')
    plt.close()
x1=input()
y1=input()
x2=input()
y2=input()
ekran=input()
spremanje_PDF()
if spremanje_PDF:
    ime_datoteke=input()
else:
    ime_datoteke=''
crtanje(x1, y1, x2, y2, ekran, spremanje_PDF, ime_datoteke)



