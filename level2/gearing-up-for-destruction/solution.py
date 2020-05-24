#   As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple - just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

#   The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

#   Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

#   For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

#   The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

def getGCD(a, b):
    if b > 0: 
        return getGCD(b, a%b)
    return a

def simplify(a, b):
    gcd = getGCD(abs(a), abs(b))
    a /= gcd
    b /= gcd
    return a, b

def solution(pegs):
    n = len(pegs)
    diff = [pegs[i+1] - pegs[i] for i in range(n-1)]
    
    v = sum([(diff[i] * (-1)**(i)) for i in range(n-1)])
    num = 2 - (-1)**(n-1)
    v, num = simplify(v, num)
    
    if v < 0:
        v = -v
        num = -num
    
    if v < 1 or num < 0:
        return [-1, -1]

    a, b = 2*v, num
    for i in range(n-1):
        a = diff[i]*b - a
        if a < b:
            return [-1, -1]
    return [2*v, num]