# POLIFORMISMO ESTÁ FORTEMENTE LIGADO A HERANÇA E A ABSTRAÇÃO !!!!!

# POLIMORFISMO DE SOBRECARGA:

# O POLIMORFISMO DE SOBRECARGA É A DEFINIÇÃO DE MAIS DE UMA FUNÇÃO COM O MESMO NOME, MAS COM ARGUMENTOS DIFERENTES!
# NO PYTHON NÃO EXISTE A SOBRECARGA, POIS O MÉTODO MAIS RECENTE É O QUE SERÁ UTILIZADO.

'''class Calculadora:
    def __init__(self):
        pass
    
    def somar(self, *args):
        print(sum(args))
    
    #def somar(self, numero1, numero2):
       #print(numero1+numero2)

calculadora = Calculadora()

# PODEMOS FAZER COM QUE NOSSO MÉTODO EM PYTHON TENHAM AS MESMAS CARACTERISTICAS DE UM MÉTODO SOBRECARREGADO, DEFININDO UM MÉTODO QUE TENHA MAIS DE UMA FORMA DE LHE CHAMAR.

calculadora.somar(1 , 20, 100,100,200)
calculadora.somar(100, 100,200)
calculadora.somar(100,200)'''


# POLIMORFISMO DE SOBRE-ESCRITA:

# O POLIMORFISMO DE SOBRE-ESCRITA É A DEFINIÇÃO DE UM MÉTODO NA CLASSE FILHA COM O MESMO NOME DO MÉTODO DA CLASSE PAI MAS COM AÇÕES DIFERENTES.

# UTILIZAMOS O PILAR DE ABSTRAÇÃO PARA QUE POSSAMOS PASSAR MÉTODOS SEM CORPO(SEM BLOCO DE CÓDIGO) NA CLASSE PAI, PARA QUE PODEMOS DEFINIR SEU CORPO NAS CLASSES FILHAS!

from abc import ABC, abstractmethod;

@abstractmethod
class Veiculo(ABC):
    def __init__(self,marca):
        self.velocidade = 0
        self.marca = marca
        self.aumentarVelocidade = 0

    def ligar(self):
        print("Conferir se tem combustivel")
        print("Ligar veiculo \n")
    
    def acelerar(self):
        pass

class Carro(Veiculo):
    def __init__(self, marca):
        super().__init__(marca)
        self.aumentarVelocidade = 30

    def ligar(self):
        print("Conferir se está em P")
        return super().ligar()

    def acelerar(self):
        self.velocidade += self.aumentarVelocidade
        print(f'{self.marca} Está a {self.velocidade}Km/h\n')

class Moto(Veiculo):
    def __init__(self, marca):
        super().__init__(marca)
        self.aumentarVelocidade = 15

    def ligar(self):
        print("Conferir se está em Neutro")
        return super().ligar()

    def acelerar(self):
        self.velocidade += self.aumentarVelocidade
        print(f'{self.marca} Está a {self.velocidade}Km/h \n')

carro = Carro("Audi")

carro.ligar()

carro.acelerar()
carro.acelerar()
carro.acelerar()

moto = Moto("XRE")

moto.ligar()

moto.acelerar()
moto.acelerar()
moto.acelerar()