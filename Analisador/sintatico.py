import ply.yacc as yacc

# Get the token map from the lexer. This is required.
from mylexer import tokens

# Definir a gramática

def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : expression_statement
                 | compound_statement
                 | selection_statement
                 | iteration_statement
                 | io_statement'''
    p[0] = p[1]

def p_expression_statement(p):
    '''expression_statement : expression PONTOVIRGULA'''
    p[0] = ('expression_statement', p[1])

def p_compound_statement(p):
    '''compound_statement : INICIOBLOCO statement_list FIMBLOCO'''
    p[0] = ('compound_statement', p[2])

def p_selection_statement(p):
    '''selection_statement : CASO ABREPARENTESE expression FECHAPARENTESE compound_statement CASOCONTRARIO compound_statement
                           | CASO ABREPARENTESE expression FECHAPARENTESE compound_statement'''
    if len(p) == 8:
        p[0] = ('if_else_statement', p[3], p[5], p[7])
    else:
        p[0] = ('if_statement', p[3], p[5])

def p_iteration_statement(p):
    '''iteration_statement : REPETICAO ABREPARENTESE expression FECHAPARENTESE compound_statement'''
    p[0] = ('while_statement', p[3], p[5])

def p_io_statement(p):
    '''io_statement : PLAY ABREPARENTESE expression FECHAPARENTESE PONTOVIRGULA
                    | CLOSE ABREPARENTESE expression FECHAPARENTESE PONTOVIRGULA
                    | ENTRADA ABREPARENTESE VARIAVEL FECHAPARENTESE PONTOVIRGULA
                    | SAIDA ABREPARENTESE expression FECHAPARENTESE PONTOVIRGULA'''
    p[0] = ('io_statement', p[1], p[3])

def p_expression(p):
    '''expression : assignment_expression
                  | arithmetic_expression
                  | relational_expression
                  | logical_expression'''
    p[0] = p[1]

def p_assignment_expression(p):
    '''assignment_expression : VARIAVEL ATRIBUICAO expression'''
    p[0] = ('assignment', p[1], p[3])

def p_arithmetic_expression(p):
    '''arithmetic_expression : arithmetic_expression SOMA term
                             | arithmetic_expression SUB term
                             | term'''
    if len(p) == 4:
        p[0] = ('arithmetic', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term MULT factor
            | term DIV factor
            | term RESTO factor
            | factor'''
    if len(p) == 4:
        p[0] = ('term', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : ABREPARENTESE expression FECHAPARENTESE
              | INTEIRO
              | REAL
              | VARIAVEL'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_relational_expression(p):
    '''relational_expression : expression MENOR expression
                             | expression MAIOR expression
                             | expression MENORIGUAL expression
                             | expression MAIORIGUAL expression
                             | expression DUPLOIGUAL expression
                             | expression DIFERENTE expression'''
    p[0] = ('relational', p[2], p[1], p[3])

def p_logical_expression(p):
    '''logical_expression : expression AND expression
                          | expression OR expression
                          | NOT expression'''
    if len(p) == 3:
        p[0] = ('logical', p[1], p[2])
    else:
        p[0] = ('logical', p[2], p[1], p[3])

# Tratamento de erros de sintaxe
def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

# Build the parser
parser = yacc.yacc()

# Para testar o parser, você pode usar o seguinte código:
while True:
    try:
        s = input('entrada > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)

#######################################################################################

import ply.yacc as yacc
from lex_analyzer import tokens, reserved

# Regras de produção para o analisador sintático

# Erros sintáticos
errossintaticos = []

def p_program(p):
    '''
    program : PLAY declarations statements CLOSE
    '''
    pass

def p_declarations(p):
    '''
    declarations : declarations declaration
                 | declaration
    '''
    pass

def p_declaration(p):
    '''
    declaration : type VARIAVEL PONTOVIRGULA
                | type variavel_mf PONTOVIRGULA
    '''
    pass

def p_type(p):
    '''
    type : RESERVADA
    '''
    pass

def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''
    pass

def p_statement(p):
    '''
    statement : assignment_statement
              | if_statement
              | while_statement
              | io_statement
              | statement_malformed
    '''
    pass

def p_assignment_statement(p):
    '''
    assignment_statement : VARIAVEL ATRIBUICAO expression PONTOVIRGULA
                         | variavel_mf ATRIBUICAO expression PONTOVIRGULA
    '''
    pass

def p_if_statement(p):
    '''
    if_statement : CASO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO else_statement
    '''
    pass

def p_else_statement(p):
    '''
    else_statement : CASOCONTRARIO INICIOBLOCO statements FIMBLOCO
                   | empty
    '''
    pass

def p_while_statement(p):
    '''
    while_statement : REPETICAO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO
    '''
    pass

def p_io_statement(p):
    '''
    io_statement : ENTRADA ABREPARENTESE VARIAVEL FECHAPARENTESE PONTOVIRGULA
                 | SAIDA ABREPARENTESE expression FECHAPARENTESE PONTOVIRGULA
    '''
    pass

def p_expression(p):
    '''
    expression : term
               | expression SOMA term
               | expression SUB term
               | expression AND term
               | expression OR term
               | expression MENOR term
               | expression MAIOR term
               | expression MENORIGUAL term
               | expression MAIORIGUAL term
               | expression DUPLOIGUAL term
               | expression DIFERENTE term
               | numero_mf
               | string_mf
    '''
    pass

def p_term(p):
    '''
    term : factor
         | term MULT factor
         | term DIV factor
         | term RESTO factor
    '''
    pass

def p_factor(p):
    '''
    factor : VARIAVEL
           | INTEIRO
           | REAL
           | ABREPARENTESE expression FECHAPARENTESE
    '''
    pass

def p_empty(p):
    '''
    empty :
    '''
    pass

def p_statement_malformed(p):
    '''
    statement_malformed : variavel_mf PONTOVIRGULA
                        | numero_mf PONTOVIRGULA
                        | string_mf PONTOVIRGULA
    '''
    pass

# Regra de erro
def p_error(p):
    if p:
        print(f"Erro sintático na entrada '{p.value}' na linha {p.lineno}")
        errossintaticos.append(p)
    else:
        print("Erro sintático no final da entrada")

# Constrói o parser
parser = yacc.yacc()

# Teste do analisador sintático
if __name__ == "__main__":
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
    result = parser.parse(data)
    print(result)
