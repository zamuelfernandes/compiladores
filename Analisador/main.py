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

#Exemplo 4: Testes Genéricos
testeCont = '''play
    int x;
    x <- 10;
    if (x > 5) {
        x <- x + 1;
    }
close'''

# Função para testar um exemplo léxico
def test_example(data):
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"Token: {tok.type}, Valor: {tok.value}, Linha: {tok.lineno}")

# Função para formatar e imprimir o resultado de maneira legível
def format_result(result, indent=0):
    indent_str = '  ' * indent
    if isinstance(result, tuple):
        print(f"{indent_str}{result[0]}:")
        for item in result[1:]:
            format_result(item, indent + 1)
    elif isinstance(result, list):
        for item in result:
            format_result(item, indent)
    else:
        print(f"{indent_str}{result}")

# Teste dos analisadores
if __name__ == "__main__":

    #Definição de qual código testar
    example = testeCont 

    print("- - - Testando Exemplo - - -\n")
    test_example(example)
    print("\n")
    
    result = parser.parse(example)
    format_result(result)
    print("\nAnálise concluída!")
