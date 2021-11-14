import random

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

    def cuenta(self):
        return "Cuenta bancaria: " + str(self.id) + " Saldo: " + str(self.saldo)


def crearNumeroCuenta():
    numero=0
    for i in range(0,13):
        num=random.randint(0,9)
        numero+=num*10^i
    return numero

def esBisiesto(año):
    bisiesto=False
    if(año%4==0):
        if(año%100==0):
            if(año%400==0):
                bisiesto=True
        else:
            bisiesto=True
    return bisiesto

def escribirfecha():
    año=random.randint(2021,2070)
    mes=random.randint(1,12)
    día=0
    if(mes==2):
        if(esBisiesto(año)==True):
            día=random.randint(1,29)
        else:
            día=random.randint(1,28)
    elif(mes==4 or mes==6 or mes==9 or mes==11):
        día=random.randint(1,30)
    else:
        día=random.randint(1,31)
    fecha=[año,mes,día]
    return fecha


def compararfechas(fecha1,fecha2):
    fecha3=fechamenor(fecha1,fecha2)
    if(fecha1!=fecha3):
        return 1
    elif(fecha2!=fecha3):
        return -1
    else:
        return 0

def fechamenor(fecha1,fecha2):
    if(fecha1[0]>fecha2[0]):
        mayor=fecha1
        menor=fecha2
    elif(fecha1[0]<fecha2[0]):
        mayor=fecha2
        menor=fecha1
    else:
        if(fecha1[1]>fecha2[1]):
            mayor=fecha1
            menor=fecha2
        elif(fecha1[1]<fecha2[1]):
            mayor=fecha2
            menor=fecha1
        else:
            if(fecha1[2]>fecha2[2]):
                mayor=fecha1
                menor=fecha2
            elif(fecha1[2]<fecha2[2]):
                mayor=fecha2
                menor=fecha1
            else:
                mayor=fecha1
                menor=fecha2
    return menor