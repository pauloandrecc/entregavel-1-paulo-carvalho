import sys

def main():
    bateria = int(input("Bateria atual (%): "))
    duracao = int(input("Duração prevista da missão (min): "))
    consumoPorMinuto = int(input("Consumo por minuto (%/min): "))

    consumoTotal = duracao * consumoPorMinuto
    if bateria >= consumoTotal:
        print(f'A missão pode ser concluída e sobrará {bateria-consumoTotal}%')
    else:
        print(f'A missão não pode pode ser concluída! Faltam {consumoTotal-bateria}%')
    return


if __name__ == '__main__':
    main()