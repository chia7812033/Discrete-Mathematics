import random
from math import gcd

def modular(a, e, n):
    x = 1
    while e:
        if e & 1:
            x = x * a % n
        a = a * a % n
        e = e >> 1
    return x


def pollard_rho(n):

    x = (random.randint(0, 2) % (n - 2))
    y = x
    c = (random.randint(0, 1) % (n - 1))
    d = 1

    while d == 1:

        x = (modular(x, 2, n) + c + n) % n

        y = (modular(y, 2, n) + c + n) % n
        y = (modular(y, 2, n) + c + n) % n

        d = gcd(abs(x - y), n)

        if d == n:
            return pollard_rho(n)

    return d, n // d


def ext_gcd(a, b):
    if a == 0:
        return b, 0, 1

    q, x, y = ext_gcd(b % a, a)
    return q, y - (b // a) * x, x


def decryption(e, n):
    p, q = pollard_rho(n)
    fi_n = (p-1) * (q-1)
    g, x, y = ext_gcd(e, fi_n)

    return x % fi_n


if __name__ == "__main__":

    n, e, string = input().split()

    n = int(n)
    e = int(e)

    string = string.split(',')
    string = list(map(int, string))

    x = decryption(e, n)

    for i in range(len(string)):
        string[i] = modular(string[i], x, n)
        string[i] = chr(string[i])

    print(''.join(string))
