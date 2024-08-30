"""This program demonstrates the solution of 
project euler problem 3

concepts:
  while
  if
  variables
"""

number = int(input("Enter the number: "))
index = number // 2
while index >= 2:
    print(index)
    if number % index == 0:
        # we need to check if index i prime or not
        print("found factor")
        counter = 2
        is_prime = True
        while counter <= index // 2:
            if index % counter == 0:
                is_prime = False
                break
            counter += 1
        if is_prime:
            print("Largest Prime factor is ")
            print(index)
            break
    index -= 1
