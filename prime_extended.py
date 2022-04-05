def prime_extend(low, up):
    """
    :param low: Lower limit
    :param up: Upper Limit
    :return: The numbers within range Which are both palindrome and prime
    """
    arr_output = []
    for iterate in range(low, up+1):
        check = True
        if str(iterate) == str(iterate)[::-1]:
            if iterate > 2:
                for a in range(2, iterate):
                    if iterate % a == 0:
                        check = False
                        break
                if check:
                    arr_output.append(iterate)
    return arr_output


if __name__ == "__main__":
    l_limit = int(input("Enter the lower limit: "))
    u_limit = int(input("Enter the upper limit: "))
    print(prime_extend(l_limit, u_limit))
