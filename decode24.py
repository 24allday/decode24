#Decode24
#24Bkdoor
#!/usr/bin/env python
import base64
import binascii
from termcolor import colored

def decode_string(encoded_string, encoding):
    try:
        if encoding == "base64":
            decoded_string = base64.b64decode(encoded_string).decode('utf-8')
        elif encoding == "hex":
            decoded_string = bytes.fromhex(encoded_string).decode('utf-8')
        elif encoding == "url":
            decoded_string = base64.urlsafe_b64decode(encoded_string).decode('utf-8')
        else:
            raise ValueError("Unsupported encoding")
    except (ValueError, binascii.Error) as e:
        return colored(f"Error decoding: {str(e)}", 'red')

    return decoded_string

# Prompt for input
encoded_string = input(colored('Enter an encoded string to decode: ', 'yellow'))
encoding = input(colored('Enter the encoding type (base64, hex, url): ', 'yellow'))

# Decode the string
decoded_string = decode_string(encoded_string, encoding)

# Print the decoded string or error message
if decoded_string:
    print(colored(f"Decoded string: {decoded_string}", 'green'))
else:
    print(decoded_string)
