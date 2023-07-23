class CuentaBancaria:
    cuentas = []  # Lista para almacenar todas las instancias de cuentas creadas

    def __init__(self, balance, tasa_interés=5):
        self.balance = balance
        self.tasa_interés = tasa_interés
        CuentaBancaria.cuentas.append(self)
    def depósito(self, amount):
        self.balance += amount
        return self
    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes")
            self.balance -= 5  # Se cobra una tarifa de $5
            print("Se ha cobrado una tarifa de $5")
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance de cuenta: ${self.balance:.2f}")
        return self
    def generar_interés(self):
        if self.balance > 0:
            interes= self.balance* (self.tasa_interés/100)
            self.balance += interes
        return self
    
    @classmethod
    def imprimir_info_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()
# Crear la primera cuenta y realizar operaciones en una línea
cuenta1 = CuentaBancaria(1000).depósito(500).depósito(200).depósito(300).retiro(400).generar_interés()

# Crear la segunda cuenta y realizar operaciones en una línea
cuenta2 = CuentaBancaria(100).depósito(50).depósito(300).retiro(200).retiro(100).retiro(50).retiro(50).generar_interés()

# Imprimir información de todas las cuentas
CuentaBancaria.imprimir_info_cuentas()
