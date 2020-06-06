# Jorge Carlos Medina Rodriguez     A00571342
import ply.lex as lex
import ply.yacc as yacc
import sys

class data:
    def __init__(self, name, types, value):
        self.name = name
        self.type = types
        self.value = value

class var_obt:
    def __init__(self, name, types, dim, dim1, dim2, dim3):
        self.name = name
        self.type = types
        self.dim = dim
        self.dim1 = dim1
        self.dim2 = dim2
        self.dim3 = dim3
    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return hash(('name', self.name))   
    def __str__(self):
        return (str(self.name) + " " + str(self.type))

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
    'PARENTESISI',
    'PARENTESISF',
    'CORCHETESI',
    'CORCHETESF',
    'AND',
    'OR'
]

reserved = {
    'put' : 'PUT',
    'as' : 'AS',
    'word' : 'WORD',
    'float' : 'FLOAT',
    'begin' : 'BEGIN',
    'end' : 'END',
    'et' : 'ET',
    'give' : 'GIVE',
    'clear' : 'CLEAR',
    'print' : 'PRINT',
    'take' : 'TAKE', #Input
    'act' : 'ACT',
    'loop' : 'LOOP',
    'whilst' : 'WHILST',
    'until' : 'UNTIL',
    'travel' : 'TRAVEL',
    'wherever' : 'WHEREVER', #if
    'for' : 'FOR',
    'then' : 'THEN',
    'other' : 'OTHER', #else
    'nowhere' : 'NOWHERE',
    'string' : 'STRING',
    'jump' : 'JUMP',
    'till' : 'TILL',
    'incoming' : 'INCOMING',
    'submethod' : 'SUBMETHOD',
    'return' : 'RETURN',
    'endwhilst' : 'ENDWHILST',
    'temporal' : 'TEMPORAL'
}

tokens = tokens + list(reserved.values())

t_ignore = '\t\r '

def t_BEGIN(t):
    r'BEGIN'
    t.type = 'BEGIN'
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

def t_GIVE(t):
    r'GIVE'
    t.type = 'GIVE'
    return t

def t_ACT(t):
    r'ACT'
    t.type = 'ACT'
    return t

def t_LOOP(t):
    r'LOOP'
    t.type = 'LOOP'
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

def t_SUBMETHOD(t):
    r'SUBMETHOD'
    t.type = 'SUBMETHOD'
    return t

def t_RETURN(t):
    r'RETURN'
    t.type = 'RETURN'
    return t

def t_WHILST(t):
    r'WHILST'
    t.type = 'WHILST'
    return t
    
def t_ENDWHILST(t):
    r'ENDWHILST'
    t.type = 'ENDWHILST'
    return t

def t_END(t):
    r'END'
    t.type = 'END'
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

def t_PARENTESISI(t):
    r'\('
    t.type = 'PARENTESISI'
    return t

def t_PARENTESISF(t):
    r'\)'
    t.type = 'PARENTESISF'
    return t

def t_CORCHETESI(t):
    r'\['
    t.type = 'CORCHETESI'
    return t

def t_CORCHETESF(t):
    r'\]'
    t.type = 'CORCHETESF'
    return t

def t_COMA(t):
    r','
    t.type = 'COMA'
    return t
    
def t_DOSPUNTOS(t):
    r':'
    t.type = 'DOSPUNTOS'
    return t

def t_IGUAL(t):
    r'=='
    t.type = 'IGUAL'
    return t

def t_AIGUAL(t):
    r'='
    t.type = 'AIGUAL'
    return t

def t_NOIGUAL(t):
    r'!='
    t.type = 'NOIGUAL'
    return t

def t_MAYORI(t):
    r'>='
    t.type = 'MAYORI'
    return t
    
def t_MENORI(t):
    r'<='
    t.type = 'MENORI'
    return t
    
def t_MAYOR(t):
    r'>'
    t.type = 'MAYOR'
    return t
    
def t_MENOR(t):
    r'<'
    t.type = 'MENOR'
    return t
    
def t_AND(t):
    r'AND'
    t.type = 'AND'
    return t
    
def t_OR(t):
    r'OR'
    t.type = 'OR'
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_STRING(t):
    r'["][a-zA-Z 0-9:!@#$%^&*()-+=/?<>,]+["]'
    t.type = reserved.get(t.value,'STRING')
    return t

def t_TEMPORAL(t):
    r'temporal*'
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print ("Error token '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

tablaSimbolos = []
variableSpace = []
temporalSpace = []
dirProcedimientos = []
dirEtiquetas = []

variables = []
tipos = []
avail = ["temporal1", "temporal2", "temporal3", "temporal4", "temporal5", "temporal6", "temporal7" ,"temporal8"]
temporales = ["temporal1", "temporal2", "temporal3", "temporal4", "temporal5", "temporal6", "temporal7" ,"temporal8"]
cuadruplos = []
operandos = []
saltos = []
ID = ''
tf = ''

temp_num = 9

def checkTemporals(): 
    global temp_num, avail, temporales
    if len(temporales) == 0:
        value = "temporal"+str(temp_num)
        avail.append(value)
        temporales.append(value)
        temp_num += 1

def p_PROGRAMA(p): 
    '''
    PROGRAMA : V BEGIN B END R
    '''
    global dirProcedimientos, cuadruplos
    cuadruplos.append(['ENDMAIN','-','-','-'])

def p_V(p):
    '''
    V : PUT VAR AS TYPE V
    |
    '''
    if len(p) >= 2:
        for x in range(p[2]): 
            tipos.append(p[4])
        
def p_TYPE(p):
    '''
    TYPE : FLOAT
    | WORD
    '''
    p[0] = p[1]

def p_VAR(p):
    '''
    VAR : VEC
    | VAR COMA VAR
    '''
    global i
    if len(p) == 2 :
        i = 0
        variables.append(p[1])
    if len(p) == 4 :
        i += 1
    p[0] = 1 + i

#Puede ser numero o variable
def p_VALUE(p):
    '''
    VALUE : ID
    | NUM
    '''
    p[0] = p[1]

#Gramatica para la declaracion de variables
def p_VEC(p):
    '''
    VEC : ID
    | ID PARENTESISI VALUE PARENTESISF
    | ID PARENTESISI VALUE COMA VALUE PARENTESISF
    | ID PARENTESISI VALUE COMA VALUE COMA VALUE PARENTESISF
    '''
    if len(p) == 2 :
        p[0] = var_obt(p[1],"VAR",0,0,0,0) 
    elif len(p) == 5 :
        p[0] = var_obt(p[1],"ARRAY",1,p[3],0,0) 
    elif len(p) == 7 :
        p[0] = var_obt(p[1],"ARRAY",2,p[3],p[5],0) 
    elif len(p) == 9 :
        p[0] = var_obt(p[1],"ARRAY",3,p[3],p[5],p[7]) 


#Gramatica de los metodos
def p_R(p):
    '''
    R : PROCEDURE B RETURN R
    |
    '''
    global dirProcedimientos, cuadruplos
    if(len(p)>1):
        cuadruplos.append(['ENDPROCEDURE','-','-','-'])

def p_PROCEDURE(p):
    '''
    PROCEDURE : SUBMETHOD ID
    '''
    global dirProcedimientos, cuadruplos
    rep= False
    for i in range(len(dirProcedimientos)):
        if (dirProcedimientos[i][0] == str(p[2])):
            rep = True
            break
    if rep == False :
        dirProcedimientos.append([p[2],len(cuadruplos)])
    else:
        raise Exception('El Id de una sub-metodo es un duplicado')

#Body de la gramatica
def p_B(p):
    '''
    B : CLEAR B
    | ETIQUETAS B
    | SALTO B
    | CALL B
    | PRINT MENS B
    | READ B
    | GIVE EXPR B
    | IF B
    | LOOPWHILE B
    | LOOPFOR B
    | LOOPDO B
    |
    '''

#Gramatica para llamr a sub-procedimientos
def p_CALL(p):
    '''
    CALL : TRAVEL ID
    '''
    global dirProcedimientos, cuadruplos
    cuadruplos.append(['CALL','-','-',str(p[2])])

#Gramatica para generar etiquetas
def p_ETIQUETAS(p):
    '''
    ETIQUETAS : ET ID
    '''
    global dirEtiquetas, cuadruplos
    rep= False
    for i in range(len(dirEtiquetas)):
        if (dirEtiquetas[i][0] == str(p[2])):
            rep = True
            break
    if rep == False :
        dirEtiquetas.append([p[2],len(cuadruplos)])
    else:
        raise Exception('El Id de una etiqueta es duplicado')

#Gramatica para generar saltos
def p_SALTO(p):
    '''
    SALTO : JUMP ID
    '''
    global dirEtiquetas, cuadruplos
    found = False
    for i in range(len(dirEtiquetas)):
        if (dirEtiquetas[i][0] == str(p[2])):
            found = True
            break
    if found == True:
        cuadruplos.append(['JUMP','-',dirEtiquetas[i][0],dirEtiquetas[i][1]])
    else:
        cuadruplos.append(['JUMP','-',dirEtiquetas[i][0],-1])

#Gramatica para el read
def p_READ(p):
    '''
    READ : TAKE STRING DOSPUNTOS ASGN
    '''
    global cuadruplos
    read_var = data(str(p[2]),"ALL",p[4])
    cuadruplos.append(['TAKE','-','-',read_var])

# Gramatica del for loop
def p_LOOPFOR(p):
    '''
    LOOPFOR : FORID EXP1 EXP2 DOSPUNTOS B INCOMING ID
    '''
    global operandos, cuadruplos, temporales, avail, saltos, ID, tf
    ID = operandos.pop()
    cuadruplos.append(['+',ID,1,ID])
    retorno = saltos.pop()
    cuadruplos.append(['goto','-','-',retorno])
    cuadruplos[retorno+1].append(len(cuadruplos))
    temporales.append(tf)

def p_EXP2(p):
    '''
    EXP2 : TILL EA
    '''
    global operandos, cuadruplos, temporales, avail, saltos, ID, tf
    checkTemporals()
    tf = temporales.pop(0)
    e2 = operandos.pop()
    checkTemporals()
    tx = temporales.pop(0)
    cuadruplos.append(['=',e2,'-',tf])
    cuadruplos.append(['<=',ID,tf,tx])
    cuadruplos.append(['gotoF',tx,'-'])
    saltos.append(len(cuadruplos)-2)
    temporales.append(tx)

def p_EXP1(p):
    '''
    EXP1 : AIGUAL EA
    '''
    global operandos, cuadruplos, temporales, avail, saltos,ID
    e1 = operandos.pop()
    ID = operandos[len(operandos)-1]
    cuadruplos.append(['=',e1,'-',ID])

def p_FORID(p):
    '''
    FORID : FOR ID 
    '''
    global operandos, cuadruplos, temporales, avail, saltos
    operandos.append(p[2])

#Gramatica del loop do while
def p_LOOPDO(p):
    '''
    LOOPDO : DO DOSPUNTOS B LOOP UNTIL PARENTESISI EL PARENTESISF 
    '''
    global operandos, cuadruplos, temporales, avail, saltos
    result = operandos.pop()
    F = saltos.pop()
    cuadruplos.append(['gotoF', result , '-', F ])

def p_DO(p):
    '''
    DO : ACT  
    '''
    global operandos, cuadruplos, temporales, avail, saltos
    saltos.append(len(cuadruplos))

#Gramatica del while
def p_LOOPWHILE(p):
    '''
    LOOPWHILE : WHILE LOGIC DOSPUNTOS B ENDWHILST 
    '''
    global operandos, cuadruplos, temporales, avail, saltos
    F = saltos.pop()
    retorno = saltos.pop()
    cuadruplos.append(['goto', '-' , '-' , retorno])
    cuadruplos[F].append(len(cuadruplos))

def p_WHILE(p):
    '''
    WHILE : WHILST
    '''
    global operandos, cuadruplos, temporales, avail, saltos
    saltos.append(len(cuadruplos))

#Gramatica del if
def p_IF(p):
    '''
    IF : WHEREVER LOGIC THEN B ELSE B NOWHERE 
    | WHEREVER LOGIC THEN B NOWHERE 
    '''
    global operandos, cuadruplos, temporales, avail, saltos
    F = saltos.pop()
    cuadruplos[F].append(len(cuadruplos))

def p_ELSE(p):
    '''
    ELSE : OTHER
    '''
    global operandos, cuadruplos, temporales, avail, saltos
    D = saltos.pop()
    cuadruplos.append(['goto', '-' , '-' ])
    saltos.append(len(cuadruplos)-1)
    cuadruplos[D].append(len(cuadruplos))

def p_LOGIC(p):
    '''
    LOGIC : EL
    '''
    global operandos, cuadruplos, temporales, avail, saltos
    result = operandos.pop()
    cuadruplos.append(['gotoF', result , '-' ])
    saltos.append(len(cuadruplos)-1)

def p_EXPR(p):
    '''
    EXPR : VEC AIGUAL EA
    '''
    global operandos, cuadruplos, temporales, avail
    cuadruplos.append([p[2], operandos.pop() , '-' , p[1]])
    temporales = avail[:]

def p_ASGN(p):
    '''
    ASGN : NUM
    | VEC
    | MENOS NUM
    '''
    if len(p) == 2 :
        p[0] = p[1]
    if len(p) == 3 :
        p[0] = p[2] * -1

#MENS significa mensaje. Es para el PRINT
def p_MENS(p):
    '''
    MENS : VEC
    | PARENTESISI STRING PARENTESISF
    | PARENTESISI STRING PARENTESISF DOSPUNTOS VEC
    '''
    global cuadruplos
    if (len(p) == 2):
        to_print = p[1]
        print_value = data('None','ALL',to_print)
    if (len(p) == 4):
        to_print = str(p[2])
        print_value = data(to_print,'ALL',0) 
    if (len(p) == 6):
        print_value = data(str(p[2]),'ALL',str(p[5])) 
    cuadruplos.append(['PRINT', '-', '-', print_value])

#Operaciones aritmeticas
def p_EA(p):
    '''
    EA : TA
    | EA MAS TA
    | EA MENOS TA
    '''
    global operandos, cuadruplos, temporales, avail
    if len(p) == 4:
        b = operandos.pop()
        a = operandos.pop()
        checkTemporals()
        c = temporales.pop(0)
        if b in avail :
            temporales.append(b)
        if a in avail :
            temporales.append(a)
        cuadruplos.append([p[2], a , b , c])
        operandos.append(c)

def p_TA(p):
    '''
    TA : FA
    | TA MULT FA
    | TA DIV FA
    '''
    global operandos, cuadruplos
    if len(p) == 4:
        b = operandos.pop()
        a = operandos.pop()
        checkTemporals()
        c = temporales.pop(0)
        if b in avail :
            temporales.append(b)
        if a in avail :
            temporales.append(a)
        cuadruplos.append([p[2], a , b , c])
        operandos.append(c)

def p_FA(p):
    '''
    FA : ASGN
    | PARENTESISI EA PARENTESISF
    '''
    global operandos, cuadruplos
    if len(p) == 2 :
        operandos.append(p[1])

#Operaciones logicas
def p_EL(p):
    '''
    EL : TL
    | EL OR TL
    | EL AND TL
    '''
    global operandos, cuadruplos
    if len(p) == 4:
        b = operandos.pop()
        a = operandos.pop()
        checkTemporals()
        c = temporales.pop(0)
        if b in avail :
            temporales.append(b)
        if a in avail :
            temporales.append(a)
        cuadruplos.append([p[2], a , b , c])
        operandos.append(c)

def p_TL(p):
    '''
    TL : FL
    | TL COND FL
    '''
    global operandos, cuadruplos
    if len(p) == 4:
        b = operandos.pop()
        a = operandos.pop()
        checkTemporals()
        c = temporales.pop(0)
        if b in avail :
            temporales.append(b)
        if a in avail :
            temporales.append(a)
        cuadruplos.append([p[2], a , b , c])
        operandos.append(c)

def p_FL(p):
    '''
    FL : ASGN
    | PARENTESISI EL PARENTESISF
    '''
    global operandos, cuadruplos
    if len(p) == 2 :
        operandos.append(p[1])

def p_COND(p):
    '''
    COND : IGUAL
    | NOIGUAL
    | MAYOR
    | MENOR
    | MAYORI
    | MENORI
    '''
    p[0] = p[1]

def p_error(p):
    print("#PARSING ERROR#")
    print(p)

#Metodos para crear las variables y el espacio de almacenamiento
def createSymbolTable(): 
    global variables
    global tablaSimbolos
    global tipos
    tipos.reverse()
    seen_titles = set()
    var_array = []
    types_array = []
    for i in range(len(variables)):
        if variables[i].name not in seen_titles:
            var_array.append(variables[i])
            types_array.append(tipos[i])
            seen_titles.add(variables[i].name)
    tablaSimbolos = [var_array,types_array]

def createVariableSpace():
    global tablaSimbolos
    global variableSpace
    global avail
    global temporalSpace
    for i in range(len(tablaSimbolos[0])):
        name = tablaSimbolos[0][i].name
        dim = tablaSimbolos[0][i].dim
        dim1 = tablaSimbolos[0][i].dim1
        dim2 = tablaSimbolos[0][i].dim2
        dim3 = tablaSimbolos[0][i].dim3
        if tablaSimbolos[1][i] == 'WORD':
            types = 'WORD'
            valor = 0
        else:
            types = 'FLOAT'
            valor = 0.0
        if(tablaSimbolos[0][i].type == 'VAR'):
            variableSpace.append(data(name,types,valor))
        if(tablaSimbolos[0][i].type == 'ARRAY'):
            if(dim1 <= 0 and dim == 1):
                raise ValueError('An array with 0 size was being created')
            if((dim1 <= 0 or dim2 <= 0) and dim == 2):
                raise ValueError('An array with 0 size was being created')
            if((dim1 <= 0 or dim2 <= 0 or dim3 <= 0) and dim == 3):
                raise ValueError('An array with 0 size was attempted to being created')
            variableSpace.append(data( name , 'ARRAY' , [dim1,dim2,dim3] ))
            size = dim1
            if(dim2 != 0):
                size *= dim2
            if(dim3 != 0):
                size *= dim3
            for j in range(size):
                variableSpace.append(data(name,types,valor))
    for i in range(len(avail)):
        name = avail[i]
        temporalSpace.append(data(name,'ALL',0))




def searchLocation(variable):
    global variableSpace
    global temporalSpace
    for i in range(len(variableSpace)):
        if variable == variableSpace[i].name:
            return variableSpace[i]
    for i in range(len(temporalSpace)):
        if variable == temporalSpace[i].name:
            return temporalSpace[i]
    return 0

def verifyVariable(variable):
    try:
        aux = variable
        variable = int(variable)
        variable = data('PUREDATA','ALL',variable)
        return variable
    except ValueError:
        try:
            variable = searchLocation(variable)
            if variable == 0:
                raise  ValueError('Error variable not found')
            else:
                return variable
        except Exception as error :
            print ( "ERROR: Variable", aux, "no existe.")
            sys.exit(0)

def checkBooleanOperation (a ,b):
    if (a.type == 'WORD' and b.type == 'FOAT'):
        print ("ERROR: Variables ", a.name, "and", b.name, "are of different type in bool operation.")
        sys.exit(0)
    if (a.type == 'FLOAT' and b.type == 'WORD'):
        print ("ERROR: Variables ", a.name, "and", b.name, "are of different type in bool operation.")
        sys.exit(0)

parser = yacc.yacc(start='PROGRAMA')

print("Program start")
f = open('Test.txt', "r")

yacc.parse(f.read())

createSymbolTable()

createVariableSpace()


print("Espacio de variables")
for i in range(len(variableSpace)):
    print (variableSpace[i].name, variableSpace[i].type, variableSpace[i].value)


#print("Espacio de temporales")
#for i in range(len(temporalSpace)):
#    print (temporalSpace[i].name, temporalSpace[i].type, temporalSpace[i].value)

#print("Cuadruplos")
#for i in range(len(cuadruplos)):
#    print(cuadruplos[i])


#print("Espacio de variables")
#for i in range(len(variableSpace)):
#    print (variableSpace[i].name, variableSpace[i].type, variableSpace[i].value)

#print("Tabla de simbolos")
#for i in range(len(tablaSimbolos)):
#    print(tablaSimbolos[i])

f.close()
print("Program finish")