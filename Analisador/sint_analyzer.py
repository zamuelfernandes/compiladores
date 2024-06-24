import ply.yacc as yacc
from lex_analyzer import tokens

# Definição das regras de produção

def p_program(p):
    '''program : PLAY statements CLOSE'''

def p_statements_multiple(p):
    '''statements : statements statement'''

def p_statements_single(p):
    '''statements : statement'''

def p_statement_while(p):
    '''statement : REPETICAO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO'''

def p_statement_if(p):
    '''statement : CASO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO
                 | CASO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO CASOCONTRARIO INICIOBLOCO statements FIMBLOCO'''

def p_statement_assignment(p):
    '''statement : VARIAVEL ATRIBUICAO expression PONTOVIRGULA
                 | VARIAVEL ATRIBUICAO INTEIRO PONTOVIRGULA
                 | VARIAVEL ATRIBUICAO REAL PONTOVIRGULA
                 | VARIAVEL ATRIBUICAO CARACTER PONTOVIRGULA
                 | VARIAVEL ATRIBUICAO VARIAVEL PONTOVIRGULA'''

def p_statement_io(p):
    '''statement : ENTRADA ABREPARENTESE VARIAVEL FECHAPARENTESE PONTOVIRGULA
                 | SAIDA ABREPARENTESE expression FECHAPARENTESE PONTOVIRGULA'''

def p_expression_binop(p):
    '''expression : expression SOMA expression
                  | expression SUB expression
                  | expression MULT expression
                  | expression DIV expression
                  | expression RESTO expression'''

def p_expression_group(p):
    '''expression : ABREPARENTESE expression FECHAPARENTESE'''

def p_expression_number(p):
    '''expression : INTEIRO
                  | REAL'''

def p_expression_variable(p):
    '''expression : VARIAVEL'''

def p_expression_character(p):
    '''expression : CARACTER'''

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}:\nToken inesperado '{p.value}' | Tipo: {p.type}")
    else:
        print("Erro de sintaxe: EOF inesperado")

# Construir o parser
parser = yacc.yacc()