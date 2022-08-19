print("Cervantes, Ian R.")
print("P-M1: ACT3 - RPA Implementation")
print('─' * 40)

num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
print("\n")

answer = 0
add = []
print(num1,num2)
input()
while num1 != 0:
   if (num1%2 != 0):
      answer=answer+num2
      add.append(num2)
      num2=num2*2
      num1=num1//2
      if (num1 != 0):
        print(num1,num2)
        print("\nPress Enter")
        input()
   if (num1%2 == 0):
      num2=num2*2
      num1=num1//2
      if (num1 != 0):
        print(num1,num2)
        print("\nPress Enter")
        input()

print("\n")
print(' + '.join(map(str,add)))
print("the product is",(answer))