#!/usr/bin/python
# Analysing_Plotting_Data.py – explain part c questions 
# by saikumar dandla, drdo
# Last modified: 6:50 pm 31/3/21

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
# plt.plot(a)
# plt.semilogx(), plt.semilogy()
# plt.loglog()
# plt.hist()
# plt.scatter()
# plt.bar()
# plt.pie()
# plt.savefig()
# plt.title()
# plt.xlabel(), plt.ylabel()



'''1) Read the data from Marks.csv into a Numpy array marks.
(a) Compute the cutoffs for different grades as per the policy: 
    O: > μ + 1.85 σ, 
    A: > μ + 0.85 σ; 
    B: > μ – 0.05 σ; 
    C: > μ – 0.85 σ; 
    D: > μ – 1.8 σ; 
    E > μ/2, where μ is the mean and σ is the standard deviation.'''
    
    
    
#(b) Compute the 5th, 20th, 50th, 80th and 95th percentiles. Compare these to the grade cutoffs.





'''2) Create a Numpy array x containing numbers from 0 to 30 in steps of 0.2. Using matplotlib.pyplot:'''

#a. Plot the curves for sin(x) and cos(x) on one figure. Use different colours, say blue and red.

#b. Plot the curve for exp(-x). Experiment with the plot functions semilogx(), semilogy() and loglog() instead of plot().





'''3) The CSV file CourseMarks.csv has marks of students in 5 subjects. The first line gives the column headings. 
Read the data into an array using np.loadtxt().'''

    
#a. Draw a scatter plot showing the relationship between the marks in Chemistry and History.


'''b. Draw a histogram of the marks in Maths. Experiment with different numbers of bins from 2 to 15. 
Which histogram gives the best insight into the performance in Maths?'''



'''4) The CSV file India_timeline.csv contains data on potato production from 1961 – 2017.'''

#1 Read the file and plot the following:
    
data = np.genfromtxt('C:/Users/matlab/Desktop/RP502P/Lab2/potato-yields.csv', delimiter=',')

data

#a. Draw a scatter plot of Production(tonnes) vs. Areaharvested(ha)


#b. Draw a bar graph of the Yield over the years.