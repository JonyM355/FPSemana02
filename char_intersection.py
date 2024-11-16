text1 = input("Frase 1: ")
set1 = set(text1.split())

text2 = input("Frase 2: ")
set2 = set(text2.split())

interseçao = set1.intersection(set2)

print(" ".join(interseçao))