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
        n1 = '0' * (len(n2) - len(n1)) + n1
    elif len(n1) > len(n2):
        n2 = '0' * (len(n1) - len(n2)) + n2

    remainder = 0
    new_bin = ''
    for i in range(len(n1) - 1, -1, -1):
        if n1[i] == '0' and n2[i] == '0':
            if remainder == 0:
                new_bin = '0' + new_bin
            else:
                new_bin = '1' + new_bin
                remainder = 0
        elif n1[i] == '1' and n2[i] == '1':
            if remainder == 1:
                new_bin = '1' + new_bin
            else:
                new_bin = '0' + new_bin
                remainder = 1
        else:
            new_bin = '1' + new_bin
    if remainder == 1:
        new_bin = '1' + new_bin
    return new_bin


def twos_complement(bin: str) -> str:
    return add_binary(binary_not(bin), '1')


def binary_not(bin: str) -> str:
    new_bin = ''
    for s in bin:
        if s == '1':
            new_bin += '0'
        else:
            new_bin += '1'
    return new_bin


if __name__ == '__main__':
    print(twos_complement('1001'))
