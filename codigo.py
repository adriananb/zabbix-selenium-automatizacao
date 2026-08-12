import pyautogui
import time

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=815, y=397)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("python123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)

import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=794, y=289)

    pyautogui.write(str(tabela.loc[linha, "codigo"]))  # pega o código da tabela e escreve no campo
    pyautogui.press("tab")  # passa para o próximo campo

    # agora repete isso para os outros campos
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

    if not pd.isna(tabela.loc[linha, "obs"]):  # verifica se existe informação em obs
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("enter")

    pyautogui.scroll(5000)