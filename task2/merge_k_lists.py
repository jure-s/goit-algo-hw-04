import heapq

def merge_k_lists(lists):
    """
    Об'єднує k відсортованих списків у один відсортований список.

    :param lists: Список відсортованих списків.
    :return: Один відсортований список.
    """
    min_heap = []
    
    # Додаємо перші елементи кожного списку у мін-кучу
    for i, lst in enumerate(lists):
        if lst:  # Перевіряємо, чи список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента в списку)
    
    result = []
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Якщо залишились елементи в тому ж списку, додаємо наступний елемент до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
    
    return result

# Приклад використання
if __name__ == "__main__":
    while True:
        try:
            print("Введіть кількість списків (одне число):")
            k = int(input().strip())
            if k <= 0:
                raise ValueError("Кількість списків має бути додатнім числом.")
            break
        except ValueError:
            print("Помилка: введіть одне ціле число, яке більше нуля. Спробуйте ще раз.")

    lists = []

    for i in range(k):
        while True:
            try:
                print(f"Введіть елементи списку {i + 1}, розділені пробілом:")
                lst = list(map(int, input().strip().split()))
                lists.append(lst)
                break
            except ValueError:
                print("Помилка: введіть коректні цілі числа, розділені пробілами. Спробуйте ще раз.")

    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)