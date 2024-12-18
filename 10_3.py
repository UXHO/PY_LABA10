# Чтение данных из файла
file_name = 'input.txt'
file = open(file_name, 'r')
data = file.readlines()
file.close()

# Создание очередей
qus = []
for line in data:
    elements = line.strip().split(', ')
    qu = list(elements)
    qus.append(qu)


# Функция для выполнения обработки очередей
def process_queues(queues):
    result = []
    while any(queues):  # Пока хотя бы одна очередь не пуста
        for queue in queues:
            if queue:  # Если очередь не пуста
                result.append(queue.pop(0))  # Удаляем первый элемент и добавляем его в результат
    return result


# Обработка очередей
res = process_queues(qus)
print(", ".join(res))
