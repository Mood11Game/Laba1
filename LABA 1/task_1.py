numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

for i in range(0, len(numbers)): #Поиск индекса пустого элемента
    if (numbers[i]==None):
        index_None=i

summa=0
for i in range(0, len(numbers)): #сумма чисел, не включаяя путой элемент
    if (i==index_None):
        pass
    else:
        summa+=numbers[i]

sr_arm=summa/(len(numbers)) #ср. арифметическое

numbers[index_None]=sr_arm
print("Измененный список:", numbers)
