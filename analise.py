#importando as biblioecas necessárias 
import pyautogui as pt
from time import sleep
import pyperclip

import pandas as pd
import email_auto 

#iniciando dando um comndo de espera entre os comandos do pyautogui
pt.PAUSE = 1
sleep(2)
#iniciando a automação | baixar o banco de dados
#atenção pode ser que no seu dispositivo o tamanho de tela pode ser diferente | use o programa position.py para posicionar no local correto
pt.hotkey('ctrl','t')
pyperclip.copy('https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh')
pt.hotkey('ctrl','v')
pt.press('ENTER')
sleep(5)
pt.moveTo(x=359, y=276)
sleep(5)
pt.rightClick(x=359, y=276)
sleep(5)
pt.click(x=474, y=679)
sleep(10)

#iniciando a análise de dados com pandas 
tabela_vendas = pd.read_excel(r'C:\\\\Users\\\\tf938\\\\Downloads\\\\Vendas - Dez.xlsx')

#pegando os dados da coluna e somando-os
total = tabela_vendas['Valor Final'].sum()
#pegando a quantidade de produtos da coluna quantidade e somando-os
quantidade = tabela_vendas['Quantidade'].sum()
#mostrando o resultado no terminal
print(f'R$ {total:,.2f}')
print(f'QT {quantidade:,.2f} itens')

#aqui é importante pois usei modulos, importei um outro programa que criei de envio de e-mail automatico, passando os parâmetros de quantidade e o total de produtos
email = email_auto.enviar_email(quantidade,total)