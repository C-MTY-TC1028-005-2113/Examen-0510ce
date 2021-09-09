# función contar_ diagnosticos
def contar_diagnosticos(n):
    casos_delta = 0
    casos_covid19 = 0
    sanos = 0
    for vcc in range(n):
        diag = input("Ingresa diagnostico: ")
        if diag in ['D', 'd']:
            casos_delta = casos_delta  + 1
        elif diag in ['C', 'c']:
            casos_covid19 = casos_covid19 + 1
        elif diag in ['S','s']:
            sanos = sanos + 1

    if casos_delta > 0:
        print("Casos Delta =", casos_delta)
    if casos_covid19 > 0:
        print("Casos Covid-19 =", casos_covid19)
    if sanos > 0:
        print("Casos Sanos =", sanos)


def main( ):
    # 1º Leer la cantidad de diagnosticos
    n = int(input("Ingresa el total de diagnosticos: "))

    # Llamar a la función contar_diagnosticos
    contar_diagnosticos(n)

if __name__=='__main__':
    main()
