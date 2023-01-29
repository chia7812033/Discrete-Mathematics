import hashlib


def hash(block, data, prev):
    find = False
    nonce = 0
    while find == False:
        result = hashlib.sha256()
        string = str(block) + str(nonce) + data + prev
        result = hashlib.sha256(string.encode()).hexdigest()
        if result[:3] == "000":
            find = True
        nonce += 1
    return result


if __name__ == "__main__":
    contents = []
    while True:
        try:
            a = input()
            contents.append(a)
        except:
            break
    prev = "0000000000000000000000000000000000000000000000000000000000000000"
    for i in range(len(contents)):
        prev = hash(i+1, contents[i], prev)
    print(prev)
