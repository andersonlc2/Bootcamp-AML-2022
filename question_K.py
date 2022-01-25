from Connection import Connection


data = Connection.data_connection
cursor = Connection.connect()


# K (código) – Qual a soma total das movimentações utilizando o CPGF?
try:
    print("\n#### Questao K ####")
    cursor.execute("SELECT SUM(valorTransacao) As Total FROM transacao")
    total = cursor.fetchone()[0]
    print("Soma total das movimentações: {0:.2f}".format(total))
except:
    pass

Connection.close()