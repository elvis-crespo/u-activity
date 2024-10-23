import time

''' Main '''
startTime = time.time()

nums = input("Ingrese cuatro números enteros separados por espacio: ").split()

num1, num2, num3, num4 = map(int, nums)

if (num1 == num2 and num3 == num4) or (num1 == num3 and num2 == num4) or (num1 == num4 and num2 == num3):
    print("dos pares")
else:
    print("no dos pares")

endTime = time.time()
executionTime = (endTime - startTime) * 1000 

print(f"\nTiempo de ejecución: {executionTime:.2f} ms")
