def main():
    # Temp variable for the flag
    flag = ""

    # Read the encrypted flag
    with open("flag.enc.txt", "r") as infile:
        # Read the flag in from the file
        flag_enc = infile.read()

        # Iterate through the flag and xor it with constant from encrypt of 0x66
        for each in flag_enc:
            each = chr(ord(each) ^ 0x66)
            # Append the character to the flag
            flag += each

    # Print the flag
    print(flag)

if __name__ == "__main__":
    main()