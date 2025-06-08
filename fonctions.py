import os
import sys
import numpy as np

def carre(x):
    return x * x

print(carre(3))

def fonction_mot(mot):
    if mot[0] == 'a':
        print(f"{mot} starts with an 'a'")
        return 1
    print(f"{mot} doesn't start with an 'a'")
    return 0
vecteur = np.asarray(["abbaba", "bcaabb", "cbcbca", "abacba", "cbbaca", "abbbaa"])
fonction_mot_vectorise = np.vectorize(fonction_mot)
fonction_mot_vectorise(vecteur)

new_list = np.random.random(size=20) * 2 - 1

def modifier_pair(liste, f):
    for i in range(len(liste)):
        if i % 2 == 0:
            liste[i] = f(liste[i])
    print(liste)
    return liste

modifier_pair(new_list, lambda x: x ** 2 - 3 * x + 4)

print("------------------")

names = ["A", "B", "C", "D", "E"]
values = [3, 1, 5, 6, 4]

for x, y in zip(names, values):
    print(x, ":", y)


print("------------------")

