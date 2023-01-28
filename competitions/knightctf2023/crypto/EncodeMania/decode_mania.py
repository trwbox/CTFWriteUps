import base64

values = []

def decrypt(s):
    # Array of values to return
    returnVal = []
    # For each item in the passed in array
    for i in range(len(s)):
        # Attempt to base64 decode the item
        try:
            # Add the decoded value to the return array
            returnVal.append(base64.b64decode(s[i]))
        # If it fails, just ignore it
        except:
            pass
        # Attempt to base32 decode the item
        try:    
            # Add the decoded value to the return array
            returnVal.append(base64.b32decode(s[i]))
        # If it fails, just ignore it
        except:
            pass
        # Attempt to base16 decode the item
        try:
            # Add the decoded value to the return array
            returnVal.append(base64.b16decode(s[i]))
        # If it fails, just ignore it
        except:
            pass
        # Attempt to base85 decode the item
        try:
            # Add the decoded value to the return array
            returnVal.append(base64.b85decode(s[i]))
        # If it fails, just ignore it
        except:
            pass
    return returnVal

# read the encoded flag
with open("encode_mania.txt", 'r') as f:
    # Strip it of any whitespace
    encrypted_flag = f.read().strip()
    values = []
    # Add the encoded flag to the values array
    values.append(encrypted_flag)

    # Since the random encoding happened 12 times, we need to decode 12 times
    for i in range(12):
        # Decode the values and save the new values in the same array
        values = decrypt(values)

    # Create a new array to hold the decoded values
    output = []
    for i in range(len(values)):
        # Attempt to decode the value as utf-8
        try:
            # Add the decoded value to the output array
            output.append(values[i].decode('utf-8'))
        # If it fails, just ignore it
        except:
            pass

    # Iterate through the values that come out of the decoding
    for i in range(len(output)):
        # Create a new file for each value
        with open("output/flag" + str(i) + ".txt", 'w') as f:
            # Write the decoded value to the file
            f.write(output[i])
