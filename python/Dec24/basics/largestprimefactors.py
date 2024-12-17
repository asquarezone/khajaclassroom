number = 13195
start = number - 1
while start > 1:
    # check if the start is factor
    if number % start == 0:
        # now we need to check if the start is prime or not
        is_prime = True
        index = 2
        while index < start:
            if start%index == 0:
                is_prime = False
                break
            index += 1
        if is_prime:
            print(start)
            break
    start -= 1
