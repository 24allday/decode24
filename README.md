# decode24.py

decode24 is a command-line tool written in Python that allows you to decode encoded strings using different encoding types such as base64, hex, and URL encoding. It provides a simple and convenient way to decode strings and supports error handling for invalid encodings.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/24bkdoor/decode24.git
   ```

2. Navigate to the `decode24` directory:
   ```
   cd decode24
   ```

3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

4. Make the script executable:
   ```
   chmod +x decode24.py
   ```

## Usage

To use decode24, follow these steps:

1. Run the script:
   ```
   ./decode24.py
   ```

2. Enter the encoded string you want to decode when prompted. For example:
   ```
   Enter an encoded string to decode: {STRING}
   ```

3. Enter the encoding type (base64, hex, url) when prompted. For example:
   ```
   Enter the encoding type (base64, hex, url): base64
   ```

4. The decoded string or an error message will be displayed based on the provided input.

## Examples

Here are some examples to help you get started:

- Decoding a base64-encoded string:
  ```
  Enter an encoded string to decode: {STRING}
  Enter the encoding type (base64, hex, url): base64
  ```

- Decoding a hex-encoded string:
  ```
  Enter an encoded string to decode: {STRING}
  Enter the encoding type (base64, hex, url): hex
  ```

- Decoding a URL-encoded string:
  ```
  Enter an encoded string to decode: {STRING}
  Enter the encoding type (base64, hex, url): url
  ```

## Contributing

Contributions are welcome!

