import random
import timeit
import pandas as pd
import matplotlib.pyplot as plt

def generate_data(size, data_type="random"):
    if data_type == "random":
        return [random.randint(1, 10000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reversed":
        return list(range(size, 0, -1))

# Wrapper for Timsort (Python's built-in sorted)
def timsort(arr):
    return sorted(arr)

def measure_timsort_performance(sizes, data_types):
    results = []

    for size in sizes:
        for data_type in data_types:
            data = generate_data(size, data_type)
            
            # Measure Timsort
            time_taken = timeit.timeit(lambda: timsort(data), number=10)
            results.append({
                "Data Size": size,
                "Data Type": data_type,
                "Time Taken (s)": time_taken / 10  # Average over 10 runs
            })

    return results

def save_results_to_csv(results, filename):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

def display_results(results):
    print("| Data Size | Data Type  | Time Taken (s) |")
    print("|-----------|------------|----------------|")
    for result in results:
        print(f"| {result['Data Size']:<9} | {result['Data Type']:<10} | {result['Time Taken (s)']:.6f} |")

def visualize_results(filename):
    df = pd.read_csv(filename)
    
    # Побудова графіків для кожного типу даних
    data_types = df["Data Type"].unique()
    for data_type in data_types:
        data = df[df["Data Type"] == data_type]
        plt.plot(data["Data Size"], data["Time Taken (s)"], marker="o", label=data_type)

    # Налаштування графіка
    plt.title("Timsort: Час виконання залежно від розміру даних")
    plt.xlabel("Розмір даних")
    plt.ylabel("Час виконання (секунди)")
    plt.legend(title="Тип даних")
    plt.grid(True)
    plt.show()

def main():
    sizes = [100, 1000, 5000, 10000, 50000]
    data_types = ["random", "sorted", "reversed"]
    
    results = measure_timsort_performance(sizes, data_types)
    display_results(results)  # Вивід у консоль
    save_results_to_csv(results, "timsort_analysis_results.csv")
    visualize_results("timsort_analysis_results.csv")

if __name__ == "__main__":
    main()
