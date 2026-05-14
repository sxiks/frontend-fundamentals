balance = 0.0
transactions = []

print(" ")
print("----- Bienvenida al banco simple -----")

while True:

    option = int(input(f"--------------------\nQue deseas hacer: \n" "\n1. Depositar \n2. Retirar \n3. Consultar saldo \n4. Ver transacciones \n5. Salir\n" "\n--------------------\nElige una opcion: "))

    try:
        option = int(option)
        print(" ")
    except ValueError:
         print("Error: Igresa un numero numero valido (1-5). ")
         continue
    
    if option == 1:
        try:
            amount = float(input("Monto a depositar: "))
            if amount <= 0:
                 print("Error: El monto debe ser positivo. ")
            else:
                 balance += amount
                 transactions.append(f"Depositaste ${amount:.2f}. Saldo: ${balance:.2f}")
                 print(f"Deposito exitoso. Saldo actual: ${balance:.2f}")
                 print(" ")
        except ValueError:
             print("Error: Igresa un numero numero valido. ")

    if option == 2:
        try:
            amount = float(input("Monto a retirar: "))
            if amount <= 0:
                 print("Error: El monto debe ser positivo. ")

            elif amount > balance:
                 print("Error: Saldo insifuciente")
            else:
                 balance -= amount
                 transactions.append(f"Retiraste ${amount:.2f}. Saldo: ${balance:.2f}")
                 print(f"Retiro exitoso. Saldo actual: ${balance:.2f}")
                 print(" ")
        except ValueError:
             print("Error: Igresa un numero numero valido. ")

    if option == 3:
         print(f"Saldo actual: ${balance:.2f}")
         print(" ")

    elif option == 4:
        if not transactions:
              print("No hay transacciones registradas.")
              print(" ")
        else:
             print("Historial de transacciones: ")
             for i, f in enumerate (transactions, 1):
                  print(f"{i}. {f}")
                  print(" ")

    if option == 5:
        print(f"Gracias por usar Banco Simple. Saldo final: ${balance:.2f}")
        break