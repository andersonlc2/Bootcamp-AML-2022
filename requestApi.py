from logging import exception
import requests
from datetime import datetime, timedelta, date
from entities.OrgaoMaximo import OrgaoMaximo
from entities.Estabelecimento import Estabelecimento
from entities.Portador import Portador
from entities.Transacao import Transacao
from entities.UnidadeGestora import UnidadeGestora
from Connection import Connection
from Control import saveOrgao
from Control import saveUnidadeGestora
from Control import savePortador
from Control import saveEstabelecimento
from Control import saveTransacao
from Control import getIdPortador


data = Connection.data_connection
cursor = Connection.connect()

url = "https://api.portaldatransparencia.gov.br/api-de-dados/cartoes?"

chave = {'chave-api-dados':'2f0392da557ad41aee3f13ca7c09f9c1'}


#initial = date(2021, 8, 25)
#final = date(2021, 9, 27)

valorDe = 5
valorAte = 10

while valorAte < 60000:
    valorDe += 5
    valorAte += 5
    print(f'Valor de: {valorDe} || Valor ate: {valorAte}')
    print()
    pagina = 0
    while True:
        pagina += 1
        param = {
            'pagina': str(pagina),
            'mesExtratoInicio':'10/2021',
            'mesExtratoFim':'10/2021',
            'tipoCartao': '1',
            'valorDe': str(valorDe),
            'valorAte': str(valorAte)
            }

        re = requests.get(url,params=param, headers=chave)

        print(f'Pagina: {pagina}')
        print(f'Status: {re.status_code}')
        if re.status_code != 200:
            break

        j = re.json()
        print(f'Tamanho resp: {len(j)}')

        for resp in j:
  
            print(resp['id'], resp['estabelecimento']['id'], resp['valorTransacao'])
 

            orgao = OrgaoMaximo(resp['unidadeGestora']['orgaoMaximo']['codigo'], 
                            resp['unidadeGestora']['orgaoMaximo']['nome'])
            saveOrgao(orgao, cursor, data)

            unidadeGestora = UnidadeGestora(resp['unidadeGestora']['codigo'], 
                                            resp['unidadeGestora']['nome'],
                                            orgao.id)
            saveUnidadeGestora(unidadeGestora, cursor, data)
            
            portador = Portador(resp['portador']['nome'],
                                unidadeGestora.id)
            savePortador(portador, cursor, data)
            
            estabelecimento = Estabelecimento(resp['estabelecimento']['id'],
                                            resp['estabelecimento']['nome'])
            saveEstabelecimento(estabelecimento, cursor, data)

            transacao = Transacao(resp['id'],
                                resp['valorTransacao'],
                                estabelecimento.id,
                                unidadeGestora.id,
                                resp['mesExtrato'],
                                portador.id,
                                resp['dataTransacao']
            )
            saveTransacao(transacao, cursor, data)
        if len(j) < 15:
            break

    
Connection.close()
