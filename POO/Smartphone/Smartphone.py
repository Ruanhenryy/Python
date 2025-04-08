from abc import ABC, abstractmethod;

@abstractmethod
class Smartphone(ABC):
    
    def __init__(self, marca, volume, bateria, armazenamento, ligado=False):
        self.ligado = ligado
        self.marca = marca
        self.volume = volume
        self.bateria = bateria
        self.armazenamento = armazenamento
        self.musicaTocando = False
        self.modoAviao = False  
    
    def ligar(self):
        if self.ligado:
            print(f'{self.marca} Já está ligado!')
            return
        print(f'{self.marca} Está ligando')
        self.ligado = True
        pass
    
    def desligarLigar(self):
        if not self.ligado:
            print(f'{self.marca} Está desligado!')
            return
        print(f'{self.marca} Está desligando!')
        
    def aumentarVolume(self, volume):
        if self.volume < 100:
            self.volume += volume
        print(f'volume: {self.volume}%')
        
    def diminuirVolume(self, volume):
        if self.volume > 0:
            self.volume -= volume
        print(f'volume: {self.volume}%') 

    def Usarbateria(self, consumo):
        if self.bateria < 20:
            print(f'ATENÇÃO! Bateria baixa: {self.bateria}%')
        elif self.bateria > consumo:
            self.bateria -= consumo
            return True
        else:
            self.bateria = 0
            self.ligado = False
            return False
            
    def tirarFoto(self, bateria, armazenamento):
        if not self.ligado:
            print(f'{self.marca} Não pode tirar foto')
            return
        if (self.Usarbateria(bateria) and self.usarArmazenamento(armazenamento)):
            print(f'{self.marca} Está tirando foto...')
        else:
            print(f'{self.marca} Não consegue tirar foto!')
        
    def tocarMusica(self):
        if not self.ligado:
            print(f'{self.marca} Ele está desligado e não pode tocar música')
            return
        
        self.musicaTocando = True
        print(f'{self.marca} Começou a tocar música...')
        
    def ativarModoAviao(self):
        if not self.ligado:
            print(f'{self.marca} Está desligado e não pode ativar esse modo')
            return
        self.modoAviao = True
        print(f'{self.marca} Modo avião ativado!')
        
    def abrirAplicativo(self, app):
        if not self.ligado:
            print(f'{self.marca} Está desligado, não pode abrir nenhum {app}')
            return
        print(f'{self.marca} abriu {app}')
        
    def abrirNavegador(self):
        if self.modoAviao:
            print(f'{self.marca} Está com o modo avião ativado, não pode abrir o navegador')
            return
        print(f'{self.marca} Abriu o navegador')
        
    
    def usarArmazenamento(self, capacidade):
        if self.armazenamento > capacidade:
            self.armazenamento -= capacidade
            return True
        else:
            print(f'{self.marca} Está com o armazenamento cheio! Remova alguns arquivos.')
            return False
       
    def pararMusica(self):
        if not self.musicaTocando:
            print(f'{self.marca} não está tocando música!')
            return
        print(f'{self.marca} Parou de tocar música!')
        self.musicaTocando = False
        
    def fecharAplicativo(self, app):
        if not self.ligado:
            print(f'{self.marca} Está desligado e não pode fechar {app}')
            return
        print(f'{self.marca} fechou o {app}')


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

class Samsung(Smartphone):
    def __init__(self, marca, volume, bateria, armazenamento, ligado=False):
        super().__init__(marca, volume, bateria, armazenamento, ligado)
    
    def aumentarVolume(self):
        print(self.volume)
        super().aumentarVolume(10)
    
    def diminuirVolume(self):
        super().diminuirVolume(10)

    def tirarFoto(self):
        super().tirarFoto(8, 2)
    

marca = input("Digite a marca do seu celular: ")

if marca.upper() == "MOTOROLA":
    volume = 50 #volume inicial
    bateria = 90 #Bateria inicial em %
    armazenamento = 1 #Armazenamento em GB
    marca = Motorola(marca.upper(), volume, bateria, armazenamento)
elif marca.upper() == "IPHONE":
    volume = 40 #volume inicial
    bateria = 20 #Bateria inicial em %
    armazenamento = 512 #Armazenamento em GB
    marca = Iphone(marca.upper(), volume, bateria, armazenamento)  
elif marca.upper() == "XIOMI":
    volume = 80 #volume inicial
    bateria = 100 #Bateria inicial em %
    armazenamento = 256 #Armazenamento em GB
    marca = Xiomi(marca.upper(), volume, bateria, armazenamento)  
elif marca.upper() == "SAMSUNG":
    volume = 10 #volume inicial
    bateria = 50 #Bateria inicial em %
    armazenamento = 64 #Armazenamento em GB
    marca = Samsung(marca.upper(), volume, bateria, armazenamento) 

marca.ligar()
#marca.tirarFoto()
#marca.ativarModoAviao()
#marca.abrirNavegador()
marca.tocarMusica()
marca.pararMusica()