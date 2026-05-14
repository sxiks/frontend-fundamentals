class CuentaBancaria:
    # Constructor - inicializa el objeto con sus atributos
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero          # Atributo: número de cuenta
        self.titular = titular        # Atributo: nombre del titular
        self.saldo = saldo            # Atributo: saldo actual
        self.activa = True            # Atributo: estado de la cuenta
    
    # Métodos - definen el comportamiento del objeto
    def depositar(self, cantidad):
        if not self.activa:
            return "Cuenta inactiva. Operación cancelada."
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self.saldo}"
        else:
            return "La cantidad debe ser positiva."
    
    def retirar(self, cantidad):
        if not self.activa:
            return "Cuenta inactiva. Operación cancelada."
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                return f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self.saldo}"
            else:
                return "Saldo insuficiente."
        else:
            return "La cantidad debe ser positiva."
    
    def consultar_saldo(self):
        if not self.activa:
            return "Cuenta inactiva."
        return f"Saldo actual: ${self.saldo}"
    
    def cerrar_cuenta(self):
        self.activa = False
        return "Cuenta cerrada correctamente."


# Creamos dos cuentas bancarias (dos objetos de la misma clase)
cuenta_ana = CuentaBancaria("123456", "Ana García", 1000)
cuenta_luis = CuentaBancaria("789012", "Luis Pérez")

# Interactuamos con la cuenta de Ana
print(cuenta_ana.consultar_saldo())  # Saldo actual: $1000
print(cuenta_ana.depositar(500))     # Depósito de $500 realizado. Nuevo saldo: $1500
print(cuenta_ana.retirar(200))       # Retiro de $200 realizado. Nuevo saldo: $1300

# Interactuamos con la cuenta de Luis
print(cuenta_luis.consultar_saldo()) # Saldo actual: $0
print(cuenta_luis.depositar(100))    # Depósito de $100 realizado. Nuevo saldo: $100