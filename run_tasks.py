import os
import subprocess

def run_timsort_analysis():
    print("Запуск аналізу алгоритму Timsort (завдання 1)...")
    script_path = os.path.join("task1", "scripts", "timsort_analysis.py")
    if os.path.exists(script_path):
        subprocess.run(["python", script_path], check=True)
    else:
        print(f"Скрипт {script_path} не знайдено.")

def run_compare_sorts():
    print("Запуск порівняння алгоритмів сортування (завдання 1)...")
    script_path = os.path.join("task1", "scripts", "compare_sorts.py")
    if os.path.exists(script_path):
        subprocess.run(["python", script_path], check=True)
    else:
        print(f"Скрипт {script_path} не знайдено.")

def run_merge_k_lists():
    print("Запуск злиття k відсортованих списків (завдання 2)...")
    script_path = os.path.join("task2", "merge_k_lists.py")
    if os.path.exists(script_path):
        subprocess.run(["python", script_path], check=True)
    else:
        print(f"Скрипт {script_path} не знайдено.")

def main():
    while True:
        print("\nВиберіть завдання для запуску:")
        print("1 - Аналіз алгоритму Timsort (завдання 1)")
        print("2 - Порівняння алгоритмів сортування (завдання 1)")
        print("3 - Злиття k відсортованих списків (завдання 2)")
        print("0 - Вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            run_timsort_analysis()
        elif choice == "2":
            run_compare_sorts()
        elif choice == "3":
            run_merge_k_lists()
        elif choice == "0":
            print("Вихід із програми.")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()