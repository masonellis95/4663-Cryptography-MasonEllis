###############################################
# Name: Mason Ellis
# Class: CMPS 4663 Cryptography
# Date: 2 August 2015
# Program 3 - Elliptic Curves
###############################################

import argparse
import EllipticCurves as EC

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
    if(EC.onCurve(Point_1,Curve)) == 0:
        print("Point 1 is not located on the curve.")
    elif(EC.onCurve(Point_2,Curve)) == 0:
        print("Point 2 is not located on the curve.") 
       
    else:
        # If the x-values of the two points are equal, 
        # the line between these two points is vertical
        # and point 3 does not exist.    
        if (Point_1[0] == Point_2[0] and Point_1 != Point_2):
                print("The line between these two points is Vertical.")
                print("Point 3 does not exist.")
        else:
            # If the two points are equal.
            if(Point_1 == Point_2):
                Point_3 = EC.findPoint(Point_1, Point_2, Curve) 
            # If point 1 is a point at infinity.
            elif(Point_1[1] == 0):
                Point_3 = Point_2
            # If point 2 is a point at infinity.
            elif(Point_2[1] == 0):
                Point_3 = Point_1
            else:
                Point_3 = EC.findPoint(Point_1, Point_2, Curve)
            
            #Runs the Graph.
            EC.graph(Point_1, Point_2, Point_3, Curve)
            
if __name__ == '__main__':
    main()
