import re


# import constraint


def parseLetters(variable):
    number = []
    var = []
    exponent = len(variable) - 1
    for l in variable:
        number.append(l + "*" + str(10 ** exponent))
        var.append(l)
        exponent -= 1
    return (number, var)
'''
# *args -> ['a','l','p'..]
# var -> ['a*1000', ...]
# variables -> [alpha, beta...]
# def constraintFunc(*args, var, variables):
#   
#   leftside = variables[:-1]
#   rightside = variables[-1]
#   idi za jednu manje
#
#
#   sum = 0
#   
#   for left in leftside:
#       exponent = len(left)
#       for letter in left:
#           sum += args[i] * 10 ** exponent
#           exponent -= 1 
#
#

TODO: pisemo program koji sam sebe prepravlja zapravo

'''

def prepareArgs(var):
    equals = var[-1]
    leftside = var[:-1]
    # print leftside
    # print equals

    leftsum = 0
    rightsum = 0

    '''
    for ls in leftside:
        exponent = len(ls) - 1
        for n in ls:
            leftsum += int(n) * (10 ** exponent)

    for l in equals:
        exponent = len(equals) - 1
        rightsum += int(l) * (10 ** exponent)
    '''

    #print leftsum + rightsum


if __name__ == "__main__":

    inputString = raw_input("Enter an expression")

    variables = re.split(r'\+|\=| ', inputString)

    letters = []
    var = []

    for v in variables:
        # print v
        letters.append(parseLetters(v)[1])
        var.append(parseLetters(v)[0])

    tmp = reduce(lambda acc, el: acc + el, letters, [])
    m = reduce(lambda acc, el: acc if el in acc else acc + [el], tmp, [])

    if len(m) > 10:
        exit("Enter up to 10 distinct letters")

    print m
    print var
    print
    print variables
    prepareArgs(var)

    # problem = constraint.Problem()

    # problem.addVariables(m, range(0, 10))

# TODO: make multiple argumets constraint function
