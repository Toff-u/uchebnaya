num = list(range(10))
ch = int(input("Введите число для вывода таблицы умножения: "))
print(f"Таблица умножения для {ch}:")
for n in num:
    result = ch * n
    print(f"{ch} * {n} = {result}")