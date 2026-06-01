'''
calculadora de minutos
'''

'''import curses
stdscr = curses.initscr()'''

total = 0
contador = 0

while True:
    entrada = input("Minutos (ou = para sair): ")
    if entrada == '=':
        break
    
    try:
        minutos = float(entrada)
        if minutos >= 0:
            total += minutos
            contador += 1
        else:
            print("Apenas valores positivos!")
    except ValueError:
        print("Número inválido!")

horas = total / 60
print(f"\n{contador} entradas | Total: {total:.1f} min | {horas:.1f} horas")
