from lex_analyzer import*
from sint_analyzer import*

# Exemplo 1: Teste dos Comandos de Entrada e Saída
exampleIO = '''play
    int x;
    int y;
    read(x);
    read(y);
    write(x + y);
close'''

# Exemplo 2: Teste dos Comandos Condicionais
exampleCond = '''play
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

# Exemplo 3: Teste dos Comandos de Repetição
exampleRepeat = '''play
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
exampleErro = '''play
    int x;
    x = 10;
    if (x > 5) {
        x = x + 1;
    }
close'''

# Função para testar um exemplo léxico
def test_example(data):
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'error':
            continue
        print(f"Token: {tok.type}, Valor: {tok.value}, Linha: {tok.lineno}")

# Gerar arquivo do reconhecimento de análise léxica
def gerar_reconhecimento_lexico(data):
    lexer.input(data)
    tokens_reconhecidos = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_reconhecidos.append(f"Token: {tok.type} | Valor: '{tok.value}' | Linha: {tok.lineno}")

    return tokens_reconhecidos

# Gerar arquivo do reconhecimento de análise sintática
def gerar_reconhecimento_sintatico(data):
    lexer.lineno = 1
    result = parser.parse(data)
    print(result)
    return result
        
# Fazer reconhecimento
def gerar_arquivo_reconhecimento(data, type):
    tokens_reconhecidos = gerar_reconhecimento_lexico(data)
    gerar_reconhecimento_sintatico(data)

    with open(f"reconhecimento_comandos_{type}.txt", "w", encoding="utf-8") as f:
        f.write("Reconhecimento Léxico:\n")
        for item in tokens_reconhecidos:
            f.write(f"{item}\n")
        
        f.write("\nReconhecimento Sintático:\n")
        if len(erros_sintaticos) == 0:
            f.write("Análise sintática concluída sem erros.\n")
        else:
            f.write("Erros sintáticos encontrados:\n")
            for erro in erros_sintaticos:
                f.write(f"{erro}\n")
                
if __name__ == "__main__":

    #Definição de qual código testar
    example = exampleErro 

    print("- - - Testando Exemplo - - -\n")
    
    gerar_arquivo_reconhecimento(example, 'exampleErro')
    
    print("\nAnálise Léxica e Sintática concluída!")
