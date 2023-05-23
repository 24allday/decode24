#Decode24 
#Base64 specific
#24Bkdoor
#!/usr/bin/env python
import base64

def decode_base64_string(encoded_string):
    padding = len(encoded_string) % 4
    if padding != 0:
        encoded_string += "=" * (4 - padding)

    decoded_string = base64.b64decode(encoded_string)
    return decoded_string.decode('utf-8')

# Prompt for input and decode the string
encoded_string = input('Enter a Base64-encoded string to decode: ')
decoded_string = decode_base64_string(encoded_string)
print(decoded_string)
