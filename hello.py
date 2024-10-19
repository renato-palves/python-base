#!C:\Users\Renato\AppData\Local\Programs\Python\Python311\python.exe
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    python hello.py
"""
__version__ = "0.0.1"
__author__ = "Renato Alves"
__licence__ = "Unlicense"

import locale

current_language, encoding = locale.getlocale("LANG")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)
