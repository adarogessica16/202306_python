class Usuario:	
    def __init__(self, nombre, email, balance_cuenta=0):
        self.nombre = nombre
        self.email = email
        self.balance_cuenta = balance_cuenta

    # agregando el método de depósito
    def hacer_depósito(self, monto):	
        self.balance_cuenta += monto	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        return self
    def hacer_retiro(self, monto):
        self.balance_cuenta -= monto
        return self
    def mostrar_balance_usuario(self):
        print(f"Balance de {self.nombre}: ${self.balance_cuenta:.2f}")
        return self
    
    def transferir(self, usuarioDestino, monto):
        if monto<= self.balance_cuenta:
            self.balance_cuenta-= monto
            usuarioDestino.hacer_depósito(monto)
            print(f"Transferencia exitosa. {self.nombre} ha transferido ${monto:.2f} a {usuarioDestino.nombre}.")
        else:
            print("No se pudo hacer la transferencia")
        return self

Usuario1= Usuario("Gessica", "adarogessia")
Usuario2= Usuario("Jose", "adarogia")
Usuario3= Usuario("Jazz", "@@@")
Usuario1.hacer_depósito(500).hacer_depósito(100).hacer_depósito(50).mostrar_balance_usuario().transferir(Usuario2, 400).mostrar_balance_usuario()
Usuario2.mostrar_balance_usuario()
Usuario3.hacer_depósito(1000).hacer_retiro(500).mostrar_balance_usuario()