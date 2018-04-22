import re
import constraint
import copy
import time

var = []
variables = []
heja = []
firstletters = []
m = []

def parseLetters(variable):
    number = []
    var = []
    exponent = len(variable) - 1
    for l in variable:
        number.append(l + "*" + str(10 ** exponent))
        var.append(l)
        exponent -= 1
    return (number, var)

def constraintFunc(*args):
  
    leftside = variables[:-1]
    rightside = variables[-1]
    
    suma = 0   
    i = 0
    recnik = dict(zip(m,args))
    
    for left in leftside:
        exponent = len(left) - 1
        for letter in left:
            suma += recnik[letter] * (10 ** exponent)
            exponent -= 1 
            i += 1

    rightsum = 0
    rightexponent = len(rightside) - 1
    for r in rightside:
        rightsum += recnik[r] * (10 ** rightexponent)
        rightexponent -= 1
        
    return suma == rightsum

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

    firstletters = reduce(lambda acc, el: acc if el in acc else acc + [el], firstletters, [])
    for l in firstletters:
        heja.remove(l)
    
    problem = constraint.Problem()
    problem.addVariables(heja, range(0, 10))
    problem.addVariables(firstletters, range(1,10))
    problem.addConstraint(constraint.AllDifferentConstraint())
    problem.addConstraint(constraintFunc, m)
    start = time.time()
    resenja = problem.getSolutions()
    end = time.time()
    
    print "Time elapsed: " + str(end-start)
    print str(len(resenja)) + " solution(s)"
    for r in resenja:
        for variable in variables:
            for v in variable:
                print r[v],
            print
