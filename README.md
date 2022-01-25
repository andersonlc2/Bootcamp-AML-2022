Questões

A – Com suas palavras explique o que é lavagem de dinheiro.
Resposta: É um procedimento que tem a finalidade de tentar tornar licito os recursos de origem ilegal.

B – O que é Cartão de Pagamento do Governo Federal (CPGF), e qual a sua finalidade.
Resposta: É um meio de pagamento, similar ao cartão de crédito, que o governo utiliza para pagamentos de despesas que podem ser enquadradas como suprimentos de fundos.

C – Quem pode utilizar o CPGF?
Resposta: Órgãos e entidades da Administração Pública Federal

D – Qual a URL onde é possível fazer o download dos arquivos do CPGF?
Resposta: https://www.portaltransparencia.gov.br/download-de-dados/cpgf

E – Qual a URL da paǵina com a descrição dos campos (ou dicionário de dados) da CPGF?
Resposta: https://api.portaldatransparencia.gov.br/swagger-ui.html#/Gastos%20por%20meio%20de%20cart%C3%A3o%20de%20pagamento/cartaoUsingGET

F – É possível identificar o nome e o documento do portador do CPGF, em todas as
movimentações ou há movimentações onde não é possível identificar o portador?
Resposta: Não, há movimentações em que esses campos não são informados.

G – É possível identificar o Órgão do portador do CPGF?
Resposta: Sim. Todos os portadores contem a informação do respectivo orgão.

H - Qual o nome do Órgão cujo código é 20402?
Resposta: Agência Espacial Brasileira

I - É possível identificar o Nome e Documento (CNPJ) dos favorecidos pela utilização do
CPGF?
Resposta: Em quase todas as transações é possivel, alguns não aparecem, como por exemplo
em trasações sigilosas.

J – É possível identificar a data e o valor das movimentações financeiras do CPGF, em
todas as movimentações? Ou há movimentações onde não é possível identificar as datas e
ou valores?
Resposta: Os valores aparecem em todas as movimentações, mas as datas em movimentações
sigilosas não podemos identificar.

K (código) – Qual a soma total das movimentações utilizando o CPGF?

L (código) – Qual a soma das movimentações sigilosas ?

M (código) – Qual o Órgão que mais realizou movimentações sigilosas no período e qual o
valor (somado)?

N (código) – Qual o nome do portador que mais realizou saques no período? Qual a soma
dos saques realizada por ele? Qual o nome do Órgão desse portador?

O (código) – Qual o nome do favorecido que mais recebeu compras realizadas utilizando o
CPGF?

P - Descreva qual a abordagem utilizada para desenvolver o código para os ítens de K a O.
Resposta: Através de chamadas a Api do CPGF passandos os parametros como o mes de extrato, datas de 
transação, tipo do cartão, pegamos as informações pertinentes e armazenamos em um banco 
de dados, para que posteriormente podemos fazer consultas nesse banco para o uso 
nas diversas questões apresentadas.
