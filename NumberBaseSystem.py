def dec_to_binary(n: int) -> str:
    """Does this count as number theory? I have no clue"""
    if n < 2:
        return str(n)
    return dec_to_binary(n // 2) + str(n % 2)


def binary_to_dec(s: str) -> int:
    n = 0
    s = s.replace(' ', '')

    if not is_valid_binary(s):
        return -1

    for i in range(len(s) - 1, -1, -1):
        if s[i] == "1":
            n += 2**(len(s) - i - 1)
    return n


def is_valid_binary(s: str) -> bool:
    for char in s:
        if char != '0' and char != '1':
            return False
    return True


def add_binary(n1: str, n2: str) -> str:
    if len(n1) < len(n2):
        n1 += '0' * (len(n2) - len(n1))
    elif len(n2) > len(n1):
        n2 += '0' * (len(n1) - len(n2))
