
# https://docs.scipy.org/doc/numpy/reference/routines.html
# https://www.tutorialspoint.com/numpy/numpy_matrix_library.htm


# import declarations
import numpy.matlib 
import numpy as np  


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

    # identify the 50th percentile
    a = np.array([2,3,4,5,6,7,8,9])
    print a
    b = np.percentile(a,50)
    print b

    
          
if __name__ == '__main__':

    main()
    
