class Ejercicio3():
  
    def  __init__ (self):
        self.distancia = 0
        self.km = 0
        self.m = 0
        self.cm = 0 
        self.resultado = ""   


def lectura_de_datos_distancia(self):
    print('CONVERTIDOR DE CM A KM, M Y CM')
    self.distancia = int(input('Escriba una distancia en centímetros: '))
    return self.distancia

def proceso_de_datos_distancia(self):
    if self.distancia == 0:
        return 'Escriba una distancia mayor que cero.'
    else:

        self.km = self.distancia // 100000
        resto_km = self.distancia % 100000

        self.m = resto_km // 100
        self.cm = resto_km % 100

        return f'{self.distancia} centímetros son {self.km} km {self.m} m {self.cm} cm.'

def mostrar_resultados_distancia(self):
    print(self.resultado)
