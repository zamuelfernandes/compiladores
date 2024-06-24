# Projeto de Compiladores

## Descrição do Projeto

Este projeto tem como objetivo a construção de um analisador léxico e sintático para a nossa linguagem de programação. A linguagem, chamada `MiniLang`, possui um conjunto definido de palavras reservadas, operadores e regras gramaticais.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `lex_analyzer.py`: Contém o código do analisador léxico.
- `sint_analyzer.py`: Contém o código do analisador sintático.
- `test_lexer.py`: Script para testar o analisador léxico.
- `test_parser.py`: Script para testar o analisador sintático.
- `example_programs/`: Pasta contendo programas de exemplo na linguagem `MiniLang`.

## Requisitos

Para executar este projeto, você precisará ter o Python e a biblioteca PLY instalados. Você pode instalá-los usando:

```bash
pip install ply
```

## Analisador Léxico

O analisador léxico é responsável por dividir o código-fonte em tokens. Ele reconhece palavras reservadas, operadores, delimitadores e identificadores específicos da linguagem.

#### Palavras reservadas

As palavras reservadas da linguagem incluem:

- `play`
- `close`
- `read`
- `write`
- `while`
- `if`
- `else`

#### Operadores e Delimitadores

Os operadores incluem soma, subtração, multiplicação, divisão, entre outros. Delimitadores como ponto-e-vírgula, dois pontos, vírgula, e ponto também são reconhecidos.

#### Testando o Analisador Léxico

Para testar o analisador léxico, execute o script test_lexer.py:

```bash
python test_lexer.py
```

## Analisador Sintático

O analisador sintático verifica a estrutura gramatical do código-fonte, assegurando que ele siga as regras da linguagem.

#### Regras Gramaticais

As regras gramaticais definem como instruções, expressões e blocos de código são estruturados na linguagem. Exemplos de estruturas gramaticais incluem:

- Declarações condicionais
- Laços de repetição
- Atribuições e expressões aritméticas

#### Testando o Analisador Sintático

Para testar o analisador sintático, execute o script test_parser.py:

```bash
python test_parser.py
```

## Programas de Exemplo

A pasta example_programs/ contém exemplos de programas escritos em MiniLang para ajudar a ilustrar como a linguagem funciona. Estes exemplos podem ser usados para testar tanto o analisador léxico quanto o sintático.

#### Exemplo 1: Entrada e Saída

```bash
play
    int x;
    int y;
    read(x);
    read(y);
    write(x + y);
close
```

#### Exemplo 2: Comando Condicional

```bash
play
    int a;
    int b;
    int max;
    read(a);
    read(b);
    if (a > b) {
        max <- a;
    } else {
        max <- b;
    }
    write(max);
close
```

#### Exemplo 3: Laço de Repetição

```bash
play
    int i;
    int sum;
    sum <- 0;
    i <- 1;
    while (i <= 10) {
        sum <- sum + i;
        i <- i + 1;
    }
    write(sum);
close
```

## Autor

Este projeto foi desenvolvido por Samuel Fernandes e Bianca Rossi
