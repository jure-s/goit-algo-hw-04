import timeit
import random
import pandas as pd
import matplotlib.pyplot as plt

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Wrapper for Timsort (Python's built-in sorted)
def timsort(arr):
    return sorted(arr)

# Generate random data for testing
def generate_data(size, data_type="random"):
    if data_type == "random":
        return [random.randint(1, 10000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reversed":
        return list(range(size, 0, -1))

# Test and measure execution time
def measure_time(sort_function, data):
    start_time = timeit.default_timer()
    sort_function(data)
    return timeit.default_timer() - start_time

def save_results_to_csv(results, filename):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

def visualize_comparison(filename):
    df = pd.read_csv(filename)

    # Фільтрування та побудова графіків для кожного алгоритму
    algorithms = df["Algorithm"].unique()
    for algo in algorithms:
        algo_data = df[df["Algorithm"] == algo]
        plt.plot(
            algo_data["Data Size"],
            algo_data["Time Taken (s)"],
            marker="o",
            label=algo
        )

    # Налаштування графіка
    plt.title("Порівняння алгоритмів сортування")
    plt.xlabel("Розмір даних")
    plt.ylabel("Час виконання (секунди)")
    plt.legend(title="Алгоритм")
    plt.grid(True)
    plt.show()

def main():
    sizes = [100, 1000, 5000, 10000]
    data_types = ["random", "sorted", "reversed"]

    results = []

    for size in sizes:
        for data_type in data_types:
            data = generate_data(size, data_type)
            
            print(f"Data Size: {size}, Data Type: {data_type}")
            
            # Measure Merge Sort
            merge_time = measure_time(merge_sort, data.copy())
            results.append({"Algorithm": "Merge Sort", "Data Size": size, "Data Type": data_type, "Time Taken (s)": merge_time})

            # Measure Insertion Sort
            if size <= 1000:  # Limiting size for Insertion Sort due to inefficiency
                insertion_time = measure_time(insertion_sort, data.copy())
                results.append({"Algorithm": "Insertion Sort", "Data Size": size, "Data Type": data_type, "Time Taken (s)": insertion_time})
            else:
                results.append({"Algorithm": "Insertion Sort", "Data Size": size, "Data Type": data_type, "Time Taken (s)": None})

            # Measure Timsort
            timsort_time = measure_time(timsort, data.copy())
            results.append({"Algorithm": "Timsort", "Data Size": size, "Data Type": data_type, "Time Taken (s)": timsort_time})

            print("-")

    save_results_to_csv(results, "compare_sorts_results.csv")
    visualize_comparison("compare_sorts_results.csv")

if __name__ == "__main__":
    main()
