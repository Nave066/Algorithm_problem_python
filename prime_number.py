# Python program to display all the prime numbers within an interval

def prime(start, end):
    """
    :param start: Starting limit
    :param end: End limit
    :return: The no of prime numbers between that range
    """
    result_arr = []
    for num in range(start, end):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            result_arr.append(num)
    return result_arr


if __name__ == "__main__":
    l_limit = int(input("Enter the lower limit: "))
    u_limit = int(input("Enter the upper limit: "))
    print(prime(l_limit, u_limit))
