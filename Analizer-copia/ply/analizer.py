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
    'AIGUAL', #ASIGNEMENT IGUAL
    'IGUAL', #COMPARASION IGUAL
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
    'begin' : 'BEGIN',
    'end' : 'END',
    'put' : 'PUT',
    'as' : 'AS',
    'word' : 'WORD',
    'float' : 'FLOAT',
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