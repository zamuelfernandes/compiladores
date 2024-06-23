import ply.lex as lex

# Palavras Reservadas do Compilador
reserved = {
    'play': 'PLAY',
    'close': 'CLOSE',
    'int': 'RESERVADA',
    'char': 'RESERVADA',
    'real': 'RESERVADA',
    'read': 'ENTRADA',
    'write': 'SAIDA',
    'while': 'REPETICAO',
    'if': 'CASO',
    'else': 'CASOCONTRARIO'
}

# Lista para os nomes dos tokens. Esta parte é sempre Requerida pela Biblioteca PLY
tokens = [
    # Operadores Matemáticos
    'SOMA', 'SUB', 'MULT', 'DIV', 'RESTO',
    # Operadores de Execução
    'DOISPONTOS', 'PONTOVIRGULA', 'VIRGULA', 'PONTO',
    # Operadores de Impressão
    'ASPAS', 'COMENTARIO', 'FINALLINHA',
    # Operadores de Atribuição
    'NEGACAO', 'IGUAL', 'MAIS_IGUAL', 'MENOS_IGUAL', 'VEZES_IGUAL', 'DIVIDE_IGUAL',
    # Operadores Relacionais
    'MENOR', 'MAIOR', 'MENOR_IGUAL', 'MAIOR_IGUAL', 'DUPLO_IGUAL', 'DIFERENTE', 'E', 'OU',
    # Operadores de Prioridade
    'ABRE_PARENTESES', 'FECHA_PARENTESES', 'ABRE_COLCHETES', 'FECHA_COLCHETES', 'ABRE_CHAVES', 'FECHA_CHAVES',
    # Identificadores
    'INTEIRO', 'REAL', 'CARACTER', 'VARIAVEL',
    # Tokens malformados
    'variavel_mf', 'numero_mf', 'string_mf'
] + list(reserved.values())  # Concateno com as palavras reservadas para verificação

# Regras de expressão regular (RegEx) para tokens simples
t_SOMA = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_RESTO = r'%'

t_DOISPONTOS = r':'
t_PONTOVIRGULA = r';'
t_VIRGULA = r','
t_PONTO = r'\.'

t_ASPAS = r'\"'
t_COMENTARIO = r'\#.*'

t_NEGACAO = r'\~'
t_IGUAL = r'='
t_MAIS_IGUAL = r'\+='
t_MENOS_IGUAL = r'-='
t_VEZES_IGUAL = r'\*='
t_DIVIDE_IGUAL = r'/='

t_MENOR = r'<'
t_MAIOR = r'>'
t_MENOR_IGUAL = r'<='
t_MAIOR_IGUAL = r'>='
t_DUPLO_IGUAL = r'=='
t_DIFERENTE = r'!='
t_E = r'&'
t_OU = r'\|'

t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_ABRE_COLCHETES = r'\['
t_FECHA_COLCHETES = r'\]'
t_ABRE_CHAVES = r'\{'
t_FECHA_CHAVES = r'\}'

# Ignorar espaços e tabulação
t_ignore = ' \t'

# Regras de expressão regular (RegEx) para tokens mais "complexos"
def t_REAL(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CARACTER(t):
    r"'[a-zA-Z0-9]'"
    t.value = t.value[1]
    return t

def t_VARIAVEL(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIAVEL')  # Verifica se é uma palavra reservada
    return t

def t_string_mf(t):
    r'("[^"]*)'
    return t

def t_variavel_mf(t):
    r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
    return t

def t_numero_mf(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    return t

# Define uma regra para que seja possível rastrear o número de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_FINALLINHA(t):
    r'\''
    t.lexer.lineno += len(t.value)
    return t

# Regra de tratamento de erros
erroslexicos = []

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    erroslexicos.append(t)
    t.lexer.skip(1)

# Constrói o lexer
lexer = lex.lex()

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

# Constrói o parser
parser = yacc.yacc()

# Teste do analisador sintático
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
    
    result = parser.parse(data)
    print("Análise sintática concluída!")
