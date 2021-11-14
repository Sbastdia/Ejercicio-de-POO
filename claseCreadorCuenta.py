from claseAPlazoFijo import APlazoFijo
from claseCuentaBancaria import cuentaBancaria
from claseVIP import VIP
import random

class CreadorCuenta():
    __id=1

    def __init__(self, tipoCuenta,titular):
        self.cuenta = None
        fecha1=cuentaBancaria.escribirfecha()
        fecha2=cuentaBancaria.escribirfecha()
        self.fecha=cuentaBancaria.fechamenor(fecha1,fecha2)
        if(self.fecha==fecha1):
            self.vencimiento=fecha2
        else:
            self.vencimiento=fecha1
        self.numerocuenta=cuentaBancaria.crearNumeroCuenta()
        self.saldo=10000
        self.negativo=random.randint(1,self.saldo/8)
        if(tipoCuenta=="CuentaBancaria"):
            self.cuenta=cuentaBancaria.CuentaBancaria(CreadorCuenta.__id,titular,self.fecha,self.numerocuenta,self.saldo)
        elif(tipoCuenta=="APlazoFijo"):
            self.cuenta=APlazoFijo(CreadorCuenta.__id,titular,self.fecha,self.numerocuenta,self.saldo,self.vencimiento)
        elif(tipoCuenta=="VIP"):
            self.cuenta=VIP(CreadorCuenta.__id,titular,self.fecha,self.numerocuenta,self.saldo,self.negativo)
        CreadorCuenta.__id+=1



if __name__ == '__main__':
    Cuenta1=CreadorCuenta("CuentaBancaria","Laura")
    Cuenta2=CreadorCuenta("APlazoFijo","José")
    Cuenta3=CreadorCuenta("VIP","María")

    print(Cuenta1.cuenta.cuenta())
    print(Cuenta2.cuenta.cuenta())
    print(Cuenta3.cuenta.cuenta())

    Cuenta1.cuenta.transferirdinero(2000,Cuenta2.cuenta)
    Cuenta2.cuenta.transferirdinero(2000,Cuenta3.cuenta)

    Cuenta1.cuenta.ingresardinero(575)
    Cuenta2.cuenta.ingresardinero(575)
    Cuenta3.cuenta.ingresardinero(575)
    Cuenta1.cuenta.retirardinero(78)

    print("El saldo de la cuenta 1 es: "+str(Cuenta1.cuenta.getsaldo()))
    print("El saldo de la cuenta 2 es: "+str(Cuenta2.cuenta.getsaldo()))
    print("El saldo de la cuenta 3 es: "+str(Cuenta3.cuenta.getsaldo()))

