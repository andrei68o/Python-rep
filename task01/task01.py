import os


for root, dirs, files in os.walk(os.getcwd()):
    maxim = 0
    for file in files:
        if ".txt" in file:
            a = open(file, 'r')
            k = 0

            for line in a.readlines():
                data = line.split()
                for word in data:
                    if "Lorem" in word:
                        k += 1
            #print(k)
            if k > maxim:
                maxim = k
                file_size = os.path.getsize(file)
    b = open("task01.txt", 'w')
    b.write(f"Numarul maxim de aparitii al cuvantului Lorem este de {maxim} ori \n")
    b.write(f"Dimensiunea fisierului ce contine numarul maxim de aparitii al cuvantului Lorem este de {file_size} bytes")








