import pandas as pd
import pyautogui
from time import sleep

pyautogui.PAUSE = 0.5

# ABRIR O CHROME
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# ENTRAR NO SITE
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(3)

# FAZER LOGIN

pyautogui.click(x=797, y=374)
pyautogui.write('gb.henriquefs@gmail.com')
pyautogui.press('tab')
pyautogui.write('123')
pyautogui.press('tab')
pyautogui.press('enter')

sleep(2)

# 4. ABRIR A BASE DE DADOS DE PRODUTOS PARA CADASTRAR
tabela = pd.read_csv('produtos.csv')


# CADASTRAR PRODUTOS

for linha in tabela.index:

    codigo = str(tabela.loc[linha, 'codigo'])

    pyautogui.click(x=787, y=257)

    # CLICAR CODIGO
    pyautogui.write(codigo)
    pyautogui.press('tab')

    # CLICAR MARCA
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    # CLICAR TIPO
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    # CLICAR CATEGORIA
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    # CLICAR PRECO
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    # CLICAR CUSTO
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    # CLICAR OBS

    obs = (str(tabela.loc[linha, 'obs']))
    if obs != 'nan':
        pyautogui.write(obs)

    # CLICANDO NO ENTER
    pyautogui.press('tab')
    sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')

# CADASTRAR PRODUTOS

# REPETIR ISSO TUDO ATE O FIM DA LISTA
