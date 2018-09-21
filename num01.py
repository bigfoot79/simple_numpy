
# https://docs.scipy.org/doc/numpy/reference/routines.html
# https://www.tutorialspoint.com/numpy/numpy_matrix_library.htm


# import declarations
import numpy.matlib 
import numpy as np  
from matplotlib import pyplot as plt 
from decimal import *

# method/statement declarations

    

def main():

    # simple matrix multiplication

    x = np.matrix('1,2,3;4,5,6')
    y = np.matrix('1,2;3,4;5,6') 
    print x
    print y

    z = x*y
    print z
    
    z = y*x
    print z


    # bitwise AND operation

    x = 13
    y = 17
    print x
    print y

    z = numpy.bitwise_and(x,y)
    print z
    

    z = numpy.bitwise_or(x,y)
    print z

    # statistical functions

    # (a) identify the 50th percentile
    a = np.array([2,3,4,5,6,7,8,9])
    print a
    b = np.percentile(a,50)
    print b

    # (b) add arrays together
    a = np.array([1,2])
    b = np.array([3,4])
    c = np.add(a,b)
    print c

    # matplotlib example
    x = np.arange(1,11,0.1) 
    y = 2 * (x*x) + 5 
    y = np.sin(x)
    plt.title("Matplotlib demo") 
    plt.xlabel("x axis caption") 
    plt.ylabel("y axis caption")
    plt.plot(x,y) 
    plt.show()
    
    # standard I/O operations

    x = np.arange(1,10.1,0.1)
    np.savetxt('outfile.txt',x)
    y = np.loadtxt('outfile.txt')
    print y

    # simple arithmetic operations
    # Decimal numbers don't round correctly, as 10*[0.1] does not equal 1.0
    a = sum([0.1]*10)
    print a

    print(sum([0.1]*10)==1.0)

    print(sum([Decimal('0.1')]*10)==Decimal('1.0'))

if __name__ == '__main__':

    main()
    
