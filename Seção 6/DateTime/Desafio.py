from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y'
data_emprestimo = datetime.strptime("20/12/2020", fmt)
data_final_pagamento = datetime.strptime("20/12/2025", fmt)
atualizar_mes = relativedelta(months=1)
valor_a_pagar = float(1000000)

while True:
    valor_prestacao = valor_a_pagar / 60
    print(f"Pagamento Realizado: {data_emprestimo.strftime(fmt)}")
    print(f"valor Pago: R${valor_prestacao:.2f}")
    data_emprestimo += atualizar_mes
    if data_emprestimo > data_final_pagamento:
        break


