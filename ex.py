
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

pc = 0
while (pc < len(cuadruplos)):
    #print ("Program counter: ", pc)
    if (cuadruplos[pc][0] == 'PRINT'):
        print_var = verifyVariable(cuadruplos[pc][3].value)
        if(cuadruplos[pc][3].name == 'None'):
            print(print_var.value)
        elif(cuadruplos[pc][3].value == 0):
            print(cuadruplos[pc][3].name)
        else:
            print(cuadruplos[pc][3].name , print_var.value)
        pc += 1
        continue
    if (cuadruplos[pc][0] == 'TAKE'):
        input_var = verifyVariable(cuadruplos[pc][3].value)
        input_var.value = input(cuadruplos[pc][3].name + " ")
        pc += 1
        continue
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
        pc += 1
    elif (cuadruplos[pc][0] == '-'):
        c.value = a.value - b.value
        pc += 1
    elif (cuadruplos[pc][0] == '*'):
        c.value = a.value * b.value
        pc += 1
    elif (cuadruplos[pc][0] == '/'):
        c.value = a.value / b.value
        pc += 1
    elif (cuadruplos[pc][0] == '='):
        if c.type == 'FLOAT':
            c.value = round(float(a.value),4)
        elif c.type == 'WORD':
            c.value = int(a.value)
        else:
            c.value = a.value
        pc += 1
    elif (cuadruplos[pc][0] == '=='):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value == b.value
        pc += 1
    elif (cuadruplos[pc][0] == '>='):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value >= b.value
        pc += 1
    elif (cuadruplos[pc][0] == '<='):
        checkBooleanOperation (a,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value <= b.value
        pc += 1
    elif (cuadruplos[pc][0] == '>'):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value > b.value
        pc += 1
    elif (cuadruplos[pc][0] == '<'):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value < b.value
        pc += 1
    elif (cuadruplos[pc][0] == '!='):
        checkBooleanOperation (a ,b)
        if (a.type == 'WORD'):
            c.type = 'WORD'
        elif (a.type == 'FLOAT'):
            c.type = 'FLOAT'
        c.value = a.value != b.value
        pc += 1
    elif (cuadruplos[pc][0] == 'gotoF'):
        if(a.value == False):
            pc = c.value
        else:
            pc += 1
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


class var_obt:
    def __init__(self, name, types, dim1, dim2, dim3):
        self.name = name
        self.type = types
        self.dim1 = dim1
        self.dim2 = dim2
        self.dim3 = dim3