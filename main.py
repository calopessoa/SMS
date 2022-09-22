from curses import meta
import pandas as pd
from twilio.rest import Client
import os

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
# Your Auth Token from twilio.com/console
auth_token  = os.environ['TWILIO_AUTH_TOKEN']
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
