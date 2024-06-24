import ply.lex as lex 
import ply.yacc as yacc

from lex_analyzer import lexer
from sint_analyzer import parser

# Exemplo 1: Comandos de Entrada e Saída
example1 = '''play
    int x;
    int y;
    read(x);
    read(y);
    write(x + y);
close'''

# Exemplo 2: Comandos Condicionais
example2 = '''play
    int a;
    int b;
    int max;
    read(a);
    read(b);
    if (a > b) {
        max <- a;
    } else {
        max <- b;
    }
    write(max);
close'''

# Exemplo 3: Comandos de Repetição
example3 = '''play
    int i;
    int sum;
    sum <- 0;
    i <- 1;
    while (i <= 10) {
        sum <- sum + i;
        i <- i + 1;
    }
    write(sum);
close'''

# Função para testar um exemplo
def test_example(data):
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"Token: {tok.type}, Valor: {tok.value}, Linha: {tok.lineno}")


# Teste do analisador léxico
if __name__ == "__main__":

    example = example3 #trocar aqui

    # print("Exemplo 1: Comandos de Entrada e Saída")
    # test_example(example)
    # print("\n")

    # print("Exemplo 2: Comandos Condicionais")
    # test_example(example)
    # print("\n")

    print("Exemplo 3: Comandos de Repetição")
    test_example(example)
    print("\n")

    lexer.lineno = 0;
    
    result = parser.parse(example)
    print("Análise concluída!")
