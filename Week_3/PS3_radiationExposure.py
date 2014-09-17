
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    amountExposed = 0.0
    point = start
    while point < stop:
        amountExposed += f(point)*step
        point += step
    return amountExposed

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    
print radiationExposure(12, 16, 1)
print 6.848645835538622
print radiationExposure(0, 5, 1)
print radiationExposure(0, 5, 0.5)
print 39.10318784326239
print radiationExposure(5, 11, 1)
print 22.94241041057671
print radiationExposure(0, 11, 1)
print 62.0455982538
print radiationExposure(40, 100, 1.5)
print 0.434612356115

def f(x):
	import math
	return 400*math.e**(math.log(0.5)/3.66 * x)

print radiationExposure(0, 4, 0.25)
print 1148.6783342153556

