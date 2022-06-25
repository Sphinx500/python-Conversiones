from random import choice


tupla=("123",215.89, 139,False,"datos",12345,"12.354",92374)

random_value = choice(tupla)

print("...................")
print("la tupla es: ", tupla)
print("...................")
print("el tipo de dato de cada elemento de la tupla es: ")
for dato in tupla:
    print(type(dato))
print("...................")
print("El valor aleatorio obtenido es: ", random_value)

try:
    afloat = float(random_value)
    print("Convertido a float: ", afloat)
    if (type(afloat) == float) == True:
        porcentaje = afloat * .16
        print("...................")
        print("El 16% es: ", porcentaje)
        lista_valor=list(tupla)
        lista_valor.append(porcentaje)
        print("la lista obtenida es: ", lista_valor)
    else:
        print("No convertido")
except:
    print("El valor no se puede convertir")
    lista_valor=list(tupla)
    print("se elimina el valor")
    lista_valor.remove(random_value)
    print("tupla original: ", tupla)
    print("la lista obtenida es: ", lista_valor)


# if (type(random_value) == float) == True or (type(random_value) == int) == True:
#     afloat = float(random_value)
#     print("Convertido a float: ", afloat)
#     porcentaje = afloat * .16
#     print("...................")
#     print("El 16% es: ", porcentaje)

# else:
#     print("El valor no se puede convertir")
#     lista_valor=list(tupla)
#     print("se elimina el valor")
#     lista_valor.remove(random_value)
#     print("tupla original: ", tupla)
#     print("la lista obtenida es: ", lista_valor)
