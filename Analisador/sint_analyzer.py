import ply.yacc as yacc
from lex_analyzer import tokens

# Regras de produção para o analisador sintático

def p_programa(p):
    '''programa : PLAY declarativas estados CLOSE'''
    p[0] = ('programa', p[2], p[3])

def p_declarativas(p):
    '''declarativas : declarativas declarativa
                    | vazio'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_declarativa(p):
    '''declarativa : tipo VARIAVEL PONTOVIRGULA'''
    p[0] = ('declarativa', p[1], p[2])

def p_tipo(p):
    '''tipo : RESERVADA'''
    p[0] = p[1]

def p_estados(p):
    '''estados : estados estado
                  | vazio'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_estado(p):
    '''estado : assinalar_estado
                 | se_estado
                 | repeticao_estado
                 | io_estado'''
    p[0] = p[1]

def p_assinalar_estado(p):
    '''assinalar_estado : VARIAVEL ATRIBUICAO expressao PONTOVIRGULA'''
    p[0] = ('assinalar', p[1], p[3])

def p_se_estado(p):
    '''se_estado : CASO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCO senao_estado'''
    p[0] = ('se', p[3], p[6], p[8])

def p_senao_estado(p):
    '''senao_estado : CASOCONTRARIO INICIOBLOCO estados FIMBLOCO
                      | vazio'''
    if len(p) == 5:
        p[0] = ('senao', p[3])
    else:
        p[0] = None

def p_repeticao_estado(p): #while
    '''repeticao_estado : REPETICAO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCO'''
    p[0] = ('repeticao', p[3], p[6])

def p_io_estado(p):
    '''io_estado : ENTRADA ABREPARENTESE VARIAVEL FECHAPARENTESE PONTOVIRGULA
                    | SAIDA ABREPARENTESE expressao FECHAPARENTESE PONTOVIRGULA'''
    p[0] = ('io', p[1], p[3])

def p_expressao(p):
    '''expressao : termo
                  | expressao SOMA termo
                  | expressao SUB termo
                  | expressao MENOR termo
                  | expressao MAIOR termo
                  | expressao MENORIGUAL termo
                  | expressao MAIORIGUAL termo
                  | expressao DUPLOIGUAL termo
                  | expressao DIFERENTE termo
                  | expressao AND termo
                  | expressao OR termo'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('expressao', p[2], p[1], p[3])

def p_termo(p):
    '''termo : fator
            | termo MULT fator
            | termo DIV fator
            | termo RESTO fator'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('termo', p[2], p[1], p[3])

def p_fator(p):
    '''fator : VARIAVEL
              | INTEIRO
              | REAL
              | ABREPARENTESE expressao FECHAPARENTESE'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_vazio(p):
    '''vazio :'''
    p[0] = None

# Tratamento de erros sintáticos
def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

# Constrói o parser
parser = yacc.yacc()
