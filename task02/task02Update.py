"""
Acest script citeste date dintr-un fisier si incearca sa calculeze care este cuvantul ce contine cele mai
multe caractere.
"""

import io

# Citim datele
f = open("input.txt", "r") # Am modificat permisiunea de scriere cu cea de citire
no_of_chars= 0
word = ""
for line in f.readlines():
    if len(line) > no_of_chars:  #Aflam numarul maxim de caractere si salvam cuvantul intr-o variabila pentru afisare
        word = line
        no_of_chars = len(word)

print(f"Cuvantul care contine cele mai multe caractere este {word}" )
print(f"Lungimea acestuia este {no_of_chars}")