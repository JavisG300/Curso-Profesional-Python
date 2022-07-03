#Los closures deben cumplir 3 características
#   Debemos tener una nested function
# 	La nested function debe referenciar un valor de un scope superior
# 	La función que envuelve a la nested function debe retornarla también

def make_repeater_of(n): #Será un repetidor de n veces
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater

def main():
    repeat_5 = make_repeater_of(5) #Lo que ocurre aquí es que se regresa una funcion de tipo repeater y se guarda n = 5
    print(repeat_5("Hola"))    

    repeat_10 = make_repeater_of(10)
    print(repeat_10("Javs"))

if __name__ == "__main__":
    main()


