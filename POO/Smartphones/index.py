from marcas.motorola import Motorola;
from marcas.iphone import Iphone;
from marcas.samsung import Samsung;
from marcas.xiomi import Xiomi;

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