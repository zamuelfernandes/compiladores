
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABREPARENTESE AND ASPAS ATRIBUICAO CARACTER CASO CASOCONTRARIO CLOSE COMENTARIO DIFERENTE DIV DOISPONTOS DUPLOIGUAL ENTRADA FECHAPARENTESE FIMBLOCO FINALLINHA INICIOBLOCO INTEIRO MAIOR MAIORIGUAL MENOR MENORIGUAL MULT NOT OR PLAY PONTO PONTOVIRGULA REAL REPETICAO RESERVADA RESTO SAIDA SOMA SUB VARIAVEL VIRGULA numero_mf string_mf variavel_mfprogram : PLAY statements CLOSEstatements : statements statementstatements : statementstatement : REPETICAO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCOstatement : CASO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO\n                 | CASO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO CASOCONTRARIO INICIOBLOCO statements FIMBLOCOstatement : VARIAVEL ATRIBUICAO expression PONTOVIRGULA\n                 | VARIAVEL ATRIBUICAO INTEIRO PONTOVIRGULA\n                 | VARIAVEL ATRIBUICAO REAL PONTOVIRGULA\n                 | VARIAVEL ATRIBUICAO CARACTER PONTOVIRGULA\n                 | VARIAVEL ATRIBUICAO VARIAVEL PONTOVIRGULAstatement : ENTRADA ABREPARENTESE VARIAVEL FECHAPARENTESE PONTOVIRGULA\n                 | SAIDA ABREPARENTESE expression FECHAPARENTESE PONTOVIRGULAexpression : expression SOMA expression\n                  | expression SUB expression\n                  | expression MULT expression\n                  | expression DIV expression\n                  | expression RESTO expressionexpression : ABREPARENTESE expression FECHAPARENTESEexpression : INTEIRO\n                  | REALexpression : VARIAVELexpression : CARACTER'
    
_lr_action_items = {'PLAY':([0,],[2,]),'$end':([1,10,],[0,-1,]),'REPETICAO':([2,3,4,11,39,40,41,42,43,47,53,54,55,56,57,58,59,61,62,63,],[5,5,-3,-2,-11,-7,-8,-9,-10,5,5,-12,-13,5,5,-4,-5,5,5,-6,]),'CASO':([2,3,4,11,39,40,41,42,43,47,53,54,55,56,57,58,59,61,62,63,],[6,6,-3,-2,-11,-7,-8,-9,-10,6,6,-12,-13,6,6,-4,-5,6,6,-6,]),'VARIAVEL':([2,3,4,11,12,13,14,15,16,17,33,34,35,36,37,39,40,41,42,43,47,53,54,55,56,57,58,59,61,62,63,],[7,7,-3,-2,21,21,24,29,21,21,21,21,21,21,21,-11,-7,-8,-9,-10,7,7,-12,-13,7,7,-4,-5,7,7,-6,]),'ENTRADA':([2,3,4,11,39,40,41,42,43,47,53,54,55,56,57,58,59,61,62,63,],[8,8,-3,-2,-11,-7,-8,-9,-10,8,8,-12,-13,8,8,-4,-5,8,8,-6,]),'SAIDA':([2,3,4,11,39,40,41,42,43,47,53,54,55,56,57,58,59,61,62,63,],[9,9,-3,-2,-11,-7,-8,-9,-10,9,9,-12,-13,9,9,-4,-5,9,9,-6,]),'CLOSE':([3,4,11,39,40,41,42,43,54,55,58,59,63,],[10,-3,-2,-11,-7,-8,-9,-10,-12,-13,-4,-5,-6,]),'FIMBLOCO':([4,11,39,40,41,42,43,54,55,56,57,58,59,62,63,],[-3,-2,-11,-7,-8,-9,-10,-12,-13,58,59,-4,-5,63,-6,]),'ABREPARENTESE':([5,6,8,9,12,13,14,16,17,33,34,35,36,37,],[12,13,15,16,17,17,17,17,17,17,17,17,17,17,]),'ATRIBUICAO':([7,],[14,]),'INTEIRO':([12,13,14,16,17,33,34,35,36,37,],[19,19,26,19,19,19,19,19,19,19,]),'REAL':([12,13,14,16,17,33,34,35,36,37,],[20,20,27,20,20,20,20,20,20,20,]),'CARACTER':([12,13,14,16,17,33,34,35,36,37,],[22,22,28,22,22,22,22,22,22,22,]),'FECHAPARENTESE':([18,19,20,21,22,23,29,30,31,46,48,49,50,51,52,],[32,-20,-21,-22,-23,38,44,45,46,-19,-14,-15,-16,-17,-18,]),'SOMA':([18,19,20,21,22,23,24,25,26,27,28,30,31,46,48,49,50,51,52,],[33,-20,-21,-22,-23,33,-22,33,-20,-21,-23,33,33,-19,33,33,33,33,33,]),'SUB':([18,19,20,21,22,23,24,25,26,27,28,30,31,46,48,49,50,51,52,],[34,-20,-21,-22,-23,34,-22,34,-20,-21,-23,34,34,-19,34,34,34,34,34,]),'MULT':([18,19,20,21,22,23,24,25,26,27,28,30,31,46,48,49,50,51,52,],[35,-20,-21,-22,-23,35,-22,35,-20,-21,-23,35,35,-19,35,35,35,35,35,]),'DIV':([18,19,20,21,22,23,24,25,26,27,28,30,31,46,48,49,50,51,52,],[36,-20,-21,-22,-23,36,-22,36,-20,-21,-23,36,36,-19,36,36,36,36,36,]),'RESTO':([18,19,20,21,22,23,24,25,26,27,28,30,31,46,48,49,50,51,52,],[37,-20,-21,-22,-23,37,-22,37,-20,-21,-23,37,37,-19,37,37,37,37,37,]),'PONTOVIRGULA':([19,20,21,22,24,25,26,27,28,44,45,46,48,49,50,51,52,],[-20,-21,-22,-23,39,40,41,42,43,54,55,-19,-14,-15,-16,-17,-18,]),'INICIOBLOCO':([32,38,60,],[47,53,61,]),'CASOCONTRARIO':([59,],[60,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([2,47,53,61,],[3,56,57,62,]),'statement':([2,3,47,53,56,57,61,62,],[4,11,4,4,11,11,4,11,]),'expression':([12,13,14,16,17,33,34,35,36,37,],[18,23,25,30,31,48,49,50,51,52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PLAY statements CLOSE','program',3,'p_program','sint_analyzer.py',7),
  ('statements -> statements statement','statements',2,'p_statements_multiple','sint_analyzer.py',10),
  ('statements -> statement','statements',1,'p_statements_single','sint_analyzer.py',13),
  ('statement -> REPETICAO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO','statement',7,'p_statement_while','sint_analyzer.py',16),
  ('statement -> CASO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO','statement',7,'p_statement_if','sint_analyzer.py',19),
  ('statement -> CASO ABREPARENTESE expression FECHAPARENTESE INICIOBLOCO statements FIMBLOCO CASOCONTRARIO INICIOBLOCO statements FIMBLOCO','statement',11,'p_statement_if','sint_analyzer.py',20),
  ('statement -> VARIAVEL ATRIBUICAO expression PONTOVIRGULA','statement',4,'p_statement_assignment','sint_analyzer.py',23),
  ('statement -> VARIAVEL ATRIBUICAO INTEIRO PONTOVIRGULA','statement',4,'p_statement_assignment','sint_analyzer.py',24),
  ('statement -> VARIAVEL ATRIBUICAO REAL PONTOVIRGULA','statement',4,'p_statement_assignment','sint_analyzer.py',25),
  ('statement -> VARIAVEL ATRIBUICAO CARACTER PONTOVIRGULA','statement',4,'p_statement_assignment','sint_analyzer.py',26),
  ('statement -> VARIAVEL ATRIBUICAO VARIAVEL PONTOVIRGULA','statement',4,'p_statement_assignment','sint_analyzer.py',27),
  ('statement -> ENTRADA ABREPARENTESE VARIAVEL FECHAPARENTESE PONTOVIRGULA','statement',5,'p_statement_io','sint_analyzer.py',30),
  ('statement -> SAIDA ABREPARENTESE expression FECHAPARENTESE PONTOVIRGULA','statement',5,'p_statement_io','sint_analyzer.py',31),
  ('expression -> expression SOMA expression','expression',3,'p_expression_binop','sint_analyzer.py',34),
  ('expression -> expression SUB expression','expression',3,'p_expression_binop','sint_analyzer.py',35),
  ('expression -> expression MULT expression','expression',3,'p_expression_binop','sint_analyzer.py',36),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','sint_analyzer.py',37),
  ('expression -> expression RESTO expression','expression',3,'p_expression_binop','sint_analyzer.py',38),
  ('expression -> ABREPARENTESE expression FECHAPARENTESE','expression',3,'p_expression_group','sint_analyzer.py',41),
  ('expression -> INTEIRO','expression',1,'p_expression_number','sint_analyzer.py',44),
  ('expression -> REAL','expression',1,'p_expression_number','sint_analyzer.py',45),
  ('expression -> VARIAVEL','expression',1,'p_expression_variable','sint_analyzer.py',48),
  ('expression -> CARACTER','expression',1,'p_expression_character','sint_analyzer.py',51),
]
