import time
import runpy

start_time = time.time()
runpy.run_path("Question1.py")
end_time = time.time()

elapsed_time = end_time - start_time

print(f"{'='*40}")
print(f"{'Execution Time':^40}")
print(f"{'-'*40}")
print(f"The time taken to execute the file is: {elapsed_time:.2f} seconds")
print(f"{'='*40}")
