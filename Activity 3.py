words = input("Enter an anywords: ")
lower = 0
upper = 0

for i in words:
      if (i.islower()):
            lower += 1
      else:
            upper += 1
            
print("The number of uppercase letters is:", upper)
print("The number of lowercase letters is:", lower)
