# Vai receber as informações do utilizador
num = int(input("Introduza um numero"))

# Conferir se os números primos são maiores que 1

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")
