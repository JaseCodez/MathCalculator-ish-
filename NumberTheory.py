def phi_function(p: int) -> int:
    if is_prime(p):
        return p - 1
    divided = []
    phi = p
    while p != 1:
        i = 2
        while p % i != 0:
            i += 1

        p = p // i
        if i not in divided:
            divided.append(i)

    for num in divided:
        phi -= phi // num
    return phi


def is_prime(p: int) -> bool:
    if p == 1:
        return False
    elif p == 2:
        return True
    for i in range(2, p-1):
        if p % i == 0:
            return False
    return True


print(phi_function(9900))
