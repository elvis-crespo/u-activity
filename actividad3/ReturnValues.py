def name():
    return "John","Armin"

#------------------Example 1: Return values using comma
import time

# start time
startTime = time.perf_counter()
# print the tuple with the returned values
print(name())

# get the individual items
name_1, name_2 = name()
print(name_1, name_2)

# end time
endTime = time.perf_counter()
executionTime = (endTime - startTime) * 1000  # Convert to milliseconds

print("Execution Time: {:.2f} ms".format(executionTime))






##----------------EXAMPLE WITH DICTIONARY

def name2():
    n1 = "John"
    n2 = "Armin"

    return {1:n1, 2:n2}

# start time
startTime = time.perf_counter()

names = name2()
print("\n", names)

# end time
endTime = time.perf_counter()
executionTime = (endTime - startTime) * 1000  # Convert to milliseconds

print("Execution Time: {:.2f} ms".format(executionTime))