from datetime import datetime


def execution_time(func): #This function measures the time it takes to execute a function
    def wrapper(*args, **kargs):
        initial_time = datetime.now()
        func(*args, **kargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,100000000): #The underscore is due to we don't care the variable of each round 
        pass

@execution_time
def suma(a: int, b:int) -> int:
    return a + b

@execution_time
def saludo(nombre = "Javier"):
    print(f"Hola {nombre}")
suma(5, 5)
random_func()
saludo("Emanuel")

