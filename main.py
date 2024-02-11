def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(m, n):
    return m // gcd(m, n) * n


x = int(input('Количество чисел: '))
numbers = []
for i in range(x):
    numbers.append(int(input(f'{i+1} число: ')))
nok = lcm(numbers[0], numbers[1])
for i in range(2, x):
    nok = lcm(nok, numbers[i])
print(f"Наименьшее общее кратное этих чисел: {nok}")
