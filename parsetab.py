
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMAACT AIGUAL AND AS BEGIN CLEAR COMA DIV DOSPUNTOS END ENDWHILST ET FLOAT FOR GIVE ID IGUAL INCOMING JUMP LOOP MAS MAYOR MAYORI MENOR MENORI MENOS MULT NOIGUAL NOWHERE NUM OR OTHER PARENTESISF PARENTESISI PRINT PUT RETURN STRING SUBMETHOD TAKE TEMPORAL THEN TILL TRAVEL UNTIL WHEREVER WHILST WORD\n    PROGRAMA : V R BEGIN B END R\n    \n    V : PUT VAR AS TYPE V\n    |\n    \n    TYPE : FLOAT\n    | WORD\n    \n    VAR : VEC\n    | VAR COMA VAR\n    \n    VALUE : ID\n    | NUM\n    \n    VEC : ID\n    | ID PARENTESISI VALUE PARENTESISF\n    | ID PARENTESISI VALUE COMA VALUE PARENTESISF\n    | ID PARENTESISI VALUE COMA VALUE COMA VALUE PARENTESISF\n    \n    R : SUBMETHOD ID B RETURN R\n    |\n    \n    B : CLEAR B\n    | ET ID B\n    | JUMP ID B\n    | TRAVEL ID B\n    | PRINT MENS B\n    | READ B\n    | GIVE EXPR B\n    | IF B\n    | LOOPWHILE B\n    | LOOPFOR B\n    | LOOPDO B\n    |\n    \n    READ : TAKE STRING DOSPUNTOS ID\n    \n    LOOPFOR : FORID EXP1 EXP2 DOSPUNTOS B INCOMING ID\n    \n    EXP2 : TILL EA\n    \n    EXP1 : AIGUAL EA\n    \n    FORID : FOR ID \n    \n    LOOPDO : DO DOSPUNTOS B LOOP UNTIL PARENTESISI EL PARENTESISF \n    \n    DO : ACT  \n    \n    LOOPWHILE : WHILE LOGIC DOSPUNTOS B ENDWHILST \n    \n    WHILE : WHILST\n    \n    IF : WHEREVER LOGIC THEN B ELSE B NOWHERE \n    | WHEREVER LOGIC THEN B NOWHERE \n    \n    ELSE : OTHER\n    \n    LOGIC : EL\n    \n    EXPR : VEC AIGUAL EA\n    \n    ASGN : NUM\n    | VEC\n    | MENOS NUM\n    \n    MENS : VEC\n    | PARENTESISI STRING PARENTESISF\n    | PARENTESISI STRING PARENTESISF DOSPUNTOS VEC\n    \n    EA : TA\n    | EA MAS TA\n    | EA MENOS TA\n    \n    TA : FA\n    | TA MULT FA\n    | TA DIV FA\n    \n    FA : ASGN\n    | PARENTESISI EA PARENTESISF\n    \n    EL : TL\n    | EL OR TL\n    | EL AND TL\n    \n    TL : FL\n    | TL COND FL\n    \n    FL : ASGN\n    | PARENTESISI EL PARENTESISF\n    \n    COND : IGUAL\n    | NOIGUAL\n    | MAYOR\n    | MENOR\n    | MAYORI\n    | MENORI\n    '
    
_lr_action_items = {'PUT':([0,35,36,37,],[3,3,-4,-5,]),'SUBMETHOD':([0,2,35,36,37,42,72,73,],[-3,5,-3,-4,-5,5,5,-2,]),'BEGIN':([0,2,4,35,36,37,72,73,106,],[-3,-15,9,-3,-4,-5,-15,-2,-14,]),'$end':([1,42,72,76,106,],[0,-15,-15,-1,-14,]),'ID':([3,5,12,13,16,17,18,19,21,27,28,31,32,63,69,75,83,84,86,87,88,89,90,91,92,93,94,99,104,119,120,121,122,125,127,142,143,],[8,10,8,39,44,45,46,8,8,8,8,-36,71,8,8,39,8,110,8,8,8,-63,-64,-65,-66,-67,-68,8,8,8,8,8,8,39,8,146,8,]),'AS':([6,7,8,38,74,126,144,],[11,-6,-10,-7,-11,-12,-13,]),'COMA':([6,7,8,38,39,40,41,74,107,126,144,],[12,-6,-10,12,-8,75,-9,-11,125,-12,-13,]),'CLEAR':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,15,15,15,15,15,15,15,15,15,15,15,15,-45,15,-42,-43,15,-11,15,-44,15,-48,-51,-54,-46,-41,-28,15,-12,15,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'ET':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,16,16,16,16,16,16,16,16,16,16,16,16,-45,16,-42,-43,16,-11,16,-44,16,-48,-51,-54,-46,-41,-28,16,-12,16,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'JUMP':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,17,17,17,17,17,17,17,17,17,17,17,17,-45,17,-42,-43,17,-11,17,-44,17,-48,-51,-54,-46,-41,-28,17,-12,17,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'TRAVEL':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,18,18,18,18,18,18,18,18,18,18,18,18,-45,18,-42,-43,18,-11,18,-44,18,-48,-51,-54,-46,-41,-28,18,-12,18,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'PRINT':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,19,19,19,19,19,19,19,19,19,19,19,19,-45,19,-42,-43,19,-11,19,-44,19,-48,-51,-54,-46,-41,-28,19,-12,19,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'GIVE':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,21,21,21,21,21,21,21,21,21,21,21,21,-45,21,-42,-43,21,-11,21,-44,21,-48,-51,-54,-46,-41,-28,21,-12,21,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'TAKE':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,26,26,26,26,26,26,26,26,26,26,26,26,-45,26,-42,-43,26,-11,26,-44,26,-48,-51,-54,-46,-41,-28,26,-12,26,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'WHEREVER':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,27,27,27,27,27,27,27,27,27,27,27,27,-45,27,-42,-43,27,-11,27,-44,27,-48,-51,-54,-46,-41,-28,27,-12,27,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'WHILST':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,31,31,31,31,31,31,31,31,31,31,31,31,-45,31,-42,-43,31,-11,31,-44,31,-48,-51,-54,-46,-41,-28,31,-12,31,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'FOR':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,32,32,32,32,32,32,32,32,32,32,32,32,-45,32,-42,-43,32,-11,32,-44,32,-48,-51,-54,-46,-41,-28,32,-12,32,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'ACT':([8,9,10,15,20,22,23,24,25,44,45,46,47,48,51,64,65,70,74,85,96,97,101,102,103,108,109,110,117,126,128,129,130,131,133,134,135,136,137,140,144,145,146,148,],[-10,33,33,33,33,33,33,33,33,33,33,33,33,-45,33,-42,-43,33,-11,33,-44,33,-48,-51,-54,-46,-41,-28,33,-12,33,-38,-39,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'END':([8,9,14,15,20,22,23,24,25,43,44,45,46,47,48,50,51,53,54,55,56,64,65,74,77,78,79,80,82,96,101,102,103,108,109,110,126,129,131,133,134,135,136,137,140,144,145,146,148,],[-10,-27,42,-27,-27,-27,-27,-27,-27,-16,-27,-27,-27,-27,-45,-21,-27,-23,-24,-25,-26,-42,-43,-11,-17,-18,-19,-20,-22,-44,-48,-51,-54,-46,-41,-28,-12,-38,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'RETURN':([8,10,15,20,22,23,24,25,34,43,44,45,46,47,48,50,51,53,54,55,56,64,65,74,77,78,79,80,82,96,101,102,103,108,109,110,126,129,131,133,134,135,136,137,140,144,145,146,148,],[-10,-27,-27,-27,-27,-27,-27,-27,72,-16,-27,-27,-27,-27,-45,-21,-27,-23,-24,-25,-26,-42,-43,-11,-17,-18,-19,-20,-22,-44,-48,-51,-54,-46,-41,-28,-12,-38,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'LOOP':([8,15,20,22,23,24,25,43,44,45,46,47,48,50,51,53,54,55,56,64,65,70,74,77,78,79,80,82,96,101,102,103,105,108,109,110,126,129,131,133,134,135,136,137,140,144,145,146,148,],[-10,-27,-27,-27,-27,-27,-27,-16,-27,-27,-27,-27,-45,-21,-27,-23,-24,-25,-26,-42,-43,-27,-11,-17,-18,-19,-20,-22,-44,-48,-51,-54,124,-46,-41,-28,-12,-38,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'NOWHERE':([8,15,20,22,23,24,25,43,44,45,46,47,48,50,51,53,54,55,56,64,65,74,77,78,79,80,82,85,96,101,102,103,108,109,110,111,126,128,129,130,131,133,134,135,136,137,140,141,144,145,146,148,],[-10,-27,-27,-27,-27,-27,-27,-16,-27,-27,-27,-27,-45,-21,-27,-23,-24,-25,-26,-42,-43,-11,-17,-18,-19,-20,-22,-27,-44,-48,-51,-54,-46,-41,-28,129,-12,-27,-38,-39,-35,-49,-50,-52,-53,-55,-47,145,-13,-37,-29,-33,]),'OTHER':([8,15,20,22,23,24,25,43,44,45,46,47,48,50,51,53,54,55,56,64,65,74,77,78,79,80,82,85,96,101,102,103,108,109,110,111,126,129,131,133,134,135,136,137,140,144,145,146,148,],[-10,-27,-27,-27,-27,-27,-27,-16,-27,-27,-27,-27,-45,-21,-27,-23,-24,-25,-26,-42,-43,-11,-17,-18,-19,-20,-22,-27,-44,-48,-51,-54,-46,-41,-28,130,-12,-38,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'ENDWHILST':([8,15,20,22,23,24,25,43,44,45,46,47,48,50,51,53,54,55,56,64,65,74,77,78,79,80,82,96,97,101,102,103,108,109,110,116,126,129,131,133,134,135,136,137,140,144,145,146,148,],[-10,-27,-27,-27,-27,-27,-27,-16,-27,-27,-27,-27,-45,-21,-27,-23,-24,-25,-26,-42,-43,-11,-17,-18,-19,-20,-22,-44,-27,-48,-51,-54,-46,-41,-28,131,-12,-38,-35,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'INCOMING':([8,15,20,22,23,24,25,43,44,45,46,47,48,50,51,53,54,55,56,64,65,74,77,78,79,80,82,96,101,102,103,108,109,110,117,126,129,131,132,133,134,135,136,137,140,144,145,146,148,],[-10,-27,-27,-27,-27,-27,-27,-16,-27,-27,-27,-27,-45,-21,-27,-23,-24,-25,-26,-42,-43,-11,-17,-18,-19,-20,-22,-44,-48,-51,-54,-46,-41,-28,-27,-12,-38,-35,142,-49,-50,-52,-53,-55,-47,-13,-37,-29,-33,]),'AIGUAL':([8,29,52,71,74,126,144,],[-10,69,83,-32,-11,-12,-13,]),'IGUAL':([8,60,61,62,64,65,74,96,112,113,114,115,126,144,],[-10,89,-59,-61,-42,-43,-11,-44,89,89,-60,-62,-12,-13,]),'NOIGUAL':([8,60,61,62,64,65,74,96,112,113,114,115,126,144,],[-10,90,-59,-61,-42,-43,-11,-44,90,90,-60,-62,-12,-13,]),'MAYOR':([8,60,61,62,64,65,74,96,112,113,114,115,126,144,],[-10,91,-59,-61,-42,-43,-11,-44,91,91,-60,-62,-12,-13,]),'MENOR':([8,60,61,62,64,65,74,96,112,113,114,115,126,144,],[-10,92,-59,-61,-42,-43,-11,-44,92,92,-60,-62,-12,-13,]),'MAYORI':([8,60,61,62,64,65,74,96,112,113,114,115,126,144,],[-10,93,-59,-61,-42,-43,-11,-44,93,93,-60,-62,-12,-13,]),'MENORI':([8,60,61,62,64,65,74,96,112,113,114,115,126,144,],[-10,94,-59,-61,-42,-43,-11,-44,94,94,-60,-62,-12,-13,]),'OR':([8,59,60,61,62,64,65,74,95,96,112,113,114,115,126,144,147,],[-10,86,-56,-59,-61,-42,-43,-11,86,-44,-57,-58,-60,-62,-12,-13,86,]),'AND':([8,59,60,61,62,64,65,74,95,96,112,113,114,115,126,144,147,],[-10,87,-56,-59,-61,-42,-43,-11,87,-44,-57,-58,-60,-62,-12,-13,87,]),'THEN':([8,58,59,60,61,62,64,65,74,96,112,113,114,115,126,144,],[-10,85,-40,-56,-59,-61,-42,-43,-11,-44,-57,-58,-60,-62,-12,-13,]),'DOSPUNTOS':([8,30,33,57,59,60,61,62,64,65,67,74,96,98,101,102,103,108,112,113,114,115,118,126,133,134,135,136,137,144,],[-10,70,-34,84,-40,-56,-59,-61,-42,-43,97,-11,-44,117,-48,-51,-54,127,-57,-58,-60,-62,-30,-12,-49,-50,-52,-53,-55,-13,]),'PARENTESISF':([8,39,40,41,60,61,62,64,65,74,81,95,96,101,102,103,107,112,113,114,115,123,126,133,134,135,136,137,139,144,147,],[-10,-8,74,-9,-56,-59,-61,-42,-43,-11,108,115,-44,-48,-51,-54,126,-57,-58,-60,-62,137,-12,-49,-50,-52,-53,-55,144,-13,148,]),'MULT':([8,64,65,74,96,101,102,103,126,133,134,135,136,137,144,],[-10,-42,-43,-11,-44,121,-51,-54,-12,121,121,-52,-53,-55,-13,]),'DIV':([8,64,65,74,96,101,102,103,126,133,134,135,136,137,144,],[-10,-42,-43,-11,-44,122,-51,-54,-12,122,122,-52,-53,-55,-13,]),'MAS':([8,64,65,74,96,100,101,102,103,109,118,123,126,133,134,135,136,137,144,],[-10,-42,-43,-11,-44,119,-48,-51,-54,119,119,119,-12,-49,-50,-52,-53,-55,-13,]),'MENOS':([8,27,28,31,63,64,65,69,74,83,86,87,88,89,90,91,92,93,94,96,99,100,101,102,103,104,109,118,119,120,121,122,123,126,133,134,135,136,137,143,144,],[-10,66,66,-36,66,-42,-43,66,-11,66,66,66,66,-63,-64,-65,-66,-67,-68,-44,66,120,-48,-51,-54,66,120,120,66,66,66,66,120,-12,-49,-50,-52,-53,-55,66,-13,]),'TILL':([8,64,65,68,74,96,100,101,102,103,126,133,134,135,136,137,144,],[-10,-42,-43,99,-11,-44,-31,-48,-51,-54,-12,-49,-50,-52,-53,-55,-13,]),'PARENTESISI':([8,19,27,28,31,63,69,83,86,87,88,89,90,91,92,93,94,99,104,119,120,121,122,138,143,],[13,49,63,63,-36,63,104,104,63,63,63,-63,-64,-65,-66,-67,-68,104,104,104,104,104,104,143,63,]),'FLOAT':([11,],[36,]),'WORD':([11,],[37,]),'NUM':([13,27,28,31,63,66,69,75,83,86,87,88,89,90,91,92,93,94,99,104,119,120,121,122,125,143,],[41,64,64,-36,64,96,64,41,64,64,64,64,-63,-64,-65,-66,-67,-68,64,64,64,64,64,64,41,64,]),'STRING':([26,49,],[57,81,]),'UNTIL':([124,],[138,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'V':([0,35,],[2,73,]),'R':([2,42,72,],[4,76,106,]),'VAR':([3,12,],[6,38,]),'VEC':([3,12,19,21,27,28,63,69,83,86,87,88,99,104,119,120,121,122,127,143,],[7,7,48,52,65,65,65,65,65,65,65,65,65,65,65,65,65,65,140,65,]),'B':([9,10,15,20,22,23,24,25,44,45,46,47,51,70,85,97,117,128,],[14,34,43,50,53,54,55,56,77,78,79,80,82,105,111,116,132,141,]),'READ':([9,10,15,20,22,23,24,25,44,45,46,47,51,70,85,97,117,128,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'IF':([9,10,15,20,22,23,24,25,44,45,46,47,51,70,85,97,117,128,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'LOOPWHILE':([9,10,15,20,22,23,24,25,44,45,46,47,51,70,85,97,117,128,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'LOOPFOR':([9,10,15,20,22,23,24,25,44,45,46,47,51,70,85,97,117,128,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'LOOPDO':([9,10,15,20,22,23,24,25,44,45,46,47,51,70,85,97,117,128,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'WHILE':([9,10,15,20,22,23,24,25,44,45,46,47,51,70,85,97,117,128,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'FORID':([9,10,15,20,22,23,24,25,44,45,46,47,51,70,85,97,117,128,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'DO':([9,10,15,20,22,23,24,25,44,45,46,47,51,70,85,97,117,128,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'TYPE':([11,],[35,]),'VALUE':([13,75,125,],[40,107,139,]),'MENS':([19,],[47,]),'EXPR':([21,],[51,]),'LOGIC':([27,28,],[58,67,]),'EL':([27,28,63,143,],[59,59,95,147,]),'TL':([27,28,63,86,87,143,],[60,60,60,112,113,60,]),'FL':([27,28,63,86,87,88,143,],[61,61,61,61,61,114,61,]),'ASGN':([27,28,63,69,83,86,87,88,99,104,119,120,121,122,143,],[62,62,62,103,103,62,62,62,103,103,103,103,103,103,62,]),'EXP1':([29,],[68,]),'COND':([60,112,113,],[88,88,88,]),'EXP2':([68,],[98,]),'EA':([69,83,99,104,],[100,109,118,123,]),'TA':([69,83,99,104,119,120,],[101,101,101,101,133,134,]),'FA':([69,83,99,104,119,120,121,122,],[102,102,102,102,102,102,135,136,]),'ELSE':([111,],[128,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> V R BEGIN B END R','PROGRAMA',6,'p_PROGRAMA','Language.py',346),
  ('V -> PUT VAR AS TYPE V','V',5,'p_V','Language.py',351),
  ('V -> <empty>','V',0,'p_V','Language.py',352),
  ('TYPE -> FLOAT','TYPE',1,'p_TYPE','Language.py',360),
  ('TYPE -> WORD','TYPE',1,'p_TYPE','Language.py',361),
  ('VAR -> VEC','VAR',1,'p_VAR','Language.py',367),
  ('VAR -> VAR COMA VAR','VAR',3,'p_VAR','Language.py',368),
  ('VALUE -> ID','VALUE',1,'p_VALUE','Language.py',380),
  ('VALUE -> NUM','VALUE',1,'p_VALUE','Language.py',381),
  ('VEC -> ID','VEC',1,'p_VEC','Language.py',387),
  ('VEC -> ID PARENTESISI VALUE PARENTESISF','VEC',4,'p_VEC','Language.py',388),
  ('VEC -> ID PARENTESISI VALUE COMA VALUE PARENTESISF','VEC',6,'p_VEC','Language.py',389),
  ('VEC -> ID PARENTESISI VALUE COMA VALUE COMA VALUE PARENTESISF','VEC',8,'p_VEC','Language.py',390),
  ('R -> SUBMETHOD ID B RETURN R','R',5,'p_R','Language.py',397),
  ('R -> <empty>','R',0,'p_R','Language.py',398),
  ('B -> CLEAR B','B',2,'p_B','Language.py',403),
  ('B -> ET ID B','B',3,'p_B','Language.py',404),
  ('B -> JUMP ID B','B',3,'p_B','Language.py',405),
  ('B -> TRAVEL ID B','B',3,'p_B','Language.py',406),
  ('B -> PRINT MENS B','B',3,'p_B','Language.py',407),
  ('B -> READ B','B',2,'p_B','Language.py',408),
  ('B -> GIVE EXPR B','B',3,'p_B','Language.py',409),
  ('B -> IF B','B',2,'p_B','Language.py',410),
  ('B -> LOOPWHILE B','B',2,'p_B','Language.py',411),
  ('B -> LOOPFOR B','B',2,'p_B','Language.py',412),
  ('B -> LOOPDO B','B',2,'p_B','Language.py',413),
  ('B -> <empty>','B',0,'p_B','Language.py',414),
  ('READ -> TAKE STRING DOSPUNTOS ID','READ',4,'p_READ','Language.py',419),
  ('LOOPFOR -> FORID EXP1 EXP2 DOSPUNTOS B INCOMING ID','LOOPFOR',7,'p_LOOPFOR','Language.py',429),
  ('EXP2 -> TILL EA','EXP2',2,'p_EXP2','Language.py',441),
  ('EXP1 -> AIGUAL EA','EXP1',2,'p_EXP1','Language.py',457),
  ('FORID -> FOR ID','FORID',2,'p_FORID','Language.py',466),
  ('LOOPDO -> DO DOSPUNTOS B LOOP UNTIL PARENTESISI EL PARENTESISF','LOOPDO',8,'p_LOOPDO','Language.py',473),
  ('DO -> ACT','DO',1,'p_DO','Language.py',482),
  ('LOOPWHILE -> WHILE LOGIC DOSPUNTOS B ENDWHILST','LOOPWHILE',5,'p_LOOPWHILE','Language.py',489),
  ('WHILE -> WHILST','WHILE',1,'p_WHILE','Language.py',499),
  ('IF -> WHEREVER LOGIC THEN B ELSE B NOWHERE','IF',7,'p_IF','Language.py',506),
  ('IF -> WHEREVER LOGIC THEN B NOWHERE','IF',5,'p_IF','Language.py',507),
  ('ELSE -> OTHER','ELSE',1,'p_ELSE','Language.py',515),
  ('LOGIC -> EL','LOGIC',1,'p_LOGIC','Language.py',525),
  ('EXPR -> VEC AIGUAL EA','EXPR',3,'p_EXPR','Language.py',534),
  ('ASGN -> NUM','ASGN',1,'p_ASGN','Language.py',542),
  ('ASGN -> VEC','ASGN',1,'p_ASGN','Language.py',543),
  ('ASGN -> MENOS NUM','ASGN',2,'p_ASGN','Language.py',544),
  ('MENS -> VEC','MENS',1,'p_MENS','Language.py',553),
  ('MENS -> PARENTESISI STRING PARENTESISF','MENS',3,'p_MENS','Language.py',554),
  ('MENS -> PARENTESISI STRING PARENTESISF DOSPUNTOS VEC','MENS',5,'p_MENS','Language.py',555),
  ('EA -> TA','EA',1,'p_EA','Language.py',570),
  ('EA -> EA MAS TA','EA',3,'p_EA','Language.py',571),
  ('EA -> EA MENOS TA','EA',3,'p_EA','Language.py',572),
  ('TA -> FA','TA',1,'p_TA','Language.py',589),
  ('TA -> TA MULT FA','TA',3,'p_TA','Language.py',590),
  ('TA -> TA DIV FA','TA',3,'p_TA','Language.py',591),
  ('FA -> ASGN','FA',1,'p_FA','Language.py',608),
  ('FA -> PARENTESISI EA PARENTESISF','FA',3,'p_FA','Language.py',609),
  ('EL -> TL','EL',1,'p_EL','Language.py',617),
  ('EL -> EL OR TL','EL',3,'p_EL','Language.py',618),
  ('EL -> EL AND TL','EL',3,'p_EL','Language.py',619),
  ('TL -> FL','TL',1,'p_TL','Language.py',636),
  ('TL -> TL COND FL','TL',3,'p_TL','Language.py',637),
  ('FL -> ASGN','FL',1,'p_FL','Language.py',654),
  ('FL -> PARENTESISI EL PARENTESISF','FL',3,'p_FL','Language.py',655),
  ('COND -> IGUAL','COND',1,'p_COND','Language.py',663),
  ('COND -> NOIGUAL','COND',1,'p_COND','Language.py',664),
  ('COND -> MAYOR','COND',1,'p_COND','Language.py',665),
  ('COND -> MENOR','COND',1,'p_COND','Language.py',666),
  ('COND -> MAYORI','COND',1,'p_COND','Language.py',667),
  ('COND -> MENORI','COND',1,'p_COND','Language.py',668),
]