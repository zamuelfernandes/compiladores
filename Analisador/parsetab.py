
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABREPARENTESE AND ASPAS ATRIBUICAO CARACTER CASO CASOCONTRARIO CLOSE COMENTARIO DIFERENTE DIV DOISPONTOS DUPLOIGUAL ENTRADA FECHAPARENTESE FIMBLOCO FINALLINHA INICIOBLOCO INTEIRO MAIOR MAIORIGUAL MENOR MENORIGUAL MULT NOT OR PLAY PONTO PONTOVIRGULA REAL REPETICAO RESTO SAIDA SOMA SUB TIPO_CARACTER TIPO_INTEIRO TIPO_REAL VARIAVEL VIRGULAprograma : PLAY estados CLOSEestados : estados estadoestados : estadoestado : REPETICAO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCOestado : CASO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCO\n                 | CASO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCO CASOCONTRARIO INICIOBLOCO estados FIMBLOCOestado : VARIAVEL ATRIBUICAO expressao PONTOVIRGULA\n                 | VARIAVEL ATRIBUICAO INTEIRO PONTOVIRGULA\n                 | VARIAVEL ATRIBUICAO REAL PONTOVIRGULA\n                 | VARIAVEL ATRIBUICAO CARACTER PONTOVIRGULA\n                 | VARIAVEL ATRIBUICAO VARIAVEL PONTOVIRGULAestado : TIPO_INTEIRO VARIAVEL PONTOVIRGULA\n                 | TIPO_REAL VARIAVEL PONTOVIRGULA\n                 | TIPO_CARACTER VARIAVEL PONTOVIRGULAestado : ENTRADA ABREPARENTESE VARIAVEL FECHAPARENTESE PONTOVIRGULA\n                 | SAIDA ABREPARENTESE expressao FECHAPARENTESE PONTOVIRGULAexpressao : expressao SOMA expressao\n                  | expressao SUB expressao\n                  | expressao MULT expressao\n                  | expressao DIV expressao\n                  | expressao RESTO expressaoexpressao : expressao MENOR expressao\n                  | expressao MAIOR expressao\n                  | expressao MENORIGUAL expressao\n                  | expressao MAIORIGUAL expressao\n                  | expressao DUPLOIGUAL expressao\n                  | expressao DIFERENTE expressaoexpressao : ABREPARENTESE expressao FECHAPARENTESEexpressao : INTEIRO\n                  | REALexpressao : VARIAVELexpressao : CARACTER'
    
_lr_action_items = {'PLAY':([0,],[2,]),'$end':([1,13,],[0,-1,]),'REPETICAO':([2,3,4,14,35,36,37,54,55,56,57,58,62,74,75,76,77,78,79,80,82,83,84,],[5,5,-3,-2,-12,-13,-14,-11,-7,-8,-9,-10,5,5,-15,-16,5,5,-4,-5,5,5,-6,]),'CASO':([2,3,4,14,35,36,37,54,55,56,57,58,62,74,75,76,77,78,79,80,82,83,84,],[6,6,-3,-2,-12,-13,-14,-11,-7,-8,-9,-10,6,6,-15,-16,6,6,-4,-5,6,6,-6,]),'VARIAVEL':([2,3,4,8,9,10,14,15,16,17,21,22,23,35,36,37,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,62,74,75,76,77,78,79,80,82,83,84,],[7,7,-3,18,19,20,-2,27,27,30,38,27,27,-12,-13,-14,27,27,27,27,27,27,27,27,27,27,27,-11,-7,-8,-9,-10,7,7,-15,-16,7,7,-4,-5,7,7,-6,]),'TIPO_INTEIRO':([2,3,4,14,35,36,37,54,55,56,57,58,62,74,75,76,77,78,79,80,82,83,84,],[8,8,-3,-2,-12,-13,-14,-11,-7,-8,-9,-10,8,8,-15,-16,8,8,-4,-5,8,8,-6,]),'TIPO_REAL':([2,3,4,14,35,36,37,54,55,56,57,58,62,74,75,76,77,78,79,80,82,83,84,],[9,9,-3,-2,-12,-13,-14,-11,-7,-8,-9,-10,9,9,-15,-16,9,9,-4,-5,9,9,-6,]),'TIPO_CARACTER':([2,3,4,14,35,36,37,54,55,56,57,58,62,74,75,76,77,78,79,80,82,83,84,],[10,10,-3,-2,-12,-13,-14,-11,-7,-8,-9,-10,10,10,-15,-16,10,10,-4,-5,10,10,-6,]),'ENTRADA':([2,3,4,14,35,36,37,54,55,56,57,58,62,74,75,76,77,78,79,80,82,83,84,],[11,11,-3,-2,-12,-13,-14,-11,-7,-8,-9,-10,11,11,-15,-16,11,11,-4,-5,11,11,-6,]),'SAIDA':([2,3,4,14,35,36,37,54,55,56,57,58,62,74,75,76,77,78,79,80,82,83,84,],[12,12,-3,-2,-12,-13,-14,-11,-7,-8,-9,-10,12,12,-15,-16,12,12,-4,-5,12,12,-6,]),'CLOSE':([3,4,14,35,36,37,54,55,56,57,58,75,76,79,80,84,],[13,-3,-2,-12,-13,-14,-11,-7,-8,-9,-10,-15,-16,-4,-5,-6,]),'FIMBLOCO':([4,14,35,36,37,54,55,56,57,58,75,76,77,78,79,80,83,84,],[-3,-2,-12,-13,-14,-11,-7,-8,-9,-10,-15,-16,79,80,-4,-5,84,-6,]),'ABREPARENTESE':([5,6,11,12,15,16,17,22,23,42,43,44,45,46,47,48,49,50,51,52,],[15,16,21,22,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'ATRIBUICAO':([7,],[17,]),'INTEIRO':([15,16,17,22,23,42,43,44,45,46,47,48,49,50,51,52,],[25,25,32,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'REAL':([15,16,17,22,23,42,43,44,45,46,47,48,49,50,51,52,],[26,26,33,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'CARACTER':([15,16,17,22,23,42,43,44,45,46,47,48,49,50,51,52,],[28,28,34,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'PONTOVIRGULA':([18,19,20,25,26,27,28,30,31,32,33,34,59,60,61,63,64,65,66,67,68,69,70,71,72,73,],[35,36,37,-29,-30,-31,-32,54,55,56,57,58,75,76,-28,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,]),'FECHAPARENTESE':([24,25,26,27,28,29,38,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[41,-29,-30,-31,-32,53,59,60,61,-28,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,]),'SOMA':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[42,-29,-30,-31,-32,42,-31,42,-29,-30,-32,42,42,-28,42,42,42,42,42,42,42,42,42,42,42,]),'SUB':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[43,-29,-30,-31,-32,43,-31,43,-29,-30,-32,43,43,-28,43,43,43,43,43,43,43,43,43,43,43,]),'MULT':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[44,-29,-30,-31,-32,44,-31,44,-29,-30,-32,44,44,-28,44,44,44,44,44,44,44,44,44,44,44,]),'DIV':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[45,-29,-30,-31,-32,45,-31,45,-29,-30,-32,45,45,-28,45,45,45,45,45,45,45,45,45,45,45,]),'RESTO':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[46,-29,-30,-31,-32,46,-31,46,-29,-30,-32,46,46,-28,46,46,46,46,46,46,46,46,46,46,46,]),'MENOR':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[47,-29,-30,-31,-32,47,-31,47,-29,-30,-32,47,47,-28,47,47,47,47,47,47,47,47,47,47,47,]),'MAIOR':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[48,-29,-30,-31,-32,48,-31,48,-29,-30,-32,48,48,-28,48,48,48,48,48,48,48,48,48,48,48,]),'MENORIGUAL':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[49,-29,-30,-31,-32,49,-31,49,-29,-30,-32,49,49,-28,49,49,49,49,49,49,49,49,49,49,49,]),'MAIORIGUAL':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[50,-29,-30,-31,-32,50,-31,50,-29,-30,-32,50,50,-28,50,50,50,50,50,50,50,50,50,50,50,]),'DUPLOIGUAL':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[51,-29,-30,-31,-32,51,-31,51,-29,-30,-32,51,51,-28,51,51,51,51,51,51,51,51,51,51,51,]),'DIFERENTE':([24,25,26,27,28,29,30,31,32,33,34,39,40,61,63,64,65,66,67,68,69,70,71,72,73,],[52,-29,-30,-31,-32,52,-31,52,-29,-30,-32,52,52,-28,52,52,52,52,52,52,52,52,52,52,52,]),'INICIOBLOCO':([41,53,81,],[62,74,82,]),'CASOCONTRARIO':([80,],[81,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'estados':([2,62,74,82,],[3,77,78,83,]),'estado':([2,3,62,74,77,78,82,83,],[4,14,4,4,14,14,4,14,]),'expressao':([15,16,17,22,23,42,43,44,45,46,47,48,49,50,51,52,],[24,29,31,39,40,63,64,65,66,67,68,69,70,71,72,73,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PLAY estados CLOSE','programa',3,'p_programa','sint_analyzer.py',6),
  ('estados -> estados estado','estados',2,'p_estados_multiple','sint_analyzer.py',9),
  ('estados -> estado','estados',1,'p_estados_single','sint_analyzer.py',12),
  ('estado -> REPETICAO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCO','estado',7,'p_estado_while','sint_analyzer.py',15),
  ('estado -> CASO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCO','estado',7,'p_estado_if','sint_analyzer.py',18),
  ('estado -> CASO ABREPARENTESE expressao FECHAPARENTESE INICIOBLOCO estados FIMBLOCO CASOCONTRARIO INICIOBLOCO estados FIMBLOCO','estado',11,'p_estado_if','sint_analyzer.py',19),
  ('estado -> VARIAVEL ATRIBUICAO expressao PONTOVIRGULA','estado',4,'p_estado_assignment','sint_analyzer.py',22),
  ('estado -> VARIAVEL ATRIBUICAO INTEIRO PONTOVIRGULA','estado',4,'p_estado_assignment','sint_analyzer.py',23),
  ('estado -> VARIAVEL ATRIBUICAO REAL PONTOVIRGULA','estado',4,'p_estado_assignment','sint_analyzer.py',24),
  ('estado -> VARIAVEL ATRIBUICAO CARACTER PONTOVIRGULA','estado',4,'p_estado_assignment','sint_analyzer.py',25),
  ('estado -> VARIAVEL ATRIBUICAO VARIAVEL PONTOVIRGULA','estado',4,'p_estado_assignment','sint_analyzer.py',26),
  ('estado -> TIPO_INTEIRO VARIAVEL PONTOVIRGULA','estado',3,'p_estado_declaration','sint_analyzer.py',29),
  ('estado -> TIPO_REAL VARIAVEL PONTOVIRGULA','estado',3,'p_estado_declaration','sint_analyzer.py',30),
  ('estado -> TIPO_CARACTER VARIAVEL PONTOVIRGULA','estado',3,'p_estado_declaration','sint_analyzer.py',31),
  ('estado -> ENTRADA ABREPARENTESE VARIAVEL FECHAPARENTESE PONTOVIRGULA','estado',5,'p_estado_io','sint_analyzer.py',34),
  ('estado -> SAIDA ABREPARENTESE expressao FECHAPARENTESE PONTOVIRGULA','estado',5,'p_estado_io','sint_analyzer.py',35),
  ('expressao -> expressao SOMA expressao','expressao',3,'p_expressao_binop','sint_analyzer.py',38),
  ('expressao -> expressao SUB expressao','expressao',3,'p_expressao_binop','sint_analyzer.py',39),
  ('expressao -> expressao MULT expressao','expressao',3,'p_expressao_binop','sint_analyzer.py',40),
  ('expressao -> expressao DIV expressao','expressao',3,'p_expressao_binop','sint_analyzer.py',41),
  ('expressao -> expressao RESTO expressao','expressao',3,'p_expressao_binop','sint_analyzer.py',42),
  ('expressao -> expressao MENOR expressao','expressao',3,'p_expressao_relational','sint_analyzer.py',45),
  ('expressao -> expressao MAIOR expressao','expressao',3,'p_expressao_relational','sint_analyzer.py',46),
  ('expressao -> expressao MENORIGUAL expressao','expressao',3,'p_expressao_relational','sint_analyzer.py',47),
  ('expressao -> expressao MAIORIGUAL expressao','expressao',3,'p_expressao_relational','sint_analyzer.py',48),
  ('expressao -> expressao DUPLOIGUAL expressao','expressao',3,'p_expressao_relational','sint_analyzer.py',49),
  ('expressao -> expressao DIFERENTE expressao','expressao',3,'p_expressao_relational','sint_analyzer.py',50),
  ('expressao -> ABREPARENTESE expressao FECHAPARENTESE','expressao',3,'p_expressao_group','sint_analyzer.py',53),
  ('expressao -> INTEIRO','expressao',1,'p_expressao_number','sint_analyzer.py',56),
  ('expressao -> REAL','expressao',1,'p_expressao_number','sint_analyzer.py',57),
  ('expressao -> VARIAVEL','expressao',1,'p_expressao_variable','sint_analyzer.py',60),
  ('expressao -> CARACTER','expressao',1,'p_expressao_character','sint_analyzer.py',63),
]
