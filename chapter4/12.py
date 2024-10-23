def kb_to_bb(kb):
    return kb * 1024

def b_to_kb(b):
    return b / 1024

choice = input("Выберите перевод: 1 - из килобайтов в байты, 2 - из байтов в килобайты: ")

if choice == '1':
    kb = float(input("Введите количество килобайтов: "))
    b = kb_to_bb(kb)
    print(f"{kb} килобайт(а) = {b} байт(а)")

elif choice == '2':
    b = float(input("Введите количество байтов: "))
    kb = b_to_kb(b)
    print(f"{b} байт(а) = {kb} килобайт(а)")

else:
    print("Неверный выбор. Пожалуйста, выберите 1 или 2.")