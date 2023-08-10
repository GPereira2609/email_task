import smtplib
import schedule
import time

from datetime import date, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = "gheaven26@gmail.com"
pwd = "cfspugitkylzshnf"
target = "gabriel.pereira2609@gmail.com"

# Dados
cheques = [
    {
        "nome": "Junior Givaldo Medeiros",
        "numero": 78,
        "valor": 2160,
        "data": date(2023, 9, 9)
    },
    {
        "nome": "pessoa_teste",
        "numero": "2609",
        "valor": 1111,
        "data": date(2023, 8, 12)
    }
]

# Mensagem
mensagem = MIMEMultipart()
mensagem["From"] = user
mensagem["To"] = target
mensagem["Subject"] = "ATENÇÂO"

def verificar_pendencias():
    for cheque in cheques:
        if cheque["data"] - timedelta(days=1) == date.today():
            numero = cheque["numero"]
            nome = cheque["nome"]
            valor = cheque["valor"]
            corpo_email = f"""
                    Cheque de numero 00{ numero } de valor { valor } expira hoje!
                    Entregue à { nome }
            """
            mensagem.attach(MIMEText(corpo_email, 'plain'))

            # Servidor 
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(user, pwd)
                texto_email = mensagem.as_string()
                server.sendmail(user, target, texto_email)
                server.quit()
                print("Email enviado")
            except Exception as e:
                print("Erro ao enviar o email", e)

schedule.every().day.at("10:00").do(verificar_pendencias)

while True:
    schedule.run_pending()
    time.sleep(1)