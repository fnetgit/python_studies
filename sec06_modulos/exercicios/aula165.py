# Calculando as datas e parcelas de um empréstimo

# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt = "%d/%m/%Y"
emprestimo = 1_000_000
tempo = relativedelta(years=5)
inicio = datetime.strptime("20/12/2020", fmt)
final = inicio + tempo

total_meses = tempo.years * 12
valor_parcela = emprestimo / total_meses

data_parcela = inicio
for i in range(1, total_meses + 1):
    print(
        f"{i:02d}ª parcela: R${valor_parcela:,.2f} - Vencimento: {data_parcela.strftime(fmt)}"
    )
    data_parcela += relativedelta(months=1)
