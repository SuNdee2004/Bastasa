name = input("Enter your Name: ")
sci = input("Enter your Science Grade: ")
math = input("Enter your Math Grade: ")
eng = input("Enter your English Grade: ")
total = float(sci) + float(math) + float(eng)
avg = float(total) / 3

print("RESULTS:")
print("Name: ", name)
print("Science: ", sci)
print("Math: ", math)
print("English: ", eng)
print("AVERAGE: " + str(avg) + "%")

if avg > 75:
    print("Congratulations You Passed!")
else:
    print("You Failed!")
