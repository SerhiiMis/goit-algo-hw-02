from collections import deque

def is_palindrome(input_string):
    # Перетворюємо рядок у нижній регістр та видаляємо пробіли
    input_string = input_string.lower().replace(" ", "")
    # Створюємо двосторонню чергу
    char_queue = deque(input_string)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True

# Приклад використання функції
input_str = "A man a plan a canal Panama"
print(is_palindrome(input_str)) 