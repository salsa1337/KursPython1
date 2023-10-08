numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
summa1 = sum(numbers[:4:])
summa2 = sum(numbers[5::])
dlina = len(numbers)
numbers[4] = (summa1+summa2)/dlina

print("Измененный список:", numbers)
