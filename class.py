
print("Registra las caracteristicas que desees de los siguientes vehiculos")

#Class: Car
class Car:
    
    #Class Attribute

    seller = "M Car C.A."

    #Instance Attributes Init

    def __init__(self,brand,model,color,year):

        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    #Class Definition
        
    def show_attr(self):
        return "Marca: {}, Modelo: {}, Color: {}, Año: {}".format(self.brand,self.model,self.color,self.year)
    
print("Elige las caracteristicas de 2 carros")

print("Las caracteristicas del primer carro son?")

marcacar1= input("elige la marca")

modelocar1= input("elige el modelo")

colorcar1= input("elige  el color")

añocar1= input("elige el año de salida")

print("Las caracteristicas del segundo carro son?")

marcacar2= input("elige la marca")

modelocar2= input("elige el modelo")

colorcar2= input("elige  el color")

añocar2= input("elige el año de salida")





car1 = Car(marcacar1,modelocar1,colorcar1,añocar1)
print(car1.show_attr())
car2 = Car(marcacar2,modelocar2,colorcar2,añocar2)
print(car2.show_attr())


#barco

#Class: Ship
class Ship:
    
    #Class Attribute

    seller = "M Ship C.A."

    #Instance Attributes Init

    def __init__(self,storage,model,color,year):

        self.storage = storage
        self.model = model
        self.color = color
        self.year = year

    #Class Definition
        
    def show_attr(self):
        return "Capacidad de carga: {}, Modelo: {}, Color: {}, Año: {}".format(self.storage,self.model,self.color,self.year)

print("Elige las caracteristicas de 2 barcos")

print("Las caracteristicas del primer barco son?")

cargaship1= input("elige la capacidad de carga")

modeloship1= input("elige el modelo")

colorship1= input("elige  el color")

añoship1= input("elige el año de salida")

print("Las caracteristicas del segundo barco son?")

cargaship2= input("elige la capacidad de carga")

modeloship2= input("elige el modelo")

colorship2= input("elige  el color")

añoship2= input("elige el año de salida")

ship1 = Ship(cargaship1,modeloship1,colorship1,añoship1)
print(ship1.show_attr())
ship2 = Ship(cargaship2,modeloship2,colorship2,añoship2)
print(ship2.show_attr())



#avion

#Class: Airplane
class Airplane:
    
    #Class Attribute

    seller = "M Airplane C.A."

    #Instance Attributes Init

    def __init__(self,passengers,model,color,year):

        self.passengers = passengers
        self.model = model
        self.color = color
        self.year = year

    #Class Definition
        
    def show_attr(self):
        return "Numero de pasajeros: {}, Modelo: {}, Color: {}, Año: {}".format(self.passengers,self.model,self.color,self.year)
    
print("Elige las caracteristicas de 2 aviones")

print("Las caracteristicas del primer avión")

pasajerosavion1= input("elige la numero de pasajeros")

modeloavion1= input("elige el modelo")

coloravion1= input("elige  el color")

añoavion1= input("elige el año de salida")

print("Las caracteristicas del segundo avión son?")

pasajerosavion2= input("elige la numero de pasajeros")

modeloavion2= input("elige el modelo")

coloravion2= input("elige  el color")

añoavion2= input("elige el año de salida")

air1 = Airplane(pasajerosavion1,modeloavion1,coloravion1,añoavion1)
print(air1.show_attr())
air2 = Airplane(pasajerosavion2,modeloavion2,coloravion2,añoavion2)
print(air2.show_attr())



print("los vehiculos que registraste fueron:")

#carros seleccionados

print("Carros registrados")

print(car1.show_attr())

print(car2.show_attr())

#barcos seleccionados

print("Barcos registrados")

print(ship1.show_attr())

print(ship2.show_attr())

#aviones seleccionados

print("Aviones registrados")

print(air1.show_attr())

print(air2.show_attr())