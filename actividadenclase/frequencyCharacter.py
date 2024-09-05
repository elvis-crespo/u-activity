import time
# start time
startTime = time.perf_counter()

str_ = "This website is awesome."
ch = 'e'
frequency = 0

# Iterate 
for char in str_:
    if ch == char:
        frequency += 1

print(f"Frequency of '{ch}' = {frequency}")

# end time
endTime = time.perf_counter()
executionTime = (endTime - startTime) * 1000  # Convert to milliseconds

print("\nExecution Time: {:.4f} ms".format(executionTime)) 