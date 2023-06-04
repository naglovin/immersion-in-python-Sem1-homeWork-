# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

ATTEMPTS = 10
count = 1
number = None
num = randint(0, 1000)
print(num)

while ATTEMPTS >= count:
    print("Попытка № ", count)
    count +=1

    print("Введите число от 0 до 1000")
    number = int(input())
    if number < num:
        print("Введеная цифра Меньше загаданного числа")
        continue
    elif number > num:
        print("Введеная цифра Больше загаданного числа")
        continue
    elif number == num:
        print("Вы угадали! Поздравляю")
        quit()
else:
    print("Вы потратили все попытки, мне очень жаль =)")

print("Загаданное число было: ", num)




#for count in range(ATTEMPTS):
#    my_number = int(input("Введите число от 0 до 1000: "))
#    if my_number == num:
#        print("Вы угадали, загаданная цифры была: ", num)
#        break
#    elif my_number < num:
#        count +=1
#    else:
#       print("Попробуй больше")
#       number_of_attempts +=1
#else:
#    print("Вы к сожалению проиграли =( загаданная цифра была: ", num)

