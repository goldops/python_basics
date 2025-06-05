number = 0
if number == 0:
    print(f"{number} is NULL")

print(f"{number} > 0 ? : {number > 0}")
print(f"{number} < 0 ? : {number < 0}")

print("----------------")

number = -5
if number < 0:
    print(f"{number} is NEGATIVE")

print(f"{number} > 0 ? : {number > 0}")
print(f"{number} < 0 ? : {number < 0}")

print("----------------")

a = 2
b = 1
if a * b <= 1:
    print("yes")
print(f"a = 2 , b = 1")
print(f"a x b <= 1 ? : {a * b <= 1}")

print("----------------")

number = .02
if number < 1 and number > 0:
    print("valid")

number = 5
if number <= 5 or number >= -5:
    print("accepted")

number = 11
if not (number == 0 and number == 10):
    print("rare!")

print("----------------")
number = 500
if number == 0:
    print(f"{number} is null")
else:
    print(f"{number} is positiive")

print("----------------")
number = -14
if number == 0:
    print(f"{number} is null")
elif number < 0: 
    print(f"{number} is negative")
else:
    print(f"{number} is positive")

print("----------------")
nom = "Bernard"
print(f"Is the third letter in {nom} an 'e'?")
if nom[2] == 'e':
    print("Yes")
else:
    print("No")

print(f"Is the second letter in {nom} an 'e' or the fourth letter an 'a'?")
if (nom[1] == 'e' or nom[3] == 'a'):
    print("Yes")
else:
    print("No")
