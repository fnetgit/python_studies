# Enviando E-mails SMTP

import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from dotenv import load_dotenv

load_dotenv()

CAMINHO_HTML = pathlib.Path(__file__).parent / "aula185.html"

remetente = os.getenv("FROM_EMAIL", "vazio@email.com")
destinatario = os.getenv("TO_EMAIL", remetente)

smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
smtp_port = int(os.getenv("SMTP_PORT", "587"))
smtp_username = os.getenv("SMTP_USERNAME", "vazio@email.com")
smtp_password = os.getenv("SMTP_PASSWORD", "vazio")

with open(CAMINHO_HTML, "r") as arquivo:
    conteudo_html = arquivo.read()
    template = Template(conteudo_html)
    conteudo_html = template.substitute(nome="Francisco Neto")

mime_multipart = MIMEMultipart()
mime_multipart["From"] = remetente
mime_multipart["To"] = destinatario
mime_multipart["Subject"] = "Assunto do E-mail"

corpo_email = MIMEText(conteudo_html, "html")
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)

    print("E-mail enviado com sucesso!")
