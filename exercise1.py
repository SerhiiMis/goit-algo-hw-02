import queue
import time
import random


# Створення черги заявок
queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    while True:
        # Створення нової заявки
        new_request = random.randint(1, 1000)
        # Додавання заявки до черги
        queue.put(new_request)
        print(f"Створено нову заявку: {new_request}")
        # Затримка перед наступною генерацією заявки
        time.sleep(random.uniform(0.5, 2))

# Функція для обробки заявок
def process_request():
    while True:
        if not queue.empty():
            # Видалення заявки з черги
            request = queue.get()
            print(f"Заявка {request} обробляється")
            # Імітація обробки заявки
            time.sleep(random.uniform(1, 3))
        else:
            print("Черга порожня")
        # Затримка перед перевіркою черги на наявність заявок
        time.sleep(1)

# Головний цикл програми
while True:
    # Виконання функції generate_request() для створення нових заявок
    generate_request()
    # Виконання функції process_request() для обробки заявок
    process_request()