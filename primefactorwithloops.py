number = 29
for factor  in range(number-1,1,-1):
    if number % factor == 0:
        is_prime = True
        for index in range(2, factor):
            if factor % index == 0:
                is_prime = False
                break
        if is_prime:
            print(factor)
            break