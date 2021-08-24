#asks for a input of a int and a string and scanse it
print("Type the first digits of student ID: ")
ID=int(input())
print("You name: ")
name=input()
#prints name one less time than the number input
for x in range(0,ID-1):
 print(name)
