def dec_to_bin(x):
    return bin(x)[2:]

def encryption(a, e, n):
    e = dec_to_bin(e)
    x = 1
    l = len(e)
    power = a
    for i in range(l):
        if int(e[l-i-1]):
            x = x * power % n
        power = power * power % n

    return x


if __name__ == "__main__":

    n, e, string = input().split()

    n = int(n)
    e = int(e)

    message = []

    for ch in string:
        ch = ord(ch)
        message.append(str(encryption(ch, e, n)))

    print(','.join(message))
