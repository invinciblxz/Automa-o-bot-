# Passo a passo do projeto
# Entrar no sistema da empresa

link = https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla
# pyautogui.click -> clicar com o mouse
# pyautogui.hotkey -> pressionar uma combinação de teclas
# pyautogui.scroll -> rolar a tela para cima ou para baixo

pyautogui.PAUSE = 1 # tempo de espera entre as ações

# abrir o navegador(chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link da empresa
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Fazer login
# selecionar o campo de email
pyautogui.click(x=685, y=451)

# escrever seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("Sua senha")
pyautogui.click(x=955, y=638) # clicar no botão entrar
time.sleep(3)

# Importar a base de produtos para cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código:
    pyautogui.click(x=653, y=294)
    
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]

    # preencher o campo
    pyautogui.write(str(codigo))

    # passar para o próximo campo
    pyautogui.press("tab")

    #preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botão enviar)
    # dar scroll de tudo para cima
    pyautogui.scroll(5000)
