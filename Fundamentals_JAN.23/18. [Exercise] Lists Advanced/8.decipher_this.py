cryptogram = input().split()

for word in cryptogram:
    crypto_word = [char for char in word if not char.isnumeric()]
    crypto_digit = int("".join([digit for digit in word if digit.isnumeric()]))

    crypto_word[0], crypto_word[-1] = crypto_word[-1], crypto_word[0]

    decrypted_word = chr(crypto_digit) + "".join(crypto_word)
    print(decrypted_word, end=" ")
