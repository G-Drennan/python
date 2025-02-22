# Now we've figured out how to get our program to do one thing. But sometimes
# you want your program to do multiple things. For example:

print("Type a number:")
num1 = int(input())

if (num1 == 5):
  print("You typed 5!")
elif (num1==6):
  print("You typed 6!")
else:
  print("You didn't type 5 or 6!")

# Using this `if`, you've steered your program down one set of commands if 
# `num1` is 5, and a different set of commands if `num1` is not 5. Since 
# you're controlling your program's flow, statements like `if` are called 
# 'control structures'.

# What other control structures can we use? Here's another one:
print("Type a number:")
num1 = int(input())

while (num1 > 0):
  #count backward from the typed number
  num1 = num1 - 1
  print(num1)

print("blastoff!")

# Guess what this program is going to do? Run it, I'll let you find out.

# Notice that in python, you need to push forward (a.k.a. indent) the commands
# that are inside of your control structures, so that python knows which 
# commands are affected by the control structure and which ones arent.

# Using these control structures you can make very complicated things. 

for x in range(1,11):
  print("step "+str(x))
  #its no inclusive of 11