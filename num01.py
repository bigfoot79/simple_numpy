
# https://docs.scipy.org/doc/numpy/reference/routines.html
# https://www.tutorialspoint.com/numpy/numpy_matrix_library.htm


# import declarations
import numpy.matlib 
import numpy as np  


# method/statement declarations

    

def main():

    x = np.matrix('1,2,3;4,5,6')
    y = np.matrix('1,2;3,4;5,6') 
    print x
    print y

    z = x*y
    print z
    
          
if __name__ == '__main__':

    main()
    
