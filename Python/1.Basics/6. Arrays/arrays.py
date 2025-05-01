# ✅ Block — Arrays.

#what is an array?
    # Is a collection of items stored in a sigle variable.
    # In Python, we often use list as dynacimic arrays, but there's also a special array module for fixed type arrays.
    # Are used when you want to stoe multiple values of the same type (numbers, for example) and perform operations on them.

# Difference between arrays and list?

    # List: 
        # can store different data types
        # very flexible
        # synta: [1, 2, 3]
        # Slower for larger calculations

    # Arrays:
        # Must store only elements of the same type
        # More efficient if all items are of one type
        # Created using: array.array('i', [1, 2, 3])
        # Faster and more memory efficient for large numerical data.


# NumPy 
    
    # What is?
        # is a python library used for workinf with large arrays, matrices and numerical computations
        # faster, powerful, and more efficient than python lists or the standard array module.
        # can me multi-dimensional (not only 1D)

# ➡️ Task 1) Create a 1D Numpy array with numbers from 1 to 10

            #💡 Explanation: 
                #- use np.arange() to create ranges.
                #- np.arange(start, stop +1)

            #💡 step by step:
                #- Import numpy
                #- use np.arange(1,11)

import numpy as np

array_1d = np.arange(1,11)
print(array_1d)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import numpy as np
array_1d = np.arange(1,20)
print(array_1d)



# ➡️ Task 2) Create an arrya of zeros with length 5

            #💡 Task and explanation: 
                #- Make an array with 5 zeros
                #- use np.zeros(n)

            #💡 step by step:
                # import numpy
                # use np.zeros(5)

import numpy as npp

array_zeros = npp.zeros(5)
print(array_zeros)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



























# ➡️ Task 

            #💡 Explanation: 
                #- 

            #💡 step by step:
                #-


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>