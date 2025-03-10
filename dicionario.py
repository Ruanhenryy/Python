carro = {
    'Modelo':'strada',
    'Cor':'branco',
    'Motor':'1.4 evo',
    'Ar-condicionado':True,
    'Tanque': '55 litros'
}

#MÉTODO UTILIZADO PARA COPIAR DICIONÁRIOS:
print("MÉTODO COPY:")

copiaCarro = carro.copy()
print('Dicionário copiado com sucesso!' , copiaCarro,'\n\n')

#RETORNA TODAS AS CHAVES DO DICIONÁRIO:
print("MÉTODO KEYS:")

print(carro.keys())
for chave in carro.keys():
    print(chave,'\n\n')

#RETORNA TODOS OS VALORES DO DICIONÁRIO:
print("MÉTODO VALUES:")

print(carro.values())
for valor in carro.values():
    print(valor,'\n\n')

#RETORNA TODAS AS CHAVES E OS VALORES:
print("MÉTODO ITEMS:")

print(carro.items(),'\n\n')
#UTILIZANDO UMA ESTRUTURA DE REPETIÇÃO PARA EXIBIR AS CHAVES E VALORES, O ELSE VAI RODAR A PARTIR DO MOMENTO QUE O LOOP FOR ENCERRADO:
print("MÉTODO ITEMS COM UMA ESTRUTURA DE REPETIÇÃO PARA EXIBIR AS CHAVES E VALORES:\n")

for chave , valor in carro.items():
    print(chave, '->' , valor)

else:
    print("Todos os itens foram percorridos!")

print('\n\n')
#CHECANDO SE EXISTE UMA CHAVE JÁ EXISTENTE:
print("CHECANDO SE EXISTE UMA CHAVE JÁ EXISTENTE:")

chave = 'Tanque'

if chave in carro:
    print(f'Essa chave já existe no dicionário e seu valor é: {carro["Tanque"]}\n\n')
else:
    print('Essa chave não existe\n\n')

#ADICIONANDO ELEMENTOS DO DICIONÁRIO:
print("MÉTODO UPDATE ADICIONANDO ELEMENTOS DO DICIONÁRIO:")

carro.update(Marca='toyota')
print(carro,'\n\n')

#ATUALIZANDO ELEMENTOS DO DICIONÁRIO:
print("MÉTODO UPDATE ATUALIZANDO ELEMENTOS DO DICIONÁRIO:")

carro.update(Modelo='hilux', Cor='prata', Tanque='80 litros')
print(carro,'\n\n')

#ESSE MÉTODO RETORNA O VALOR DO ITEM DA CHAVE QUE FOR ESPECÍFICADA, E CASO NÃO EXISTA A CHAVE, PASSE O NOME DA CHAVE E O VALOR PARA QUE SEJA CRIADO UM NOVO PAR CHAVE-VALOR:
print('MÉTODO SETDEFAULT')

marca = carro.setdefault('Marca')
print(marca)
carro.setdefault('Assento', 'couro')
print(carro,'\n\n')


#O MÉTODO GET() RETORNA O VALOR ASSOCIADO A UMA CHAVE ESPECÍFIFA:
print('MÉTODO GET')

ArCondicionado = carro.get('Ar-condicionado')
if ArCondicionado == True:
    print("O carro possui Ar-condicionado\n\n")
else:
    print("o carro não possui Ar-condicionado\n\n")

#REMOVENDO ELEMENTOS DO DICIONÁRIO:
print('MÉTODO POP')

carro.pop('Cor')
print(carro,'\n\n')

#ESSE MÉTODO  RETORNA UM DICIONÁRIO COM CHAVES E VALORES ESPECÍFICADOS:
print('MÉTODO FROMKEYS')

novasChaves = ('Computador','Carro','Camisa','Bermuda')
cor = "Azul"
novoDicionario = carro.fromkeys(novasChaves, cor)
print(novoDicionario,'\n\n')

#O MÉTODO POPITEM() ELE REMOVE E RETORNA O ÚLTIMO PAR CHAVE-VALOR DO DICIONÁRIO:
print('MÉTODO POPITEM')

print(carro.popitem())
print(carro,'\n\n')

#ESSE MÉTODO APAGA O  DICIONÁRIO POR COMPLETO:
print('MÉTODO CLEAR')

carro.clear()
print(carro,'\n\n')

#ATUALIZANDO O DICIONÁRIO COM ELEMENTOS DE UM OUTRO DICIONÁRIO:
print('MÉTODO UPDATE ATUALIZANDO O DICIONÁRIO COM ELEMENTOS DE UM OUTRO DICIONÁRIO:')

moto = {
    'Modelo':'Pop 110i',
    'Cor':'branco',
    'Motor':'110 cc',
    'Partida elétrica': True,
    'Tanque':'15 litros'
}
carro.update(moto)
print(carro)