
def saveOrgao (orgao, cursor, data):
    try:
        cursor.execute(f'INSERT INTO orgaomaximo (codigo, nome) VALUES ({orgao.id}, "{orgao.nome}");')
        data.commit()
    except:
        pass


def saveUnidadeGestora (unidadeGestora, cursor, data):
    try:
        cursor.execute(f"""INSERT INTO unidadegestora (codigo, nome, orgao) 
            VALUES ({unidadeGestora.id}, "{unidadeGestora.nome}", {unidadeGestora.orgaoMaximo});""")
        data.commit()
    except:
        pass
    

def savePortador (portador, cursor, data):
    try:
        cursor.execute(f"""INSERT INTO portador (nome, unidadegestora) 
            VALUES ("{portador.nome}", {portador.unidadeGestora});""")
        data.commit()
    except:
        pass
    
  
def saveEstabelecimento (estabelecimento, cursor, data):
    try:
        cursor.execute(f"""INSERT INTO estabelecimento (id, nome) 
            VALUES ({estabelecimento.id}, "{estabelecimento.nome}");""")
        data.commit()
    except:
        pass
    
    

def saveTransacao (transacao, cursor, data):
    try:
        cursor.execute(f"""INSERT INTO transacao (id, valortransacao, estabelecimento, 
            unidadegestora, mesExtrato, portador, dataTransacao) 
            VALUES ({transacao.id}, {transacao.valorTransacao}, {transacao.estabelecimento}, 
            {transacao.unidadeGestora}, '{transacao.mesExtrato}', {transacao.portador}, {transacao.dataTransacao});""")
        data.commit()

    except:
        pass
    

def getIdPortador(nome, cursor):
    cursor.execute(f"SELECT id FROM portador WHERE nome='{nome}'")
    id = cursor.fetchone()[0]
    return id
