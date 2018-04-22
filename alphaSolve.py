import re
import constraint
import copy

var = []
variables = []
heja = []
firstletters = []

def parseLetters(variable):
    number = []
    var = []
    exponent = len(variable) - 1
    for l in variable:
        number.append(l + "*" + str(10 ** exponent))
        var.append(l)
        exponent -= 1
    return (number, var)

# *args -> ['a','l','p'..]
# var -> ['a*1000', ...]
# variables -> [alpha, beta...]


def constraintFunc(*args):
  
    leftside = variables[:-1]
    rightside = variables[-1]
    
    suma = 0
   
    i = 0
    recnik = dict(zip(heja,args))
    #print args
    print dict(zip(heja,args))
    #print 

    for left in leftside:
        #print left, "levo"
        exponent = len(left) - 1
        for letter in left:
            suma += recnik[letter] * (10 ** exponent)
            exponent -= 1 
            i += 1
            #print suma, "levo"

    rightsum = 0
    rightexponent = len(rightside) - 1
    #print rightexponent
    #print rightside
    for r in rightside:
        rightsum += recnik[r] * (10 ** rightexponent)
        rightexponent -= 1
        #print rightsum, "desn", r
        
    return suma == rightsum
        



# TODO: pisemo program koji sam sebe prepravlja zapravo


if __name__ == "__main__":
    inputString = raw_input("Enter an expression")

    variables = re.split(r'\+|\=| ', inputString)

    letters = []
    

    for v in variables:
        letters.append(parseLetters(v)[1])
        var.append(parseLetters(v)[0])
        firstletters.append(v[0])

    tmp = reduce(lambda acc, el: acc + el, letters, [])
    m = reduce(lambda acc, el: acc if el in acc else acc + [el], tmp, [])
    i = 0
    heja = copy.deepcopy(m)
    if len(m) > 10:
        exit("Enter up to 10 distinct letters")

    #TODO: ocisti ove grozote

    #print heja
    firstletters = reduce(lambda acc, el: acc if el in acc else acc + [el], firstletters, [])
    for l in firstletters:
        heja.remove(l)
        
    print heja
    print firstletters
    print m
    problem = constraint.Problem()

    problem.addVariables(heja, range(0, 10))
    problem.addVariables(firstletters, range(1,10))
    problem.addConstraint(constraint.AllDifferentConstraint())
    problem.addConstraint(constraintFunc, m)
    resenja = problem.getSolutions()
    for r in resenja:
        print r['s'], r['e'], r['n'], r['d'] 
        print r['m'], r['o'], r['r'], r['e']
        print r['m'], r['o'], r['n'], r['e'], r['y']  
    

# TODO: make multiple argumets constraint function
