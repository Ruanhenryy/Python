from smartphone.Smartphone import Smartphone;

class Motorola(Smartphone):
    def __init__(self, marca, volume, bateria, armazenamento, ligado=False):
        super().__init__(marca, volume, bateria, armazenamento, ligado)
    
    def aumentarVolume(self):
        print(self.volume)
        super().aumentarVolume(20)
    
    def diminuirVolume(self):
        super().diminuirVolume(20)

    def tirarFoto(self):
        super().tirarFoto(10, 2)