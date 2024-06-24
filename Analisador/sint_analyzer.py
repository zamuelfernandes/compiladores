import ply.yacc as yacc
from lex_analyzer import tokens

# Definição das regras de produção
def p_programa(p):
    '''programa : PLAY estados CLOSE'''

def p_estados_multiple(p):
    '''estados : estados estado'''

def p_estados_single(p):
    '''estados : estado'''

def p_estado_while(p):
    '''estado : REPETICAO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCO'''

def p_estado_if(p):
    '''estado : CASO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCO
                 | CASO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCO CASOCONTRARIO INICIOBLOCO estados FIMBLOCO'''

def p_estado_assignment(p):
    '''estado : VARIAVEL ATRIBUICAO expressao PONTOVIRGULA
                 | VARIAVEL ATRIBUICAO INTEIRO PONTOVIRGULA
                 | VARIAVEL ATRIBUICAO REAL PONTOVIRGULA
                 | VARIAVEL ATRIBUICAO CARACTER PONTOVIRGULA
                 | VARIAVEL ATRIBUICAO VARIAVEL PONTOVIRGULA'''

def p_estado_declaration(p):
    '''estado : TIPO_INTEIRO VARIAVEL PONTOVIRGULA
                 | TIPO_REAL VARIAVEL PONTOVIRGULA
                 | TIPO_CARACTER VARIAVEL PONTOVIRGULA'''

def p_estado_io(p):
    '''estado : ENTRADA ABREPARENTESE VARIAVEL FECHAPARENTESE PONTOVIRGULA
                 | SAIDA ABREPARENTESE expressao FECHAPARENTESE PONTOVIRGULA'''

def p_expressao_binop(p):
    '''expressao : expressao SOMA expressao
                  | expressao SUB expressao
                  | expressao MULT expressao
                  | expressao DIV expressao
                  | expressao RESTO expressao'''

def p_expressao_relational(p):
    '''expressao : expressao MENOR expressao
                  | expressao MAIOR expressao
                  | expressao MENORIGUAL expressao
                  | expressao MAIORIGUAL expressao
                  | expressao DUPLOIGUAL expressao
                  | expressao DIFERENTE expressao'''

def p_expressao_group(p):
    '''expressao : ABREPARENTESE expressao FECHAPARENTESE'''

def p_expressao_number(p):
    '''expressao : INTEIRO
                  | REAL'''

def p_expressao_variable(p):
    '''expressao : VARIAVEL'''

def p_expressao_character(p):
    '''expressao : CARACTER'''

erros_sintaticos = []

def p_error(p):
    if p:
        erro = f"Erro de sintaxe na linha {p.lineno}: Token inesperado '{p.value}' | Tipo: {p.type}"
        print(erro)
        erros_sintaticos.append(erro)
    else:
        erro = "Erro de sintaxe: EOF inesperado"
        print(erro)
        erros_sintaticos.append(erro)

# Construir o parser
parser = yacc.yacc()