import random

for i in range(50):
    print(i)

print("----------------")

matrice = [
    ["Pierre", 34, "Paris"],
    ["Basile", 29, "Bordeaux"],
    ["Aurélie", 24, "Auch"]
]

for i in range(len(matrice[0])):
    for j in range(len(matrice[i])):
        print(f"Individu", i, "information n°", j, ":", matrice[i][j])

print("----------------")

number = random.randint(0, 100)

while number <= 80:
    print(number)
    number = random.randint(0, 100)
print(f"End: last number {number}")

print("----------------")

while number <= 95:
    print(number)
    number = random.randint(0, 100)
print(f"End: last number {number}")

print("----------------")

iteration = 0

while number <= 95 and iteration < 5:
    print(number)
    iteration += 1
    number = random.randint(0, 100)

if iteration == 5: 
    print(f"Fin stoppée: last number {number}")
else:
    print(f"Fin normale: last number {number}")

print("----------------")
