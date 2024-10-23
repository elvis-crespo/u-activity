import time

def desc(cantGastada, porcentajeCupon):
    return (porcentajeCupon / 100) * cantGastada


'''Main'''
startTime = time.time()

cantGastada = float(input("Please enter the cost of your groceries: "))

porcentajeCupon = 0.0

if cantGastada > 9 and cantGastada < 60:
    porcentajeCupon = 8.0
elif cantGastada > 59 and cantGastada < 150:
    porcentajeCupon = 10.0
elif cantGastada > 149 and cantGastada < 210:
    porcentajeCupon = 12.0
elif cantGastada > 209:
    porcentajeCupon = 14.0

valueDesc = desc(cantGastada, porcentajeCupon)

valueDescFormatted = f"{valueDesc:.2f}"

print(f"You win a discount coupon of: $ {valueDescFormatted} ({porcentajeCupon}% of your purchase.)")

endTime = time.time()
executionTime = (endTime - startTime) * 1000 
print(f"\nTiempo de ejecución: {executionTime:.2f} ms")

