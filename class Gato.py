class Gato:
    def __init__(self, energia, hambre):
        self.energia = energia
        self.hambre = hambre
        print ('Se creo un gato')
 
    def tomar_leche(self, leche_en_litros):
        self.hambre += leche_en_litros
        print ('el gato toma su leche')
 
    def acariciar(self):
        print ('prrrrr...')
 
    def jugar(self):
        if self.energia <= 0 or self.hambre <=1:
            print ('el gato no quiero jugar')
        else:
            self.energia -=1
            self.hambre -= 2
            print ('al gato le encanta jugar')
 
    def dormir(self, horas):
        self.energia += horas
        print ('el gato tomo una siesta')



