num = int(input("Enter any number: "))

if num <= 1:
    print("its not prime number..")
else:
    is_prime = True

    # Check every number from 2 up to num - 1
    for i in range(2, num):
        if num % i == 0:  # Found a divisor in between!
            is_prime = False
            break  # Stop checking immediately

    if is_prime:
        print("it a prime number")
    else:
        print("its not prime number..")