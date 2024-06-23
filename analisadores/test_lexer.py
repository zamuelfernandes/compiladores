from lexx import lexer

def test_lexer():
    # Entrada de teste
    data = '''
    play int x <- 10;
    real y <- 5.5;
    char c <- 'a';
    if (x > y) {
        write x;
    } else {
        write y;
    }
    close
    '''

    # Alimente o lexer com a entrada
    lexer.input(data)

    # Tokens esperados
    expected_tokens = [
        ('PLAY', 'play'),
        ('RESERVADA', 'int'),
        ('VARIAVEL', 'x'),
        ('ATRIBUICAO', '<-'),
        ('INTEIRO', 10),
        ('PONTOVIRGULA', ';'),
        ('VARIAVEL', 'y'),
        ('ATRIBUICAO', '<-'),
        ('REAL', 5.5),
        ('PONTOVIRGULA', ';'),
        ('RESERVADA', 'char'),
        ('VARIAVEL', 'c'),
        ('ATRIBUICAO', '<-'),
        ('CARACTER', 'a'),
        ('PONTOVIRGULA', ';'),
        ('CASO', 'if'),
        ('ABREPARENTESE', '('),
        ('VARIAVEL', 'x'),
        ('MAIOR', '>'),
        ('VARIAVEL', 'y'),
        ('FECHAPARENTESE', ')'),
        ('INICIOBLOCO', '{'),
        ('SAIDA', 'write'),
        ('VARIAVEL', 'x'),
        ('PONTOVIRGULA', ';'),
        ('FIMBLOCO', '}'),
        ('CASOCONTRARIO', 'else'),
        ('INICIOBLOCO', '{'),
        ('SAIDA', 'write'),
        ('VARIAVEL', 'y'),
        ('PONTOVIRGULA', ';'),
        ('FIMBLOCO', '}'),
        ('CLOSE', 'close')
    ]

    # Verifique se os tokens gerados correspondem aos tokens esperados
    for expected_token in expected_tokens:
        tok = lexer.token()
        assert tok is not None, f"Expected token {expected_token} but got None"
        assert (tok.type, tok.value) == expected_token, f"Expected {expected_token} but got ({tok.type}, {tok.value})"
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    test_lexer()
