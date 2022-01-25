from Connection import Connection


data = Connection.data_connection
cursor = Connection.connect()

# N (código) – Qual o nome do portador que mais realizou saques no período? Qual a soma
# dos saques realizada por ele? Qual o nome do Órgão desse portador?

print("\n#### Questao N ####")
cursor.execute("""SELECT SUM(valorTransacao) As Total, unidadegestora.nome, portador.nome
        FROM transacao
        INNER JOIN portador on transacao.portador = portador.id
        inner join unidadegestora on transacao.unidadegestora = unidadegestora.codigo
        where transacao.estabelecimento = -2
        group by portador
        order by Total desc""")
total = cursor.fetchone()

print("Orgao:", total[1])
print("Nome portador:", total[2])
print("Valor: {0:.2f}".format(total[0]))





print()
Connection.close()