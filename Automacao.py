import time
from tkinter.constants import S
import pyautogui

pyautogui.FAILSAFE = True

# definicao das funcoes
def clicar_em(x, y):
    pyautogui.click(x, y)


def enter():
    pyautogui.press("enter")


def tab():
    pyautogui.press("tab")


def copiar():
    pyautogui.hotkey("ctrl", "c")


def colar():
    pyautogui.hotkey("ctrl", "v")


def abrir_pagina():
    pyautogui.hotkey("ctrl", "t")


def fechar_pagina():
    pyautogui.hotkey("ctrl", "w")


def vezes_tecla_baixo(vezes):
    for i in range(vezes):
        pyautogui.press("down")


pyautogui.alert(
    "mova o mouse para o canto superior direito se quiser encerrar o programa",
    "O programa ira começar!",
)

# abrir o chrome
pyautogui.hotkey("win", "s")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
enter()
time.sleep(4)

# entrar no csmp
pyautogui.write("https://cmspweb.ip.tv/")
enter()
time.sleep(3)

# entrar em turmas
clicar_em(1085, 127)
time.sleep(1)

# abrir a turma especifica
clicar_em(824, 218)
time.sleep(3.5)

# abrir tarefas
clicar_em(1098, 134)
time.sleep(5)

while True:
    # abrir a lição
    for i in range(4):
        tab()
    enter()
    time.sleep(1)
    tab()
    enter()
    time.sleep(2)

    # copiar a perguta
    pyautogui.hotkey("ctrl", "a")
    copiar()
    time.sleep(1)

    # pesquisar a pergunta
    abrir_pagina()
    time.sleep(2)

    colar()
    enter()
    time.sleep(1.5)

    # entrar no site
    clicar_em(0, 376)
    time.sleep(1)
    tab()
    enter()
    time.sleep(1.2)

    # ir nas respostas
    pyautogui.press("f12")
    time.sleep(2.5)
    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)
    pyautogui.write(
        r"""//*[@id="question-sg-layout-container"]/div[1]/div[1]/div[1]/article/div/div/div[4]/div/div""", 1
    )
    time.sleep(1)
    clicar_em(183, 415)
    time.sleep(0.5)
    pyautogui.press("f12")
    time.sleep(3)

    # selecionar a alternativa
    fechar_pagina()
    time.sleep(1.5)
    clicar_em(1294, 431)

    pyautogui.press("f12")
    time.sleep(2.5)
    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)
    pyautogui.write("question-choice")
    time.sleep(1)
    clicar_em(340, 430)
    time.sleep(0.5)
    pyautogui.press("f12")

    # verificar qual alternativa escolher
    alternativa = pyautogui.prompt(
        "Escreva qual é a alternativa...\nSe estiver em dúvida volte ao site da resposta e reveja",
        "Confirmação da resposta",
    )

    if alternativa == "a" or alternativa == "A":
        tab()
        enter()
        time.sleep(2.5)

    elif alternativa == "b" or alternativa == "B":
        vezes_tecla_baixo(1)
        tab()
        enter()
        time.sleep(2.5)

    elif alternativa == "c" or alternativa == "C":
        vezes_tecla_baixo(2)
        tab()
        enter()
        time.sleep(2.5)

    elif alternativa == "d" or alternativa == "D":
        vezes_tecla_baixo(3)
        tab()
        enter()
        time.sleep(2.5)

    elif alternativa == "e" or alternativa == "E":
        vezes_tecla_baixo(4)
        tab()
        enter()
        time.sleep(2.5)

    # se nao digitar (a, b, c, d ou e) perguntar se deseja sair ou nao
    else:
        sair_confirmar = pyautogui.confirm(
            "Aperte em 'ok' para encerrar ou 'cancelar' para continuar o programa",
            "Deseja sair?",
        )

        if sair_confirmar == "OK":
            pyautogui.alert("Até mais :)", "Programa encerrado")
            break
        else:
            continue


