class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def informacaoPersonagem(self): #Definindo a função com as informações gerais independente do personagem.
        print(f'Informações do personagem {self.nome}, Nével {self.nivel}:')
    
class Cavalheiro(Personagem):
    def informacaoPersonagem(self, habilidade, pontosDeVida, fraqueza):
        super().informacaoPersonagem()#Chamando uma função da SUPERclasse personagem para sobre-escrever
        print(f'Seu personagem ele é do tipo cavalheiro! Sua habilidade é {habilidade} e tem {pontosDeVida} pontos de vida e sua fraqueza é {fraqueza}.\n')


class Mago(Personagem):
    def informacaoPersonagem(self, habilidade, pontosDeVida, fraqueza):
        super().informacaoPersonagem()#Chamando uma função da SUPERclasse personagem para sobre-escrever
        print(f'Seu personagem ele é tipo Mago! Sua habilidade é {habilidade} e tem {pontosDeVida} pontos de vida e sua fraqueza é {fraqueza}.\n')

cavalheiro1 = Cavalheiro("Valdemar", 5)
cavalheiro1.informacaoPersonagem("Força", 1000, "Magia")

mago1 = Mago("Ronaldo", 15)
mago1.informacaoPersonagem("Magia", 1500, "Lutador")