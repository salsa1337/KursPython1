numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_item = 4
summa = sum(numbers[:missing_item]) + sum(numbers[missing_item+1:])
count = len(numbers)
average = summa/count

numbers[missing_item] = average
print("Измененный список:", numbers)
