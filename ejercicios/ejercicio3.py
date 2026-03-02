def lectura_de_datos_distancia():
    print('CONVERTIDOR DE CM A KM, M Y CM')
    distancia = int(input('Escriba una distancia en centímetros: '))
    return distancia
def proceso_de_datos_distancia(distancia):
    if distancia == 0:
        return 'Escriba una distancia mayor que cero.'
    else:

        km = distancia // 100000
        resto_km = distancia % 100000

        m = resto_km // 100
        cm = resto_km % 100

        return f'{distancia} centímetros son {km} km {m} m {cm} cm.'

def mostrar_resultados_distancia(resultado):
    print(resultado)

def ejercicio_3():
    distancia = lectura_de_datos_distancia()
    resultado = proceso_de_datos_distancia(distancia)
    mostrar_resultados_distancia(resultado)

ejercicio_3()