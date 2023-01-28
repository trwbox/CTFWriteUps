import sys
import random


def main():
    byte_data = []
    file_name = "vaulter-output-test.enc"
    # Select a random number to XOR with
    num = random.randint(1, 1024)

    with open(file_name, "rb") as f:
        # Read in the file as a byte object
        byte_data = f.read()        
        # Take the bytes and convert them to a hex string
        bdh = byte_data.hex()
        # A holding value for the output
        out = []
        # A pair of temporary lists so I can debug
        temp = []
        tempXOR = []


        for each in list(bdh):
            # Take the ord of the character and put it in temp to debug
            temp.append(ord(each))
            # For each character in the hex string, convert to an integer
            # and XOR it with the random number, this will give us the
            # new integer value
            out.append(ord(each) ^ num)

        for i in temp:
            # Do the XOR with a constant I control and put it in tempXOR to debug
            tempXOR.append(i ^ 1)

        # Turn the new integer values into characters
        concat = "".join(chr(i) for i in out)

        # Write the output to a file
        with open("output.enc", "w") as f:
            f.write(concat)



if __name__ == "__main__":
    main()