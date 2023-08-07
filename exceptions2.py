fruits = ["manzanas","banana","perá","sandia","fresas"]

while True:
    user_option = input("Ingrese un número entre 0 y 4 para elegir tu fruta, q para salir: ")
    if (user_option == "q"):
        break
    try:
        print(fruits[int(user_option)])
    except IndexError:
        print("NO! ingresa un número del 0 al 5") 
    except ValueError as valueerror:
        print("Por favor ingresa un número no una letra",valueerror)    
        
