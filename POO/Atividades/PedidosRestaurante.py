class Restaurante:
    def __init__(self):
        self.quantidadeDePedidos = 0


    def adicionarPedido(self):
        self.quantidadeDePedidos += 1
        print(f'Pedido número: {self.quantidadeDePedidos}, da fila!')

class Pedido(Restaurante):
    def adicionarPedido(self, item, quantidade, valorTotal):
        print(f'O pedido de {quantidade} unidade(s) de {item} no valor de R${valorTotal},foi adicionado com sucesso.')
        return super().adicionarPedido()
    
pd = Pedido()
pd.adicionarPedido("Lagosta", 2, 300)
pd.adicionarPedido("Pastel", 3, 30)
pd.adicionarPedido("Coca", 1, 15)
pd.adicionarPedido("Camarão", 1, 60)