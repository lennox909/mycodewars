#You are given two interior angles (in degrees) of a triangle.

#Write a function to return the 3rd.

#Note: only positive integers will be tested.

#https://en.wikipedia.org/wiki/Triangle

#My solution 
def other_angle(a, b):
    
    other_angle = 180 - (a + b)
    return other_angle
    pass

