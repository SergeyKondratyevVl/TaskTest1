
def my_str(N):

    alphabet = {}

    max_key = N[0]
    max_value = 1

    for i in N:

        if i not in alphabet.keys():
            alphabet[i] = 1
        else:
            alphabet[i] += 1
            max_key, max_value = (i, alphabet[i]) if alphabet[i] > max_value else (max_key, max_value)

    return (max_key, max_value)

if __name__ == "__main__":
    N = str(input('Enter the string: '))
    print(my_str(N.lower()))
