# SMS - Automatização de disparo de metas!

### Olá! Este é um simples, porém funcional e divetido estudo de automatização via Python. 

- [Uso](#uso)
- [Reconhecimento](#reconhecimento)

# Uso

Para praticar e expandir o exercício, abra o terminal em um local onde normalmente são realizados exercícios/projetos. 
Realize o clone do respositório em sua máquina:

```bash
git clone 'git@github.com:calopessoa/SMS.git'
```

Vá para a pasta do projeto:

```bash
cd SMS
```

Instale as dependências:

```bash
pip install pandas
```
```bash
pip install twilio
```
```bash
pip install openpyxl
```

Após isso, vá ao site e realize o cadastro para que possas registrar seu Account ID (account_sid) e o autenticador (auth_token):
https://www.twilio.com/

crie o arquivo 'twilio.env' com o seguinte padrão:

```bash
echo "export TWILIO_ACCOUNT_SID='INSIRA AQUI SEU ACCOUNT ID'" > twilio.env
echo "export TWILIO_AUTH_TOKEN='INSIRA AQUI SEU TOKEN AUTH'" >> twilio.env
source ./twilio.env
```

Insira os dados constantes em Account Info no código, substituindo pelos valores que há no meu (inclusive meu número de telefone!) e...
execute o comando Run Pyton File no menu de navegação.

# Reconhecimento

<p>Projeto originalmente criado por Lira da Hashtag: https://www.youtube.com/c/HashtagProgramação </p>
<p>Alterado e implantado por Carlos Augusto : https://www.linkedin.com/in/carlos-augusto-lopes-de-oliveira-2602458b/ </p>
