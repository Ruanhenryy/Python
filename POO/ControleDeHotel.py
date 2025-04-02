class Hotel:
    def __init__(self):
        ...

    def resevar(self):
        print('Reserva concluida com sucesso!')

    def cancelar(self):
        print('Reserva concluido com sucesso!')

class Quarto(Hotel):
    
    def __init__(self, numero, tipo, ocupado=False):
        self.ocupado = ocupado
        self.numero = numero
        self.tipo = tipo     

    def resevar(self):

        if self.tipo == "simples":
            print("Os quartos tipo simples possui cama de solteiro, televisão, ar-condicionado e frigobar")
        elif self.tipo == "duplo":
            print("Os quartos tipo duplo possui, duas camas de solteiro, televisão, ar-condicionado e frigobar")
        elif self.tipo == "suite":
            print("Os quartos tipo suite possui, cama de casal, televisão, ar-condicionado, frigobar e banheira")

        if self.ocupado:
            print(f'O quarto número {self.numero} do tipo {self.tipo} está ocupado no momento, reserve outro modelo quarto!')
            return
        print(f'Reservando quarto número {self.numero} do tipo {self.tipo} ...')
        super().resevar()
        self.ocupado = True
    
    def cancelar(self):
        if not self.ocupado:
            print(f'O quarto número {self.numero} tipo {self.tipo} não tem reserva!')
        print(f'Cancelando reserva do quarto número {self.numero} tipo {self.tipo} ...')
        super().cancelar()
        self.ocupado = False


q1 = Quarto(1 , "simples")
q1.resevar()
q1.resevar()

q2 = Quarto(2 , "simples")
q2.resevar()

"""q3 = Quarto(3 , "duplo")
q3.resevar()

q4 = Quarto(4 , "suite")
q4.resevar()

q5 = Quarto(5 , "duplo")
q5.cancelar()

q6 = Quarto(6 , "suite")
q6.resevar()
q6.cancelar()
q6.cancelar()

q7 = Quarto(7 , "suite")
q7.resevar()
q7.resevar()
q7.cancelar()
q7.cancelar()"""

