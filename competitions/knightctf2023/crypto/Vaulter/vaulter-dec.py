hexChars = "0123456789abcdef"
file_name = "vaulter-output.enc"
# Set this to True if you want to see the hex output of everything put to file
PRINT_BYTES = False

with open(file_name, "rb") as f:
    # Read the bytes from the file as a byte object
    byte_data = f.read()
    # Decode the bytes to a string of utf-8 characters
    string_data = byte_data.decode("utf-8")

    int_data = []
    # Convert the utf-8 character string to a list of integers
    # representing the ordinal value of each character
    for i in string_data:
        int_data.append(ord(i))
    
    out = []
    # Iterate over all the possible XOR values
    for xor in range(1, 1025):
        # Iterate over the list of integers
        for j in int_data:
            # XOR the integer with the current XOR value
            xored = j ^ xor
            # We are looking for a hex string, so if the XORed value
            # is not a valid hex character, we can break out of the loop
            if chr(xored) not in hexChars:
                out = []
                break
            # If the XORed value is a valid hex character, append it to the output
            else:
                out.append(chr(xored))
        
        # If the output is not empty, we have found a valid hex string
        if len(out) > 0:
            # Print the XOR value
            print(f'Valid hex string at {xor} iterations')
            # Join the list of hex characters into a string
            hex_string = "".join(out)
            # Convert the hex string to bytes
            bytes_hex = bytes.fromhex(hex_string)

            # Print the bytes if you want to see the output
            if PRINT_BYTES:
                print(bytes_hex)
            # Write the bytes to a file
            with open(f"output/output{xor}.dec", "wb") as binary_file:
                binary_file.write(bytes_hex)
        
        # Clear the output list
        out = []

