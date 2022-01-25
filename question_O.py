from Connection import Connection


data = Connection.data_connection
cursor = Connection.connect()

# O (código) – Qual o nome do favorecido que mais recebeu compras realizadas utilizando o CPGF?
try:
    print("\n#### Questao O ####")
    cursor.execute("""SELECT SUM(valorTransacao) As Total, transacao.estabelecimento, estabelecimento.nome
FROM transacao
INNER JOIN estabelecimento on transacao.estabelecimento = estabelecimento.id
where estabelecimento.id > 0
group by transacao.estabelecimento
order by Total desc""")
    total = cursor.fetchone()
    print("Dos estastabelecimentos que temos informações o que mais recebeu foi:", total[1])
    print("Nome estabelecimento:", total[2])
    print("Valor: {0:.2f}".format(total[0]))
except:
    pass

print()
Connection.close()