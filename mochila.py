class Mochila:
    def __init__(self, peso, valor, indice):
        self.indice = indice
        self.peso = peso
        self.valor = valor 
        self.report = valor//peso 
        #Esta función serviría para comparar 2 mochilas.

#Obtenemos el ratio calculado para ordenadarlo todo
    def __it__ (self, otro):
        return self.report < otro

def obtenerMaxValor (peso, valores, capacidad):
    arraySort = []
    for i in range (len(peso)):
        arraySort.append(Mochila(peso[i],valores[i],i))
    
    #Ordena los elementos de la bolsa
    arraySort.sort (reverse=True)

    counterValue = 0
    for object in arraySort:
        pesoactual = int(object.peso)
        valoractual = int(object.valor)
        if capacidad - pesoactual >= 0:
            #agregamos el objeto en la bolsa y restamos la capacidad
            capacidad -= pesoactual
            counterValue += valoractual
            
            #agregamos ese valor en la bolsa
            return counterValue
        
peso = [1,5,3,2,4]
valores = [10,50,20,30,60]
capacidad = 11
Maxvalor = obtenerMaxValor(peso,valores, capacidad)
print("El valor máximo en la mochila es =", Maxvalor)

