def encode_password(password):
    encoded_password = ""
    for num in password:
        new_num = str((int(num) + 3) % 10)
        encoded_password += new_num
    return encoded_password

# decode password function
def decode_password(password):
    decoded_string = ""
    for num in password:
        decoded_num = str((int(num) - 3) % 10)
        decoded_string += decoded_num
    return decoded_string


if __name__ == "__main__":
    Continue = True
    original_password = ""
    while Continue is True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("\nPlease enter an option: "))
        password_encoded = encode_password(original_password)  # moved into while loop to update value
        if option == 1:
            original_password = str(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif option == 2:
            print("The encoded password is ", encode_password(original_password), ", and the original password is ", decode_password(password_encoded), sep="", end=".\n")
        elif option == 3:
            break
