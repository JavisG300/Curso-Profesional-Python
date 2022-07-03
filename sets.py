my_set1 = {1,2,3,4,5}
my_set2 = {3,4,5,6,7}

#Union
my_set3 = my_set1 | my_set2

#Interseccion
my_set4 = my_set1 & my_set2

#Diferencia
my_set5 = my_set1 - my_set2

#Diferencia simétrica
my_set6 = my_set1 ^ my_set2

print(f'Los sets son {my_set1} y {my_set2}')
print(f'La unión es {my_set3}')
print(f'La intersección es {my_set4}')
print(f'La diferencia A - B es {my_set5}')
print(f'La diferencia simétrica es {my_set6}')

