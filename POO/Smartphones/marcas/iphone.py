from smartphone.Smartphone import Smartphone;

class Iphone(Smartphone):
    def __init__(self, marca, volume, bateria, armazenamento, ligado=False):
        super().__init__(marca, volume, bateria, armazenamento, ligado)
    
    def aumentarVolume(self):
        print(self.volume)
        super().aumentarVolume(5)
    
    def diminuirVolume(self):
        super().diminuirVolume(5)

    def tirarFoto(self):
        super().tirarFoto(20, 4)