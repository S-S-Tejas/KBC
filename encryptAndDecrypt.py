import random
def encryption(text):
    words = text.split()
    enc_list = []
    for word in words:
        if len(word) <= 3:
            a = str(word[::-1])
            enc_list.append(a)
        elif len(word) > 3:
            a = str(word)
            b = a[1:] + a[0]
            randAN = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            for i in range(2):
                c = random.choice(randAN)
                b = b + c
            for j in range(2):
                d = random.choice(randAN)
                b = d + b 
            enc_list.append(b)
    for word in enc_list:
        print(word, end=" ")

def decryption(text):
    words = text.split()
    dec_list = []
    for word in words:
        if len(word) <= 3:
            a = str(word[::-1])
            dec_list.append(a)
        elif len(word) > 3:
            a = str(word)
            b = a[2:-2]
            c = b[-1] + b[:-1]
            dec_list.append(c)
    for word in dec_list:
        print(word, end=" ")

if __name__ == "__main__":
    print(f"{'-'*25}Secret Code{'-'*25}")
    print('''1. Encryption
2. Decryption''')
    try:
        choice = int(input("Enter 1 or 2: "))
        if choice == 1:
            text = input("Enter a sentence: ")
            encryption(text)
        elif choice == 2:
            text = input("Enter the encrypted sentence: ")
            decryption(text)
        else:
            print("Invalid choice!\nExiting...")
    except Exception as e:
        print("Error: ",e)
        print("Enter a valid choice")
        print("Thank you!")