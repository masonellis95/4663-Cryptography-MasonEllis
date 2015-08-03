###############################################
# Name: Mason Ellis
# Class: CMPS 4663 Cryptography
# Date: 2 August 2015
# Program 3 - Elliptic Curves
###############################################

import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt

"""
    derivative(pt, curve)
    
    @param1: pt - two number list
    @param2: curve - two number list
    
    returns the derivative of the curve at a certain point.
"""
def derivative(pt, curve):
    #The Derivative for the curve.
    return float((3 * pt[0] ** 2 + curve[0]))/(2*pt[1])
    
"""
    findPoint(pt1, pt2, curve):
    
    @param1: pt1 - two number list
    @param2: pt2 - two number list
    @param3: curve - two number list
    
    Returns the third point on an elliptic curve given two
    other points on the same line.
"""
def findPoint(pt1, pt2, curve):
    # If the two points are equal, we must use the derivative 
    # to get the slope of the tangent line.
    if(pt1 == pt2):
        m = derivative(pt1, curve)
    else:
        if(pt1[1] != pt2[1]):
            m = getSlope(pt1, pt2)
    
    #Calculates the x and y values of the third point.
    x3 = m ** 2 - pt1[0] - pt2[0]
    y3 = (x3 ** 3 + curve[0] * x3 + curve[1]) ** .5
    
    return[x3, y3]
    
    
"""
    getSlope(pt1, pt2)
    
    @param1: pt1 - two number list.
    @param2: pt2 - two number list.
    
    Returns the slope between two points.
"""
def getSlope(pt1, pt2):
    #Change in y over change in x.
    return (float(pt2[1]) - pt1[1])/ (float(pt2[0]) - pt1[0])
    
"""
    onCurve(pt, curve)
    
    @param1: pt - two number list.
    @param2: curve - two number list.
    
    Returns a 1 if the point is on the curve and a 
    0 otherwise.
"""
def onCurve(pt, curve):
    #Defaults to true.
    on_Curve = 1
    if (pt[1] ** 2 != pt[0] ** 3 + curve[0] * pt[0] + curve[1]):
        # Returns false if the point is not on the curve.
        on_Curve = 0
    return on_Curve
    
"""
    graph(pt1, pt2, pt3, curve)
    
    @param1: pt1 - two number list
    @param2: pt2 - two number list
    @param3: pt3 - two number list
    @param4: curve - two number list
    
    This function will graph the curve along with our three
    points and the line that passes through them.
"""
    
def graph(pt1, pt2, pt3, curve):    
    
    #Values defining our curve read in from a list.
    a = curve[0]
    b = curve[1]
    
    # Create three points
    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt2[0]
    y2 = pt2[1]
    x3 = pt3[0]
    y3 = pt3[1]    
    
    # Determines width and height of plot. Determined by the 
    # Maximum x and y values with 5 "cushion" units added to 
    # both dimensions.
    w = max(x1, x2, x3) + 5
    h = max(y1, y2, y3) + 5 
    
    an1 = plt.annotate("Mason Ellis", xy=(-w+2 , h-2), xycoords="data",
              va="center", ha="center",
              bbox=dict(boxstyle="round", fc="w"))
              
    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]
    
    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) + ax + b ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a *x + b ), [0])
    
    #Get the slope of the line
    if (pt1 != pt2):
        m = (y1-y2)/(x1-x2)
    else:
        m = derivative(pt1, curve)
    
    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro')
    
    # Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )
    
    plt.plot(x2, y2,'ro')
    
    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )
    
    # Use a contour plot to draw the line (in pink) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))
    
    # I hard coded the third point, YOU will use good ol mathematics to find
    # the third point
    plt.plot(x3, y3,'yo')
    
    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1,y3-1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )
    
    # Show a grid background on our plot
    plt.grid()
    
    # Show the plot
    plt.show()

def main():
    
    parser = argparse.ArgumentParser()

    # Reads in the arguments from the command line.
    # Passes in the curve and two points.
    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="")
    parser.add_argument("-y1",dest="y1", help="")
    parser.add_argument("-x2",dest="x2", help="")
    parser.add_argument("-y2",dest="y2", help="")

    args = parser.parse_args()
    
    # A two number list to contain the a and b values
    # for the Elliptic Curve y^2 = x^3 + ax + b.
    Curve = [int(args.a),int(args.b)]
    # Two two number lists to store the given points.
    Point_1 = [int(args.x1),int(args.y1)]
    Point_2 = [int(args.x2),int(args.y2)]
    # A third two number list to contain the third point that
    # the program will find.
    Point_3 = [0,0]
    
    # Tests to see if the points are actually on the curve.
    # If they are not, The progam will skip the evaluation
    # of point 3 and the graphing of the curve and points.
    if(onCurve(Point_1,Curve)) == 0:
        print("Point 1 is not located on the curve.")
    elif(onCurve(Point_2,Curve)) == 0:
        print("Point 2 is not located on the curve.") 
        
    # If the x-values of the two points are equal, 
    # the line between these two points is vertical
    # and point 3 does not exist.    
    if (Point_1[0] == Point_2[0] and Point_1 != Point_2):
            print("The line between these two points is Vertical.")
            print("Point 3 does not exist.")
    else:
        # If the two points are equal.
        if(Point_1 == Point_2):
            Point_3 = findPoint(Point_1, Point_2, Curve) 
        # If point 1 is a point at infinity.
        elif(Point_1[1] == 0):
            Point_3 = Point_2
        # If point 2 is a point at infinity.
        elif(Point_2[1] == 0):
            Point_3 = Point_1
        else:
            Point_3 = findPoint(Point_1, Point_2, Curve)
        
        #Runs the Graph.
        graph(Point_1, Point_2, Point_3, Curve)
        
if __name__ == '__main__':
    main()
