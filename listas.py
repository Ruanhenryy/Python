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

#INVERTENDO OS ITENS DA LISTA:
carros.reverse()
print(carros)

#PROCURANDO O INDICE ONDE O ITEM QUE ESTAMOS PROCURANDO ESTÁ (OBS: ELE VAI INFORMAR O  INDICE DO PRIMEIRO ITEM DO MESMO VALOR):
print("O indice do carro 'saveiro' é",carros.index('saveiro'),"na lista!")

#PROCURANDO O INDICE ONDE O ITEM QUE ESTAMOS PROCURANDO ESTÁ EM UM INTERVALO DE INDICES( .INDEX(ITEM, INDICE INICIAL,  INDICEFINAL))
print("O indice do carro 'sw4' é",carros.index('sw4',1,8),"na lista!")

#ORDENANDO OS ITENS DA LISTA (OBS: TODOS OS ELEMENTOS TEM QUE SER DO MESMO TIPO  COMO EXEMPLO ABAIXO STRING)
compras = ['arroz','feijão','batata','leite','carne','macarrão','sardinha','mateiga','papel']
compras.sort()
print(compras)

#ORDENANDO OS ITENS DA LISTA NA ORDEM DECRESCENTE PASSANDO O PARAMETRO REVERSE=TRUE (OBS: TODOS OS ELEMENTOS TEM QUE SER DO MESMO TIPO  COMO EXEMPLO ABAIXO STRING)
compras.sort(reverse=True)
print(compras)