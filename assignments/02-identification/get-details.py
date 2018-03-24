name = input("What is your name? ")
n = len(name)
# If length of name is greater than 20,
# print something
if n > 20 :
   print ("something")


age = input("What is your age? ")
age = int(age)
# If age is less than 10, print "Smol"
if age < 10 :
   print ("Smol")
# ELse if age is between 10 and 20, print "Big boi"
elif age > 10 and age < 20 :
    print ("Big boi")
# Else, print "Big big boi"
else :
    print("Big big boi")


coolness = input("Rate your coolness out of 100.0")
c = float(coolness)
# If coolness is more than 100.0, just print some error
if c > 100.0 :
    print ("some error")


# Now print a string like
# My name is Arnold Tan, I am 69 and I'm Really Cool


