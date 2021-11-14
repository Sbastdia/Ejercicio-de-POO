from claseCuentaBancaria import cuentaBancaria


class VIP(cuentaBancaria):
    def __init__(self,id,titular,fecha,numeroCuenta,saldo,negativo):
        cuentaBancaria.__init__(self,id,titular,fecha,numeroCuenta,saldo)
        self.negativo=negativo

    def retirarDinero(self,dinero):
        if(self.saldo+self.negativo>=dinero):
            self.saldo=self.saldo-dinero
        else:
            print('El dinero a retirar está fuera de tu limite')

    def transferirDinero(self,dinero,cuentaATransferir):
        if (self.saldo+self.negativo>=dinero):
            self.saldo=self.saldo-dinero
            cuentaATransferir.saldo=cuentaATransferir.saldo+dinero
        else:
            print('El dinero a transferir está fuera de tu limite')