"""Ejercicio 09 - Cuenta bancaria"""

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular, self.saldo = titular, saldo

    # Solo acepta montos mayores que cero
    def depositar(self, monto):
        if monto <= 0:
            print("Depósito de S/ {} rechazado: monto inválido".format(monto))
        else:
            self.saldo += monto
            print("Depósito de S/ {} realizado".format(monto))

    # Rechaza montos inválidos o mayores al saldo
    def retirar(self, monto):
        if monto <= 0:
            print("Retiro de S/ {} rechazado: monto inválido".format(monto))
        elif monto > self.saldo:
            print("Retiro de S/ {} rechazado: saldo insuficiente".format(monto))
        else:
            self.saldo -= monto
            print("Retiro de S/ {} realizado".format(monto))

    def mostrar_saldo(self):
        print("Saldo de {}: S/ {:.2f}".format(self.titular, self.saldo))

cuenta = CuentaBancaria("Carlos Ramírez", 800)
for monto in (200, 150, 100, -50):
    cuenta.depositar(monto)
for monto in (300, 2000, 0):
    cuenta.retirar(monto)
cuenta.mostrar_saldo()
