from Connection import Connection


data = Connection.data_connection
cursor = Connection.connect()

# L (código) – Qual a soma das movimentações sigilosas ?
try:
    print("\n#### Questao L ####")
    cursor.execute("select SUM(valorTransacao) from transacao where estabelecimento=-11")
    soma = cursor.fetchone()[0]
    print("Soma total das movimentações sigilosas: {0:.2f}".format(soma))
except:
    pass

Connection.close()