import pyautogui
import time
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
#time.sleep(3)
pyautogui.PAUSE = (1.5)
# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link do sistema

pyautogui.write("Digite a URL do sistema da empresa")
pyautogui.press("enter")
time.sleep(3) # O time.sleep é para esperar um determinado tempo apenas nesse pedaço de código

# 2 passo fazer o login
# selecionar o campo do e-mail
pyautogui.click(x=691, y=474)
# escrever o e-mail
pyautogui.write("emaildeacesso@exemplo.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")

# 3 passo: importar a base de produtos para cadastrar
tabela = pd.read_csv("produtos.csv")
# 4 passo: Cadastrar um produto
for linha in tabela.index:
    #clicar no campo de código
    pyautogui.click(x=801, y=313)
    # pegar da tabela o valor do campo que a gente precisa
    codigo = tabela.loc[linha, "codigo"]
    #preencher o campo código
    pyautogui.write(str(codigo))
    # Passar para o próximo campo
    pyautogui.press("tab")
    #preencher os outros campos
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
    pyautogui.press("enter") #cadastrar o produto, botão de enviar

    #dar scroll de tudo para cima
    pyautogui.scroll(10000)
