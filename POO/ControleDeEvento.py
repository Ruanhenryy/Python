class Evento:
    def __init__(self, nome, data, quantidadeDeParticipantes):
        self.nome = nome
        self.data = data
        self.quantidadeDeParticipantes = quantidadeDeParticipantes

    def adicionarParticipante(self):
        quantidadeDeParticipantes += 1
        print(f'Novo participante adicionado com sucesso! Agora o evento tem {self.quantidadeDeParticipantes} participantes')

    def adicionarParticipante(self):
        quantidadeDeParticipantes -= 1
        print(f'Participante excluido com sucesso! Agora o evento tem {self.quantidadeDeParticipantes} participantes')