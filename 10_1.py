slovo = input("Введите слово: ")
if len(slovo) < 3:
    print("Ошибка:слово должно содержать минимум 3 буквы.")
    exit()
chars = list(slovo)  # Создаем список из слова
length = len(chars)
stak = []  # Список который будем использоваться как стек
seredina = length // 2  # Индекс середины
for i in range(seredina):
    stak.append(chars[i])  # Добавление в стек первой половины

start_index = seredina + (length % 2)  # Определяет с какого индекса начинать сравн второй половины стека
for i in range(start_index, length):  # Извлекает символы из стека и сравн с соотв символы из второй половины слова
    if stak.pop() != chars[i]:
        print("Слово не является палиндромом")
        exit()
print("Слово является палиндромом")
