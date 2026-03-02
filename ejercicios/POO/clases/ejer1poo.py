class Ejercicio1():
  
    def  __init__ (self):
        self.dividendo = 0
        self.divisor = 0
        self.resultado = ""    
    def lectura_de_datos(self):
    
        self.dividendo = float(input("Escriba el dividendo: "))
        self.divisor = float(input("Escriba el divisor: "))
        

    def proceso_de_datos(self):

        if self.divisor == 0:
            return "No se puede dividir por cero."
        else:
            if self.dividendo % self.divisor == 0.0:
                print( f"{self.dividendo // self.divisor} ")
            else:
                print(f"{self.dividendo // self.divisor} Resto: {self.dividendo % self.divisor}")

    def mostrar_resultados(self):

        print(self.resultado)

