
class data:
    def __init__(self, name, types, value):
        self.name = name
        self.types = types
        self.value = value


def verifyVariable(variable):
    try:
        variable = int(variable)
        return variable
    except ValueError:
        print("error")
        pass


for pc in range(len(cuadruplos)):
    print ("Program counter: ", pc)
    if (cuadruplos[pc][1] != '-'):
        a = verifyVariable(cuadruplos[pc][1])
        #print("a= ", a.value)
    if (cuadruplos[pc][2] != '-'):
        b = verifyVariable(cuadruplos[pc][2])
        #print("b= ", b.value)
    c = verifyVariable(cuadruplos[pc][3])
    #print("c= ", c.value)
    if (cuadruplos[pc][0] == '+'):
        c.value = a.value + b.value
    elif (cuadruplos[pc][0] == '-'):
        c.value = a.value - b.value
    elif (cuadruplos[pc][0] == '*'):
        c.value = a.value * b.value
    elif (cuadruplos[pc][0] == '/'):
        c.value = a.value / b.value
    elif (cuadruplos[pc][0] == '='):
        if c.type == 'FLOAT':
            c.value = float(a.value)
        elif c.type == 'WORD':
            c.value = int(a.value)
    elif (cuadruplos[pc][0] == '=='):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value == b.value
    elif (cuadruplos[pc][0] == '>='):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value >= b.value
    elif (cuadruplos[pc][0] == '<='):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value <= b.value
    elif (cuadruplos[pc][0] == '>'):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value > b.value
    elif (cuadruplos[pc][0] == '<'):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value < b.value
    elif (cuadruplos[pc][0] == '!='):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value != b.value
    elif (cuadruplos[pc][0] == 'gotoF'):
        if(a.value == False):
            pc = c.value
    elif (cuadruplos[pc][0] == 'goto'):
        pc = c.value





    def t_NOT(t):
        r'NOT'
        t.type = 'NOT'
        return t

    
def p_TXT(p):
    '''
    TXT : ID TXT
    | 
    '''