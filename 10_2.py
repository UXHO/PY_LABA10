def reverse_s(input_str):
    stack = []
    for char in input_str:  # Проход по каждому символу
        stack.append(char)  # Добавляем символ в стек
    reversed_str = ""  # Инициализируем перевернутую строку
    while stack:  # Пока стек не пуст
        reversed_str += stack.pop()  # Извлекаем символ из стека и добавляем к перевернутой строке
    return reversed_str  # Возвращаем перевернутую строку


orig_str = input("Введите строку для инвертирования: ")  # Ввод строки с клавиатуры
res = reverse_s(orig_str)
print("Инвертированная строка:", res)
