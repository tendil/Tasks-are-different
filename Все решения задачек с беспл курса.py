Блок 1, Команды print и input #####################################################################################################################

#1
print("Здравствуй, мир!")

#2
print('4', '8', '15', '16', '23', '42')

#3
print('4')
print('8')
print('15')
print('16')
print('23')
print('42')

#4
z = "*"
for j in range(7):
 print(z)
 z += "*"

 #5
 name = input()
print('Привет,', name)

#6
name = input()
print(name,  "- чемпион!")

#7
text1 = input()
text2 = input()
text3 = input()

print(text1,)
print(text2,)
print(text3,)

#8
text1 = input()
text2 = input()
text3 = input()

print(text3,)
print(text2,)
print(text1,)


Блок 2, параметры sep и end ######################################################################################################################

#1
print('I', 'like', 'Python', sep='***')


#2
test1=input('')
test2=input('')
test3=input('')
test4=input('')

print(test2, test3, test4, sep=test1)

#3
name = input()
print('Привет,', name, end='!')

Блок 3, Целочисельная арифметика, Ч1 ##############################################################################################################

#1
num = int(input())
print(num)
print (num +1)
print (num +2)

#2
num1=int(input())
num2=int(input())
num3=int(input())

print(int(num1 + num2 + num3))

#3
l = int(input())

print('Объем =',l**3)
print('Площадь полной поверхности =',6*l**2)

#4
a = int(input())
b = int(input())

num1 = 3*(a + b)**3 + 275*b**2 - 127 * a - 41 

print(num1)

#5
num = int(input())
num1 = int(num + 1)
num2 = int(num - 1)

print('Следующее за числом', num, 'число:', num1)
print('Для числа', num, 'предыдущее число:', num2)

#6
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print((a + b + c + d)*3)

#7
num1 = int(input())
num2 = int(input())

print(num1, '+', num2, '=', num1+num2)
print(num1, '-', num2, '=', num1-num2)
print(num1, '*', num2, '=', num1*num2)

#8
a1 = int(input())
d = int(input())
n = int(input())

num1 = (a1 + d * (n - 1))

print(num1)

#9
a1 = int(input())

print(a1, a1 * 2, a1 * 3, a1 * 4, a1 * 5, sep='---')

Блок 3, Целочисельная арифметика, Ч2 #############################################################################################################

#1
b1, q, n = int(input()), int(input()), int(input())

num = (b1 * q**(n-1))
print(num)

#2
sm = int(input())
sm //= 100
print(sm)

#3
n = int(input())
k = int(input())

x = k // n
z = k % n
print(x)
print(z)

#4
pop = int(input())

a = (pop // 2)
b = (pop % 2)
c = (a + b)

print(c)

#5
num = int(input())

a = (num + 3)
b = (a // 4)

print(b)

#6
min = int(input())

hour = (min // 60)
min1 = (min % 60)

print(min, 'мин -', 'это', hour, 'час', min1, 'минут.')

#7
num = int(input())

digit3 = num % 10
digit2 =(num // 10) % 10
digit1 =num // 100

print('Сумма цифр =', digit3 + digit2 + digit1)
print('Произведение цифр =', digit3 * digit2 * digit1)

#8
num = int(input())

a = num % 10
b = (num // 10) % 10
c = num // 100

print(c, b, a, sep='')
print(c, a, b, sep='')
print(b, c, a, sep='')
print(b, a, c, sep='')
print(a, c, b, sep='')
print(a, b, c, sep='')

#9
num = int(input())

d = (num % 10**4) // 10**3
c = (num % 10**3) // 10**2
b = (num % 10**2) // 10**1
a = (num % 10**1) // 10**0



print('Цифра в позиции тысяч равна', d)
print('Цифра в позиции сотен равна', c)
print('Цифра в позиции десятков равна', b)
print('Цифра в позиции единиц равна', a)


Блок 4, Итоговая рaбота на ввод-вывод данных #####################################################################################################

#1                                                                                                                                                         
print('*****************')
print('*               *')
print('*               *')
print('*****************')

#2
a = int(input())
b = int(input())

print('Квадрат суммы', a, 'и', b, 'равен', (a+b)**2)
print('Сумма квадратов', a, 'и', b, 'равна', (a**2) + (b**2))

#3
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print((a**b)+(c**d))

#4
num = int(input())

print(num * 123)

Блок 5, Условный оператор ########################################################################################################################

#1
psw1 = input()
psw2 = input()

if psw1 == psw2:
    print('Пароль принят')
else: 
    print('Пароль не принят')


#2
intnum = int(input())
if intnum % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

#3
num = int(input())

d = (num % 10**4) // 10**3
c = (num % 10**3) // 10**2
b = (num % 10**2) // 10**1
a = (num % 10**1) // 10**0

if (d + a) == (c - b):
    print('ДА')
else:
    print('НЕТ')
    
#4
age = int(input())

if age < 18:
    print('Доступ запрещен')
else: 
    print('Доступ разрешен')
    
#5
a1 = int(input())
a2 = int(input())
a3 = int(input())

if a3 == (a2 - a1) + a2:
    print('YES')
else:
    print('NO')

#6
num1, num2 = int(input()), int(input())

if num1 <= num2:
    print(num1)
elif num1 >= num2:
    print(num2)
    
#7
 a, b, c, d = int(input()), int(input()), int(input()), int(input())

min = a

if min > b:
    min = b
if min > c:
    min = c
if min > d:
    min = d
    
print(min)

#8
age = int(input())
    
if age <= 13:
    print("детство")
elif 14 <= age <= 24:
    print("молодость")
elif 25 <= age <= 59:
    print("зрелость")
elif age >= 60:
    print("старость")
    
#9
a, b, c = int(input()), int(input()), int(input())

if a >= 0:
    a = a
elif a <= 0:
    a = 0 

if b >= 0:
    b = b
elif b <= 0:
    b = 0 

if c >= 0:
    c = c
elif c <= 0:
    c = 0 

sum = print(a + b + c)














































