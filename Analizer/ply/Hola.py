# Jorge Carlos Medina Rodriguez     A00571342
import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    'ID',
    'NUM',
    'MAS',
    'MENOS',
    'MULT',
    'DIV',
    'COMA',
    'DOSPUNTOS',
    'IGUAL',
    'AIGUAL',
    'NOIGUAL',
    'MAYOR',
    'MENOR',
    'MAYORI',
    'MENORI',
    'COMILLA',
    'PARENTESISI',
    'PARENTESISF',
    'AND',
    'OR',
    'NOT'
]

reserved = {
    'put' : 'PUT',
    'as' : 'AS',
    'word' : 'WORD',
    'float' : 'FLOAT',
    'begin' : 'BEGIN',
    'end' : 'END',
    'et' : 'ET',
    'clear' : 'CLEAR',
    'print' : 'PRINT',
    'take' : 'TAKE', #Input
    'act' : 'ACT',
    'loop' : 'LOOP',
    'whilst' : 'WHILST',
    'until' : 'UNTIL',
    'travel' : 'TRAVEL',
    'wherever' : 'WHEREVER', #if
    'then' : 'THEN',
    'other' : 'OTHER', #else
    'nowhere' : 'NOWHERE',
    'jump' : 'JUMP',
    'for' : 'FOR',
    'till' : 'TILL',
    'incoming' : 'INCOMING',
    'give' : 'GIVE',
    'submethod' : 'SUBMETHOD',
    'return' : 'RETURN',
    'endwhilst' : 'ENDWHILST'
}

tokens = tokens + list(reserved.values())

t_ignore = '\t\r '

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_MAS(t):
    r'\+'
    t.type = 'MAS'
    return t

def t_MENOS(t):
    r'\-'
    t.type = 'MENOS'
    return t

def t_MULT(t):
    r'\*'
    t.type = 'MULT'
    return t

def t_DIV(t):
    r'/'
    t.type = 'DIV'
    return t

def t_COMA(t):
    r','
    t.type = 'COMA'
    return t
    
def t_DOSPUNTOS(t):
    r':'
    t.type = 'DOSPUNTOS'
    return t

def t_AIGUAL(t):
    r'='
    t.type = 'AIGUAL'
    return t
    
def t_IGUAL(t):
    r'=='
    t.type = 'IGUAL'
    return t

def t_NOIGUAL(t):
    r'<>'
    t.type = 'NOIGUAL'
    return t
    
def t_MAYOR(t):
    r'>'
    t.type = 'MAYOR'
    return t
    
def t_MENOR(t):
    r'<'
    t.type = 'MENOR'
    return t
    
def t_MAYORI(t):
    r'>='
    t.type = 'MAYORI'
    return t
    
def t_MENORI(t):
    r'<='
    t.type = 'MENORI'
    return t
    
def t_COMILLA(t):
    r'\"'
    t.type = 'COMILLA'
    return t

def t_PARENTESISI(t):
    r'\('
    t.type = 'PARENTESISI'
    return t

def t_PARENTESISF(t):
    r'\)'
    t.type = 'PARENTESISF'
    return t
    
def t_AND(t):
    r'AND'
    t.type = 'AND'
    return t
    
def t_OR(t):
    r'OR'
    t.type = 'OR'
    return t
    
def t_NOT(t):
    r'NOT'
    t.type = 'NOT'
    return t

def t_COMMENT(t):
    r'\#.'
    pass

def t_BEGIN(t):
    r'BEGIN'
    t.type = 'BEGIN'
    return t

def t_END(t):
    r'END'
    t.type = 'END'
    return t

def t_PUT(t):
    r'PUT'
    t.type = 'PUT'
    return t

def t_AS(t):
    r'AS'
    t.type = 'AS'
    return t

def t_WORD(t):
    r'WORD'
    t.type = 'WORD'
    return t

def t_FLOAT(t):
    r'FLOAT'
    t.type = 'FLOAT'
    return t

def t_ET(t):
    r'ET'
    t.type = 'ET'
    return t

def t_CLEAR(t):
    r'CLEAR'
    t.type = 'CLEAR'
    return t

def t_PRINT(t):
    r'PRINT'
    t.type = 'PRINT'
    return t

def t_TAKE(t):
    r'TAKE'
    t.type = 'TAKE'
    return t

def t_ACT(t):
    r'ACT'
    t.type = 'ACT'
    return t

def t_LOOP(t):
    r'LOOP'
    t.type = 'LOOP'
    return t

def t_WHILST(t):
    r'LOOP'
    t.type = 'WHILST'
    return t

def t_UNTIL(t):
    r'UNTIL'
    t.type = 'UNTIL'
    return t

def t_TRAVEL(t):
    r'TRAVEL'
    t.type = 'TRAVEL'
    return t

def t_WHEREVER(t):
    r'WHEREVER'
    t.type = 'WHEREVER'
    return t

def t_THEN(t):
    r'THEN'
    t.type = 'THEN'
    return t

def t_OTHER(t):
    r'OTHER'
    t.type = 'OTHER'
    return t

def t_NOWHERE(t):
    r'NOWHERE'
    t.type = 'NOWHERE'
    return t

def t_JUMP(t):
    r'JUMP'
    t.type = 'JUMP'
    return t

def t_FOR(t):
    r'FOR'
    t.type = 'FOR'
    return t

def t_TILL(t):
    r'TILL'
    t.type = 'TILL'
    return t

def t_INCOMING(t):
    r'INCOMING'
    t.type = 'INCOMING'
    return t

def t_GIVE(t):
    r'GIVE'
    t.type = 'GIVE'
    return t

def t_SUBMETHOD(t):
    r'SUBMETHOD'
    t.type = 'SUBMETHOD'
    return t

def t_RETURN(t):
    r'RETURN'
    t.type = 'RETURN'
    return t

def t_ENDWHILST(t):
    r'ENDWHILST'
    t.type = 'ENDWHILST'
    return t

def t_error(t):
    print ("Error token '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

def p_PROGRAMA(p): 
    '''
    PROGRAMA : V R BEGIN B END R
    '''

def p_V(p):
    '''
    V : PUT VAR AS TYPE V
    |
    '''

def p_TYPE(p):
    '''
    TYPE : FLOAT
    | WORD
    '''

def p_VAR(p):
    '''
    VAR : 
    | VEC
    | VAR COMA VAR
    '''

def p_VEC(p):
    '''
    VEC : 
    | ID
    | ID PARENTESISI NUM PARENTESISF
    | ID PARENTESISI NUM COMA NUM PARENTESISF
    | ID PARENTESISI NUM COMA NUM COMA NUM PARENTESISF
    '''

def p_R(p):
    '''
    R : SUBMETHOD ID B RETURN R
    |
    '''

def p_B(p):
    '''
    B : CLEAR B
    | ET ID B
    | JUMP ID B
    | TRAVEL ID B
    | PRINT MENS B
    | TAKE COMILLA TXT COMILLA DOSPUNTOS ID B
    | GIVE ID AIGUAL EA B
    | WHEREVER EL THEN B OTHER B NOWHERE B
    | WHEREVER EL THEN B NOWHERE B
    | WHILST PARENTESISI EL PARENTESISF B ENDWHILST B
    | FOR ID AIGUAL EA TILL EA B INCOMING ID B
    | ACT B LOOP WHILST PARENTESISI EL PARENTESISF B
    | ACT B LOOP UNTIL PARENTESISI EL PARENTESISF B
    |
    '''

def p_ASGN(p):
    '''
    ASGN : NUM
    | VEC
    '''


def p_MENS(p):
    '''
    MENS : VAR
    | PARENTESISI COMILLA TXT COMILLA PARENTESISF
    | PARENTESISI COMILLA TXT COMILLA PARENTESISF DOSPUNTOS VAR
    '''

def p_TXT(p):
    '''
    TXT : ID TXT
    | 
    '''

def p_EA(p):
    '''
    EA : TA
    | EA MAS TA
    | EA MENOS TA
    '''

def p_TA(p):
    '''
    TA : FA
    | TA MULT FA
    | TA DIV FA
    '''

def p_FA(p):
    '''
    FA : ASGN
    | PARENTESISI EA PARENTESISF
    '''

def p_EL(p):
    '''
    EL : TL
    | EL OR TL
    '''

def p_TL(p):
    '''
    TL : FL
    | TL AND FL
    '''

def p_FL(p):
    '''
    FL : ASGN COND ASGN
    | PARENTESISI EL PARENTESISF
    '''

def p_COND(p):
    '''
    COND : IGUAL
    | NOIGUAL
    | MAYOR
    | MENOR
    | MAYORI
    | MENORI
    '''

def p_error(p):
    print("#PARSING ERROR#")

parser = yacc.yacc(start='PROGRAMA')
print("CODE VERIFICATION")

f = open("test.txt", "r")
yacc.parse(f.read())
print("VERIFICACION TERMINADA")