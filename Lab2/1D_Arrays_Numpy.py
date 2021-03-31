#!/usr/bin/python
# 1D_Arrays_Numpy.py – explain part b questions 
# by saikumar dandla, drdo
# Last modified: 6:50 pm 31/3/21

import numpy as np

'''1) In the Spyder Console, create Numpy arrays as below with name a, b, c, .... In each case, observe the data type and the
values of the array in the Variable Explorer.'''

#a. all numbers from 10 to 20.

a = np.array([10,11,12,13,14,15,16,17,18,19,20])

#b. a float array with your predicted marks in 6 different subjects.

b = np.array([80.75,99.92,85.88,75.77,82.87,92.32], dtype = "f")

#c. A string array with names of your friends.

c = np.array(['sai', 'anji', 'shekar', 'chandra', 'bhanu'])

#d. Array with any six integers of your choice between 10 and 30.

d = np.array([12,22,18,27,29,15])

#e. Array with names of 6 cities of Tamilnadu.

e = np.array(['chennai', 'ooty', 'Kodaikanal', 'Kanyakumari', 'Coimbatore', 'Rameswaram'])


#2) A slice is an indexing mechanism to select multiple elements to form a sub-array. 

'''In the Spyder Console, do the following slicing operations on the arrays. Array names are
the ones created in Exer. 1 above. In your notebook, draw neat memory diagrams
showing the array a and each of the slices in (a) .. (i) below.'''

#a. a[1:2]

a[1:2]

#b. a[1]

a[1]

#c. a[:1]

a[:1]

#d. a[::1]

a[::1]

#e. a[::-1]

a[::-1]

#f. a[4:7]

a[4:7]

#g. a[2:]

a[2:]

#h. a[2::2]

a[2::2]

#i. a[-3:-6:-2]

a[-3:-6:-2]

3) In the Spyder Console, do the arithmetic operations indicated. In each case, observe the data type and the values of the resulting array in the Variable Explorer. 
Array names are the ones created in Exer. 1 above.

a. Square each value of the array a.

b. Find the size of the array c.

c. Explain what happens when you multiply 2 with array e.

d. Compute mean and standard deviation of array d.

4) Create array x containing 5 numbers, y containing another 5 numbers, and z containing 2 rows each with 5 numbers. Observe the results of x+y, x+z, x*y, x*z.