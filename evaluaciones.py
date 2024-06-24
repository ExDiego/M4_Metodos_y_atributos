from pizza import Pizza
from clear import limpiar

limpiar()

#a

print("** ATRIBUTOS DE LA CLASE PIZZA **\n")
print(f"1. Lista de proteinas : {Pizza.proteinas}")
print(f"2. Lista de vegetales : {Pizza.vegetales}")
print(f"3. Lista de masas : {Pizza.masas}")
print(f"4. Tamaño de la Pizza : {Pizza.tamano}")
print(f"5. Precio : {Pizza.precio}")


#b

salsa = Pizza.validar_elementos("salsa de tomate", ["salsa de tomate", "salsa bbq"])

print(f'\n\nSalsa de Tomate es una salsa válida:   {"Sí" if salsa else "No"}.\n')

#c

mi_pizza = Pizza()
mi_pizza.tomar_pedido()

#d

print(f'\n¿Esta es una pizza válida? {"Sí" if mi_pizza.es_valida else "no"}\n')

#e

print(f'La clase Pizza es válida? {"Sí" if Pizza.es_valida else "No"}.') #classe Pizza da error, cambiar por variable mi_pizza para que no de erorr