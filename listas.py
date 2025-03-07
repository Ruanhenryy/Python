frutas = ['banana','acerola','mamão','caju','melancia','uva','abacaxi','amora','laranja']
print(frutas)

#ADICIONANDO ITENS A LISTA INFORMANDO O INDICE:
frutas.insert(1, 'melão')
print(frutas)

#ADICIONANDO ITENS NO FINAL DA LISTA:
frutas.append('graviola')
print(frutas)

#REMOVENDO ITENS:
frutas.remove('banana')
print(frutas)

#REMOVENDO ITENS IMFORMANDO SEU INDICE:
frutas.pop(4)
print(frutas)

#LIMPANDO A LISTA COMPLETA:
frutas.clear()
print(frutas)

#COPIANDO LISTA (DEIXANDO A LISTA ORIGINAL SEM ALTERAÇÕES):
carros = ['strada','king','hrv','hilux','corola','etios','sw4','cross']
copia_carros  = carros.copy()
copia_carros[0] = 'toro'
print(copia_carros)
print(carros)

#ADICIONANDO VÁRIOS ITENS NA LISTA:
carros.extend(['montana','montana','montana','chevete','saveiro','virtus'])
print(carros)

#CONTANDO QUANTOS ITENS IGUAIS TEM NA MESMA LISTA:
quantidade = carros.count('montana')
print("O carro montana aparece", quantidade ,"vezes")

#CONTANDO OCORRÊNCIAS DE CARACTERES EM UMA STRING ( Isso pode ser útil, por exemplo, quando precisamos analisar um texto e identificar quantas vezes uma determinada palavra ou letra aparece.):
texto = "Python é uma linguagem de programação muito popular e versátil"
quantidade = texto.count('a')
print("A letra 'a' aparece", quantidade, "vezes no texto.")