import matplotlib.pyplot as plt
def crtanje(x_1, x_2, y_1, y_2):
    k=(y_2 - y_1) / (x_2 - x_1)
    ods=y_2 - k*x_2
    jedn= f'y= {k}x + {ods}'
    plt.plot([x_1, x_2], [y_1, y_2], 'go-', label=jedn)
    plt.grid(True)
    plt.legend()

    odabir=input('Odaberi P ili S').lower()
    if odabir=='s':
        ime=input('Upisi ime PDF-a:')
        plt.savefig(f'{ime}.pdf')
    else:
        plt.show()
    return jedn 
x1=float(input('x_1:'))
x2=float(input('x_2:'))
y1=float(input('y_1:'))
y2=float(input('y_2:'))
ispis=crtanje(x1, x2, y1, y2)
print('Jednadzba ', ispis)

