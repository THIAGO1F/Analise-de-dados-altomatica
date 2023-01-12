#importando as bibliotecas 
import smtplib
import email.message



#Uma função que vai ser chamada no outro programa
def enviar_email(quantidade,total): 
    #corpo do email que vai ser enviado com quantidade e o valor total de produtos | o corpo do email é utilizado tags html 
    corpo_email = f"""
    <p>Este é um email automatico não precisa responder!!!</p>
    <p>Estou informando a você o total e a quantidade de produtos vendidos no mês.</p>
    <p>A quantidade de produtos vendidos foram de {quantidade:,.2f} itens.</p>
    <p>O total adquirido neste mês foi de R$ {total:,.2f}.</p>
    <h3>Relatório enviado por <strong>THIAGO S FERREIRA</strong>.</h3>
    """

    #aqui começa o comando para o envio do email | configurações
    #ATENÇÃO! para enviar e-mail você precisa ir em sua conta google e fazer umas configurações necessárias

    """ PASSO A PASSO para ter a chave de acesso do email 
    1- vá em gerenciar sua conta google
    2- vá em segurança
    3- procure por Como fazer login no google e verifique se a verificação em dua etapas está ativada 
    4- clique em senhas de apps
    5- prencha com sua senha
    6- vá em selecionar app e click em E-mail
    7- vá em selecionar dispositivo e click em Outro e dê um nome 
    8- click em gerar 
    9- copie a chave, essa vai ser a chave para você colocar no seu programa 
    """

    msg = email.message.Message()
    msg['Subject'] = "RELATÓRIO DE VENDAS" # Título do email a ser enviado
    msg['From'] = 'COLOQUE AQUI O EMAIL DE ORIGEM' #email de onde bvai ser  enviado
    msg['To'] = 'COLOQUE AQUI O EMAIL DE DESTINO' #email que vai receber a mensagem
    password = 'COLOQUE AQUI SUA CHAVE DE ACESSO' #IMPORTANTE | aqui você vai passar a chave de acesso do google
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    #aqui é a parte de configurção do email
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')