import ply.lex as lex 
import ply.yacc as yacc

from lex_analyzer import lexer
from sint_analyzer import parser

# Função de teste para ver a contagem de linhas
def test_line_counting():
    data = '''int x;
    x = 10;
    if (x > 5) {
        x = x + 1;
    }'''
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"Token: {tok.type}, Valor: {tok.value}, Linha: {tok.lineno}")

# Executa a função de teste
if __name__ == "__main__":
    test_line_counting()