import random

attemps = 0
guessed = False


difficulty = int(input(f"----- ADIVINA EL NUMERO -----\nElige la dificultad: \n1. Facil \n2. Medio \n3. Dificil \n4. Salir\n-----\n"))

if difficulty == 1:
    secret_number = random.randint(1,50)
                
    while not guessed:
        attemps += 1
        

        try:
            attemp = int(input("\nIngresa tu intento: "))
        
            if attemps < 1 or attemps > 50:
                print("Por favor, ingrese un numero del 1 al 50.")
                attemps -= 1

            if attemp < secret_number:
                print("Demasiado bajo. Intenta un numero mas alto.")

            elif attemp > secret_number:
                print("Demasiado alto. Intenta un numero mas bajo.")

            else:
                guessed = True
                print(f"\nFelicidades, Adivinaste el numero {secret_number}!!!")
                print(f"Lo lograste en: {attemps} intentos.")

        except ValueError:
            print("Por favor, ingresa un numero valido.")
            attemps -= 1


elif difficulty == 2:
    secret_number = random.randint(1,100)
    print("----- ADIVINA EL NUMERO -----\nEl número esta entre 1 y 100.")

    while not guessed:
        attemps += 1

        try:
            attemp = int(input("\nIngresa tu intento: "))

            if attemps < 1 or attemps > 100:
                print("Por favor, ingrese un numero del 1 al 100.")
                attemps -= 1

            if attemp < secret_number:
                print("Demasiado bajo. Intenta un numero mas alto.")
            elif attemp > secret_number:
                print("Demasiado alto. Intenta un numero mas bajo.")

            else:
                guessed = True
                print(f"\nFelicidades, Adivinaste el numero {secret_number}!!!")
                print(f"Lo lograste en: {attemps} intentos.")

        except ValueError:
                print("Por favor, ingresa un numero valido.")
                attemps -= 1

elif difficulty == 3:
    secret_number = random.randint(1,200)
    print("----- ADIVINA EL NUMERO -----\nEl número esta entre 1 y 100.")

    while not guessed:
        attemps += 1

        try:
            attemp = int(input("\nIngresa tu intento: "))

            if attemps < 1 or attemps > 200:
                print("Por favor, ingrese un numero del 1 al 200.")
                attemps -= 1

            if attemp < secret_number:
                print("Demasiado bajo. Intenta un numero mas alto.")               
            elif attemp > secret_number:
                print("Demasiado alto. Intenta un numero mas bajo.")

            else:
                guessed = True
                print(f"\nFelicidades, Adivinaste el numero {secret_number}!!!")
                print(f"Lo lograste en: {attemps} intentos.")

        except ValueError:
                print("Por favor, ingresa un numero valido.")
                attemps -= 1

elif difficulty == 4:
    print("Gracias por jugar!!  :DDD")
    i = 0
    while i == 1:
        break
