import ply.lex as lex

reserved = {
    'play': 'PLAY',
    'close': 'CLOSE',
    'read': 'ENTRADA',
    'write': 'SAIDA',
    'while': 'REPETICAO',
    'if': 'CASO',
    'else': 'CASOCONTRARIO'
}

# lista dos tokens
tokens = [
    'SOMA', 'SUB', 'MULT', 'DIV', 'RESTO', # op matematicos
    'DOISPONTOS', 'PONTOVIRGULA', 

    # No nosso trabalho é separador
    'VIRGULA', 'PONTO',

    # Operadores de Impressão 
    'ASPAS', 'COMENTARIO', 'FINALLINHA',

    # Operadores de Atribuição 
    'ATRIBUICAO',

    # Operadores Relacionais
    'MENOR', 'MAIOR', 'MENORIGUAL', 'MAIORIGUAL', 'DUPLOIGUAL', 'DIFERENTE', 'AND', 'OR', 'NOT',
   
    # Operadores de Prioridade
    'ABREPARENTESE', 'FECHAPARENTESE', 'INICIOBLOCO', 'FIMBLOCO',
   
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

t_ATRIBUICAO = r'<-'

t_MENOR = r'<'
t_MAIOR = r'>'
t_MENORIGUAL = r'<='
t_MAIORIGUAL = r'>='
t_DUPLOIGUAL = r'=='
t_DIFERENTE = r'!='
t_AND = r'&'
t_OR = r'\|'
t_NOT = r'!'

t_ABREPARENTESE = r'\('
t_FECHAPARENTESE = r'\)'
t_INICIOBLOCO = r'\{'
t_FIMBLOCO = r'\}'

# Regras de expressão regular (RegEx) para tokens mais "complexos"
def t_VARIAVEL(t):
    r'[a-zA-Z]+(\d*[a-zA-Z]*)*'
    t.type = reserved.get(t.value, 'VARIAVEL')
    return t

def t_INTEIRO(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_REAL(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CARACTER(t):
    r"'[a-zA-Z0-9]'"
    t.value = t.value[1]
    return t

def t_string_mf(t):
    r'("[^"]*)'
    print(f"String malformada: {t.value}")
    return t

def t_variavel_mf(t):
    r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
    print(f"Variável malformada: {t.value}")
    return t

def t_numero_mf(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    print(f"Número malformado: {t.value}")
    return t

# Regra de tratamento de erros
erroslexicos = []

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    erroslexicos.append(t)
    t.lexer.skip(1)

# Constrói o lexer
lexer = lex.lex()