import time
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


def vezes_tecla_cima(vezes):
    for i in range(vezes):
        pyautogui.press("up")


def entrar_licao(vezes):
    for i in range(vezes):
        tab()
    enter()
    time.sleep(1)
    tab()
    enter()
    time.sleep(2)


def mandar_licao():
    pyautogui.press("f12")
    time.sleep(2.5)
    pyautogui.hotkey("ctrl", "f")
    time.sleep(0.5)
    pyautogui.write(r"""//*[@id="root"]/div/div[1]/button[1]""")
    time.sleep(1)
    pyautogui.press("f12")
    clicar_em(880, 602)
    time.sleep(3)


def entrar_html(codigo, x=0, y=0):
    pyautogui.press("f12")
    time.sleep(3.5)         
    pyautogui.hotkey("ctrl", "f")
    time.sleep(0.5)
    pyautogui.write(codigo)
    time.sleep(1.5)
    pyautogui.press("f12")
    if x == 0 and y == 0:
        pass
    else:
        clicar_em(x, y)
    time.sleep(1.5)
    


letras = ("a", "b", "c", "d", "e")
def selecionar_alternativa(qtde_alternativas, alternativa):
    cont = 0
    for letra in letras:
        if letra != alternativa:
            pass
        elif letra == alternativa:
            if qtde_alternativas == 3:
                subidas = (cont + 2) - (cont * 2)
                vezes_tecla_cima(subidas)  
                break

            elif qtde_alternativas == 4:
                subidas = (cont + 3) - (cont * 2)
                vezes_tecla_cima(subidas)
                break

            elif qtde_alternativas == 5:
                subidas = (cont + 4) - (cont * 2)
                vezes_tecla_cima(subidas)
                break

        cont = cont + 1

pyautogui.alert(
    "mova o mouse para o canto superior direito se quiser encerrar o programa",
    "O programa ira começar!",
)

# abrir o chrome
pyautogui.hotkey("win", "s")
time.sleep(1)
pyautogui.write("edge")
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

cont = 0
while True:
    cont = cont + 1
    # abrir a lição
    if cont != 111:
        entrar_licao(4)
    # else:
    #     entrar_licao(3)

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
    clicar_em(0, 400)
    time.sleep(1)
    tab()
    enter()
    time.sleep(1.5)

    # ir nas respostas do brainly
    entrar_html(
        r"""//*[@id="question-sg-layout-container"]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div"""
    )
    time.sleep(4)

    # selecionar a alternativa
    fechar_pagina()
    time.sleep(1.5)
    clicar_em(1340, 548)
    pyautogui.tripleClick(1356, 686)
    pyautogui.tripleClick(1356, 686)
    time.sleep(1)

    entrar_html("question-choice", 872, 515)

    # verificar qual alternativa escolher

    qtde_alternativas = pyautogui.prompt("Quantas questoes tem?\n(digite de 3 a 5)", "Quatidade de questões")

    alternativa = pyautogui.prompt(
        "Escreva qual é a alternativa...\nSe estiver em dúvida volte ao site da resposta e reveja",
        "Confirmação da resposta".casefold(),
    )

    # tratamento de erro
    if alternativa not in letras:
        sair_confirmar = pyautogui.confirm(
            "Aperte em 'ok' para encerrar ou 'cancelar' para continuar o programa",
            "Deseja sair?",
        )

        if sair_confirmar == "OK":
            pyautogui.alert("Até mais :)", "Programa encerrado")
            break
        else:
            continue
    
    time.sleep(1.5)
    selecionar_alternativa(int(qtde_alternativas), str(alternativa))
    time.sleep(1)
    mandar_licao()
    time.sleep(4)
