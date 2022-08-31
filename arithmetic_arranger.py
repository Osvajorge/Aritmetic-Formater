def exceptions(n1, n2, operator):
    #Only digit exception
    try:
        int(n1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(n2)
    except:
        return "Error: Numbers must only contain digits."
    #Too many digits. (more than 4)
    try:
        if len(n1) > 4 or len(n2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    # Operator must be + | - exception.

    try:
        if operator != '+' and operator != '-':
            raise ValueError
    except:
        return "Error: Operator must be '+' or '-'."
    return ""


def arithmetic_arranger():
    print('1' + exceptions(123,'f','+'))
    print('2' + exceptions(1.5,124,'+'))
    print('3' + exceptions(124,1,'+'))
    print('4' + exceptions(124,125,'+'))
    print('5' + exceptions(123,1,'*'))

arithmetic_arranger()