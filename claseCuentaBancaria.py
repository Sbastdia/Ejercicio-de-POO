class cuentaBancaria:

    def __init__(self,id,titular,fecha,numeroCuenta,saldo):
        self.id=id
        self.titular=titular
        self.fecha=fecha
        self.numeroCuenta=numeroCuenta
        self.saldo=saldo


    def setid(self,id):
        self.id=id

    def setTitular(self,titular):
        self.titular=titular

    def setFecha(self,fecha):
        self.fecha=fecha

    def setNumeroCuenta(self,numeroCuenta):
        self.numeroCuenta=numeroCuenta

    def setSaldo(self,saldo):
        self.saldo=saldo

    def getid(self):
        return self.id

    def getTitular(self):
        return self.titular

    def getFecha(self):
        return self.fecha

    def getNumeroCuenta(self):
        return self.numeroCuenta

    def getSaldo(self):
        return self.saldo

    def retirarDinero(self,dinero):
        if (self.saldo>=dinero):
            self.saldo=self.saldo-dinero
        else:
            print('Quieres retirar más dinero del que tienes')

    def ingresarDinero(self, dinero):
        self.saldo=self.saldo+dinero

    def transferirDinero(self,dinero,cuentaATransferir):
        if (self.saldo>=dinero):
            self.saldo=self.saldo-dinero
            cuentaATransferir.saldo=cuentaATransferir.saldo+dinero
        else:
            print('Quieres transferir más dinero del que tienes')