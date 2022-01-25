from Connection import Connection


data = Connection.data_connection
cursor = Connection.connect()


# M (código) – Qual o Órgão que mais realizou movimentações sigilosas no período e qual o valor (somado)?
try:
    print("\n#### Questao M ####")
    cursor.execute("""SELECT SUM(valorTransacao) As Total, unidadegestora.orgao
            FROM transacao
            INNER JOIN unidadegestora on transacao.unidadegestora = unidadegestora.codigo
            where transacao.estabelecimento = -11
            group by unidadegestora.orgao
            order by Total desc""")
    total = cursor.fetchone()
    print("Ogao: ", total[1])
    print("Valor: {0:.2f}".format(total[0]))
except:
    pass

Connection.close()