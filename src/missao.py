import sys

def main():
    bateria = int(input("Bateria atual (%): "))
    duracao = int(input("Duração prevista da missão (min): "))
    consumoPorMinuto = int(input("Consumo por minuto (%/min): "))

    if not 0 <= bateria <= 100:
        print('A bateria deve estar entre 0 e 100')
        sys.exit(1)

    if duracao <= 0 or consumoPorMinuto <= 0:
        print('Duração e consumo por minuto não podem ser menores ou iguais a zero.')
        sys.exit(1)

    consumoTotal = duracao * consumoPorMinuto
    if bateria >= consumoTotal:
        print(f'A missão pode ser concluída e sobrará {bateria-consumoTotal}%')
    else:
        print(f'A missão não pode pode ser concluída! Faltam {consumoTotal-bateria}%')
    return


if __name__ == '__main__':
    main()