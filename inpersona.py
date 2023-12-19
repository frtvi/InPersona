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
        server.send_message(mensagem)

# Exemplo de uso
destinatario = 'destinatario@asdasd.com'
assunto = 'Assunto'
corpo = 'Corpo (texto)'
remetente = 'E-mail spoofado'
servidor_smtp = 'exemplo.smtp.com'
porta = 587
usuario = 'seu_usuario'
senha = 'sua_senha'

enviar_email(destinatario, assunto, corpo, remetente, servidor_smtp, porta, usuario, senha)
