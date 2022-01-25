from asyncio.windows_events import NULL
from datetime import datetime, date


class Transacao:
    def __init__(self, id, valorTransacao, estabelecimento, unidadeGestora, mesExtrato, portador, dataTransacao):
        self.id = id
        self.valorTransacao = float(valorTransacao.replace('-', '').replace('.', '').replace(',', '.'))
        self.estabelecimento = estabelecimento
        self.unidadeGestora= unidadeGestora
        self.mesExtrato = datetime.strptime(mesExtrato, '%m/%Y').date().strftime('%Y/%m/%d')
        self.portador = portador
        self.dataTransacao = setDataTransacao(dataTransacao)


def setDataTransacao(data):
    return NULL if data == 'Sem informação' else datetime.strptime(data, '%d/%m/%Y').date().strftime('%Y/%m/%d')