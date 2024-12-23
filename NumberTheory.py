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


def euclidean_algorithm(a: int, b: int) -> dict[int, tuple[int, int, int]]:
    """
    Assume a > b

    https://tjyusun.com/mat202/sec-integers-divisibility
    Theorem 1.3.2. Division Algorithm.

    Let a, b be Naturals. Then there exist a unique q and r
    that satisfy all of the following:

                    a = qb + r,    q >= 0, 0 <= r < b

    :return key as dividend a with values q as quotient, b
    as divisor and remainder r.
    {a: (q, b, r)}
    """
    if a % b == 1:
        return {a: ((a - 1) // b, b, 1)}

    d = {a: ((a - a % b) // b, b, a % b)}
    d.update(euclidean_algorithm(d[a][1], d[a][2]))
    return d


def inverse_modulo(x: int, y: int) -> dict[int, int]:
    pass


if __name__ == '__main__':
    print(euclidean_algorithm(101, 44))
