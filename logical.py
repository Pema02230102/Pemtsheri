#AND Operator (Both conditions should be True)

x = 5
print(x > 4 and x < 6) #TRUE

y = 10
print(y > 8 and y % 3 == 0) # FALSE

#OR Operator (True if one condition is is True)

x = 12
print(x > 10 or x <= 0) # TRUE

y = 8 
print(y > 9 or y % 3 == 0) #FALSE

#NOT Operator (Reverse)

x = 24
print(not (x > 20 and x < 25)) # FALSE

y = 50
print(not(y > 49 and y % 3 == 0) ) # TRUE
