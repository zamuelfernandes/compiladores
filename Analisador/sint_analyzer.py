import ply.yacc as yacc
from lex_analyzer import tokens

# Regras de produção para o analisador sintático

def p_program(p):
    '''program : PLAY declarations statements CLOSE'''
    p[0] = ('program', p[2], p[3])

def p_declarations(p):
    '''declarations : declarations declaration
                    | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_declaration(p):
    '''declaration : type VARIAVEL PONTOVIRGULA'''
    p[0] = ('declaration', p[1], p[2])

def p_type(p):
    '''type : RESERVADA'''
    p[0] = p[1]

def p_statements(p):
    '''statements : statements statement
                  | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_statement(p):
    '''statement : assignment_statement
                 | if_statement
                 | while_statement
                 | io_statement'''
    p[0] = p[1]

def p_assignment_statement(p):
    '''assignment_statement : VARIAVEL ATRIBUICAO expression PONTOVIRGULA'''
    p[0] = ('assignment', p[1], p[3])

def p_if_statement(p):
    '''if_statement : CASO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO else_statement'''
    p[0] = ('if', p[3], p[6], p[8])

def p_else_statement(p):
    '''else_statement : CASOCONTRARIO INICIOBLOCO statements FIMBLOCO
                      | empty'''
    if len(p) == 5:
        p[0] = ('else', p[3])
    else:
        p[0] = None

def p_while_statement(p):
    '''while_statement : REPETICAO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO'''
    p[0] = ('while', p[3], p[6])

def p_io_statement(p):
    '''io_statement : ENTRADA ABREPARENTESE VARIAVEL FECHAPARENTESE PONTOVIRGULA
                    | SAIDA ABREPARENTESE expression FECHAPARENTESE PONTOVIRGULA'''
    p[0] = ('io', p[1], p[3])

def p_expression(p):
    '''expression : term
                  | expression SOMA term
                  | expression SUB term
                  | expression MENOR term
                  | expression MAIOR term
                  | expression MENORIGUAL term
                  | expression MAIORIGUAL term
                  | expression DUPLOIGUAL term
                  | expression DIFERENTE term
                  | expression AND term
                  | expression OR term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('expression', p[2], p[1], p[3])

def p_term(p):
    '''term : factor
            | term MULT factor
            | term DIV factor
            | term RESTO factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('term', p[2], p[1], p[3])

def p_factor(p):
    '''factor : VARIAVEL
              | INTEIRO
              | REAL
              | ABREPARENTESE expression FECHAPARENTESE'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_empty(p):
    '''empty :'''
    p[0] = None

# Tratamento de erros sintáticos
def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

# Constrói o parser
parser = yacc.yacc()
