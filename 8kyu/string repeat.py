# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

#Examples (input -> output)
#6, "I"     -> "IIIIII"
#5, "Hello" -> "HelloHelloHelloHelloHello"

# My solution 

def repeat_str(repeat, string):
    repeated_str = string * repeat
    return repeated_str