array = list(map(int, input('Введите любую последовательность чисел черз пробел:').split()))
number = int(input('Введите любое число:'))

while number:
    if number <= min(array):
        print('Введёное число не соответствует критериям поиска, введеное число не превышает  максимальное и больше минимального')
        number = int(input('Введите любое число:'))
    elif number > max(array):
        print('Введёное число не соответствует критериям поиска, введеное число не превышает  максимальное и больше минимального')
        number = int(input('Введите любое число:'))
    else:
        break

def buble(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array_one = buble(array)

def binar_search(array_one, number, left, right):
    if left > right:
        return False
    middle = (left + right) // 2
    if array_one[middle] == number:
        return middle
    elif number < array_one[middle]:
        return binar_search(array_one, number, left, middle -1)
    else:
        return binar_search(array_one, number, middle + 1, right)

print(binar_search(array_one, number, 0, len(array_one)-1))







