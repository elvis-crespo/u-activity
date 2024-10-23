# Python program to shuffle a deck of cards

# importing modules
import itertools, random, time

# start time
startTime = time.perf_counter()

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])

# end time
endTime = time.perf_counter()
executionTime = (endTime - startTime) * 1000  # Convert to milliseconds

print("\nExecution Time: {:.2f} ms".format(executionTime))
