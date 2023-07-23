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
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.cuenta = CuentaBancaria(tasa_interés=0.02, balance=0)
        
    def hacer_depósito(self, amount):
        self.cuenta.depósito(amount)

    def hacer_retiro(self, amount):
        self.cuenta.retiro(amount)

    def mostrar_balance_usuario(self):
        print(f"Balance de {self.nombre}:")
        self.cuenta.mostrar_info_cuenta()


