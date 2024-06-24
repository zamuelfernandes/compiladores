import ply.lex as lex

reserved = {
    'play': 'PLAY',
    'close': 'CLOSE',
    'read': 'ENTRADA',
    'write': 'SAIDA',
    'while': 'REPETICAO',
    'if': 'CASO',
    'else': 'CASOCONTRARIO',
    'int': 'TIPO_INTEIRO',
    'real': 'TIPO_REAL',
    'char': 'TIPO_CARACTER'
}

# Lista de Tokens
tokens = [
    #Matemáticos
    'SOMA', 'SUB', 'MULT', 'DIV', 'RESTO', 

    # Impressão 
    'ASPAS', 'COMENTARIO', 'FINALLINHA',

    # Atribuição 
    'ATRIBUICAO',

    # Relacionais
    'MENOR', 'MAIOR', 'MENORIGUAL', 'MAIORIGUAL', 'DUPLOIGUAL', 'DIFERENTE', 'AND', 'OR', 'NOT',

    # Identificadores
    'INTEIRO', 'REAL', 'CARACTER', 'VARIAVEL',
    
    # Outros
    'VIRGULA', 'PONTO', 'DOISPONTOS', 'PONTOVIRGULA', 'ABREPARENTESE', 'FECHAPARENTESE', 'INICIOBLOCO', 'FIMBLOCO',
] + list(reserved.values())  # Concateno com as palavras reservadas para verificação

# Regras de (RegEx) para tokens simples
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

t_ignore = ' \t' # Ignorar espaços em branco e tabulações

# Regras de (RegEx) para tokens mais "complexos"
def t_VARIAVEL(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
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
    print(f"String malformada: {t.value} na linha {t.lineno}")
    return t

def t_variavel_mf(t):
    r'([0-9]+[a-z]+)|([@!#$%&]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&]+)'
    print(f"Variável malformada: {t.value} na linha {t.lineno}")
    return t

def t_numero_mf(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    print(f"Número malformado: {t.value} na linha {t.lineno}")
    return t

# Rastrear o números de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_FINALLINHA(t):
    r'\''
    t.lexer.lineno += len(t.value)
    return t

# Tratamento de erros
erroslexicos = []

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    erroslexicos.append(t)
    t.type = 'ILEGAL'
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

# Constrói o lexer
lexer = lex.lex()