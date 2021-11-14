from claseCuentaBancaria import cuentaBancaria


class APlazoFijo(cuentaBancaria):
    def __init__(self,id,titular,fecha,numeroCuenta,saldo,vencimiento):
        cuentaBancaria.__init__(self,id,titular,fecha,numeroCuenta,saldo)
        self.vencimiento=vencimiento

    def retirarDinero(self,dinero,fechaActual):
        if(fechaActual<self.vencimiento):
            dinero=dinero*1.05
        cuentaBancaria.retirarDinero(dinero)