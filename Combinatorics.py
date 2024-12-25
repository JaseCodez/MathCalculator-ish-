def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def C(n: int, r: int) -> int:
    """
    Pre-condition: n >= r

    return nCr
    """
    n_fact = factorial(n)
    r_fact = factorial(r)
    nr_fact = factorial(n - r)
    return n_fact // (r_fact * nr_fact)


def balls_in_bins(balls: int, bins: int) -> int:
    return C(balls + bins - 1, balls)


def P(n: int, k: int) -> int:
    """
    Assume k <= n
    """
    n_fact = factorial(n)
    kn_fact = factorial(n - k)
    return n_fact // kn_fact


def number_of_string_arrangements(s: str) -> int:
    n = factorial(len(s))
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    for _, val in d.items():
        n //= factorial(val)
    return n


def powerset(lst):
    if not lst:
        return [[]]
    else:
        x = []
        for i in range(len(lst)):
            temp = lst[:]
            if temp not in x:
                x.append(temp[:])
            temp.pop(i)
            x.extend(powerset(temp))

        if [] in x:
            x.remove([])

        return x


if __name__ == '__main__':
    print(powerset([1, 2, 3]))
