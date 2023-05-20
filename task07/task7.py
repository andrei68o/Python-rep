#from xlwt import Workbook

#wb = Workbook()

#wb.add_sheet("Sheet 1")

def get_max_salary(f,max_sal_local):
    for line in f.readlines()[1:]:
        data = line.split(",")
        data[1] = int(data[1])
        if(max_sal_local < data[1]):
            max_sal_local = data[1]
    return max_sal_local




f1 = open("f1.txt", 'r')
f2 = open("f2.txt", 'r')
f3 = open("f3.txt", 'r')

max_sal = 0

max_sal_local = 0

max_sal_f1 = get_max_salary(f1, max_sal_local)
max_sal_f2 = get_max_salary(f2, max_sal_local)
max_sal_f3 = get_max_salary(f3, max_sal_local)

max_sal = max_sal_f3

print(max_sal)

suma = 0
for line in f3.readlines()[1:]:
    print(line)
