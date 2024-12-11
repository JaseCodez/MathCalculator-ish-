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


def gcd(p: int, q: int) -> int:
    n = 1
    i = 2
    while i <= p and i <= q:
        if p % i == 0 and q % i == 0:
            n = i
        i += 1
    return n


def convert_from_dec_to_binary(n: int) -> str:
    """Does this count as number theory? I have no clue"""
    if n < 2:
        return str(n)
    return convert_from_dec_to_binary(n // 2) + str(n % 2)


def convert_from_binary_to_dec(s: str) -> int:
    n = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "1":
            n += 2**(len(s) - i - 1)
    return n


if __name__ == '__main__':
    print(convert_from_binary_to_dec(convert_from_dec_to_binary(120)))
