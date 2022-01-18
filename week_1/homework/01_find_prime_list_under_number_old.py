input = 20


def find_prime_list_under_number(number):
    prime = []
    for i in range(2, number):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)

    return prime


result = find_prime_list_under_number(input)
print(result)