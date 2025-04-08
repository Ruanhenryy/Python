from smartphone.Smartphone import Smartphone;

class Xiomi(Smartphone):
    def __init__(self, marca, volume, bateria, armazenamento, ligado=False):
        super().__init__(marca, volume, bateria, armazenamento, ligado)
    
    def aumentarVolume(self):
        print(self.volume)
        super().aumentarVolume(10)
    
    def diminuirVolume(self):
        super().diminuirVolume(10)

    def tirarFoto(self):
        super().tirarFoto(5, 3)