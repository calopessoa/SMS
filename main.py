from curses import meta
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2f5b8dbd335d05a1ce74fd89200184e4"
# Your Auth Token from twilio.com/console
auth_token  = "741968cb1d8d4b8ba7e86be34d0caf8c"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabelaVendas = pd.read_excel(f'{mes}.xlsx')
    metaVendas = tabelaVendas['Vendas'] > 55000
    if(metaVendas).any():
        vendedor = tabelaVendas.loc[metaVendas, 'Vendedor'].values[0]
        vendas = tabelaVendas.loc[metaVendas, 'Vendas'].values[0]

        message = client.messages.create(
            to=+5583996010121,
            from_=+18149047827,
            body=f'No mes de {mes} a meta foi batida! YES! Vendedor {vendedor}, realizou R$ {vendas} em vendas.'
        )
        print(message.sid)
