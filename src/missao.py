import sys

def main():
    bateria = int(input("Bateria atual (%): "))
    duracao = int(input("Duração prevista da missão (min): "))
    consumo_por_minuto = int(input("Consumo por minuto (%/min): "))

    if not 0 <= bateria <= 100:
        print('A bateria deve estar entre 0 e 100')
        sys.exit(1)

    if duracao <= 0 or consumo_por_minuto <= 0:
        print('Duração e consumo por minuto não podem ser menores ou iguais a zero.')
        sys.exit(1)

    consumo_total = duracao * consumo_por_minuto
    if bateria >= consumo_total:
        print(f'A missão pode ser concluída e sobrará {bateria-consumo_total}%')
    else:
        print(f'A missão não pode ser concluída! Faltam {consumo_total-bateria}%')


if __name__ == '__main__':
    main()