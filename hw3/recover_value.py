import hashlib
import re

def compute_hash(block, nonce, message, prev):
    find = False
    while find == False:
        result = hashlib.sha256()
        string = str(block) + str(nonce) + message + prev
        result = hashlib.sha256(string.encode()).hexdigest()
        if result[:4] == "0000":
            find = True
            return result, nonce
        nonce += 1

def extract_name_money(message):
    message = message.split(" ")
    p1 = message[0]
    p2 = message[2]
    money = message[3]

    return p1, p2, int(money)


if __name__ == "__main__":

    # Get the input
    first_message = input()
    origin_message = input()
    second_nonce = int(input())
    third_message = input()
    third_hash = input()


    # Compute hash for block 1
    prev = "0000000000000000000000000000000000000000000000000000000000000000"
    first_hash, n = compute_hash(1, 0, first_message, prev)
    
    find_cash = False
    cash_2 = 0
    while find_cash == False:

        # Compute hash for block 2
        second_message = origin_message.replace("_", str(cash_2))
        second_hash, n = compute_hash(2, second_nonce, second_message, first_hash)

        # Compute hash for block 3
        last_hash, n = compute_hash(3, 0, third_message, second_hash)

        if last_hash == third_hash:
            find_cash = True
            break
        
        cash_2 += 1


    # Store Alice's cash
    alice = 0

    # Process first message
    first_message = first_message.split("&")
    for message in first_message:
        p1, p2, money = extract_name_money(message)
        if p2 == 'Alice':
            alice += money

    # Process second message
    p1, p2, money = extract_name_money(second_message)
    if p1 == 'Alice':
        alice -= money
    elif p2 == 'Alice':
        alice += money

    # Process third message
    p1, p2, money = extract_name_money(third_message)
    if p1 == 'Alice':
        alice -= money
    elif p2 == 'Alice':
        alice += money



    print(cash_2, end=",")
    print(alice, end=",")
    print(n)

