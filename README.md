
# Encryption and Decryption Tool

This is a simple Python-based command-line tool for generating encryption keys, encrypting messages, and decrypting them using the `cryptography` library's `Fernet` module.

## Features

- **Generate Key**: Create a secure encryption key.
- **Encrypt Message**: Securely encrypt any text message.
- **Decrypt Message**: Decrypt an encrypted message back to its original form using the corresponding key.

## Prerequisites

- **Python 3.x** must be installed on your system.
- **cryptography** library is required. Install it using pip:

```bash
pip install cryptography
```

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/encryption-decryption-tool.git
   cd encryption-decryption-tool
   ```

2. **Run the Program:**

   ```bash
   python encryption_decryption.py
   ```

3. **Menu Options:**

   - **1. Generate a new key:** Generates a new encryption key and displays it.
   - **2. Encrypt a message:** Prompts for a message and encrypts it using the provided key.
   - **3. Decrypt a message:** Prompts for an encrypted message and decrypts it using the provided key.
   - **4. Exit:** Exits the program.

## Example

```shell
Menu:
1. Generate a new key
2. Encrypt a message
3. Decrypt a message
4. Exit

Enter your choice (1-4): 1
Generated key: AbCdeFgHiJkLmNoPqRsTuVwXyZ1234567890=
```


## Important Notes

- **Security:** The encryption key is displayed in plain text for demonstration purposes. In real-world applications, ensure that keys are securely stored.
- **Key Management:** Losing the encryption key means that you will not be able to decrypt the encrypted messages.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- This tool uses the [cryptography](https://cryptography.io/en/latest/) library for secure encryption and decryption.
