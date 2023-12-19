import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(destinatario, assunto, corpo, remetente, servidor_smtp, porta, usuario, senha):
    # Configurar o e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    # Corpo do e-mail
    mensagem.attach(MIMEText(corpo, 'plain'))

    # Conectar ao servidor SMTP e enviar o e-mail
    with smtplib.SMTP(servidor_smtp, porta) as server:
        server.starttls()
        server.login(usuario, senha)
        server.sendmail(remetente, destinatario, mensagem.as_string())

# Exemplo de uso com Mailtrap
destinatario = 'vitima@vitima.com'
assunto = 'TESTE'
corpo = 'TESTE'
remetente = 'mailtrap e-mail'  # Substitua pelo seu endereço Mailtrap
servidor_smtp = 'smtp.mailtrap.io'  # Servidor SMTP do Mailtrap
porta = 587  # Porta do Mailtrap
usuario = '*********'  # Substitua pelo seu usuário Mailtrap
senha = '**********'  # Substitua pela sua senha Mailtrap

enviar_email(destinatario, assunto, corpo, remetente, servidor_smtp, porta, usuario, senha)
