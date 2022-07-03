#Es un iterador que guarda los infinitos números de la serie Fibonacci
import time 

class FiboIter(): #Esta clase va a representar a los objetos de tipo iterador que voy a instanciar dentro del código

    #No se crea el método constructor dunder init porque no necesitará ningún atributo el objeto y se puede obviar
    
    def __iter__(self): #Necesita self para existir
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2 
            #self.n1 = self.n2
            #self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux #Esta linea es el sustituto para las dos anteriores
            self.counter += 1
            return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.1) #Es para pausar antes de cada impresion 
