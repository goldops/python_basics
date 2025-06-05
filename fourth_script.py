first_list = [4, 5, 6, 7, 8, 9]
print(first_list)
print(f"nombre d'éléments dans la liste: ", len(first_list))
print(first_list[1])

first_list.append(10)
print(first_list)

first_list.append(100)
print(first_list)

person = ["Jean", "Dupont", 35]
print(f"{person[0]}, {person[1]}, a, {person[2]}, ans.")

person.append("Paris")
print(f"{person[0]}, {person[1]}, a, {person[2]}, ans et habite à, {person[3]}")