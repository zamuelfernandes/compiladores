import ply.lex as lex 
import ply.yacc as yacc

from lex_analyzer import*
from sint_analyzer import*

# Constrói o lexer
lexer = lex.lex()

# Constrói o parser
# parser = yacc.yacc()

# Teste do analisador léxico
if __name__ == "__main__":
    data = '''
    play int x = 10;
    real y = 5.5;
    char c = 'a';
    if (x > y) {
        write x;
    } else {
        write y;
    }
    close
    '''
    
    lexer.input(data)
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    
    # result = parser.parse(data)
    # print("Análise concluída!")
