numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

t = numbers.index(None) # находим расположение пропущенного элемента в списке
numbers[t] = 0 # присваиваем ему значение 0, так, чтобы этот элемент не вносил вклада в сумму для среднего арифметического
m = sum(numbers) / len(numbers) # среднее арифметическое списка
numbers[t] = m # замена пропущенного элемента значением среднего арифметического
print("Измененный список:", numbers)
