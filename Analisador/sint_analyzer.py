## ANALISADOR SINTATICO
import ply.yacc as yacc
from lex_analyzer import tokens  # Importa os tokens do analisador léxico

# Erros sintáticos
errossintaticos = []

def p_program(p):
    '''program : PLAY declarations statements CLOSE'''
    pass

def p_declarations(p):
    '''declarations : declarations declaration
                    | declaration'''
    pass

def p_declaration(p):
    '''declaration : type VARIAVEL PONTOVIRGULA'''
    pass

def p_type(p):
    '''type : RESERVADA'''
    pass

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    pass

def p_statement(p):
    '''statement : assignment_statement
                 | if_statement
                 | while_statement
                 | io_statement'''
    pass

def p_assignment_statement(p):
    '''assignment_statement : VARIAVEL IGUAL expression PONTOVIRGULA'''
    pass

def p_if_statement(p):
    '''if_statement : CASO ABRE_PARENTESES expression FECHA_PARENTESES ABRE_CHAVES statements FECHA_CHAVES else_statement'''
    pass

def p_else_statement(p):
    '''else_statement : CASOCONTRARIO ABRE_CHAVES statements FECHA_CHAVES
                      | empty'''
    pass

def p_while_statement(p):
    '''while_statement : REPETICAO ABRE_PARENTESES expression FECHA_PARENTESES ABRE_CHAVES statements FECHA_CHAVES'''
    pass

def p_io_statement(p):
    '''io_statement : ENTRADA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES PONTOVIRGULA
                    | SAIDA ABRE_PARENTESES expression FECHA_PARENTESES PONTOVIRGULA'''
    pass

def p_expression(p):
    '''expression : term
                  | expression SOMA term
                  | expression SUB term
                  | expression E term
                  | expression OU term
                  | expression MENOR term
                  | expression MAIOR term
                  | expression MENOR_IGUAL term
                  | expression MAIOR_IGUAL term
                  | expression DUPLO_IGUAL term
                  | expression DIFERENTE term'''
    pass

def p_term(p):
    '''term : factor
            | term MULT factor
            | term DIV factor
            | term RESTO factor'''
    pass

def p_factor(p):
    '''factor : VARIAVEL
              | INTEIRO
              | REAL
              | ABRE_PARENTESES expression FECHA_PARENTESES'''
    pass

def p_empty(p):
    '''empty :'''
    pass

# Regra de erro
def p_error(p):
    if p:
        print(f"Erro sintático na entrada '{p.value}' na linha {p.lineno}")
        errossintaticos.append(p)
    else:
        print("Erro sintático no final da entrada")
