import tracemalloc
import sys


tracemalloc.start()

value = [x**2 for x in range(10000000)]


current_1, peak_1 = tracemalloc.get_traced_memory()
tracemalloc.stop()



tracemalloc.start()

value = (x**2 for x in range(10000000))

current_2, peak_2 = tracemalloc.get_traced_memory()
tracemalloc.stop()


ram_list_mb = peak_1 / (1024 * 1024)
ram_gen_mb = peak_2 / (1024 * 1024)

ram_difference = ram_list_mb - ram_gen_mb

print("--- MEMORY UTILIZATION RESULTS ---")
print(f"Method 1 (List Comprehension) Peak RAM: {ram_list_mb:.2f} MB")
print(f"Method 2 (Generator Expression) Peak RAM: {ram_gen_mb:.2f} MB")
print("-" * 34)
print(f"The Generator saved you: {ram_difference:.2f} MB of RAM!")



