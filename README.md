# Encryption and Decryption Tool

This is a simple Python-based command-line tool for generating encryption keys, encrypting messages, and decrypting them using the `cryptography` library's `Fernet` module.

## Features

- **Generate Key**: Create a secure encryption key.
- **Encrypt Message**: Securely encrypt any text message.
- **Decrypt Message**: Decrypt an encrypted message back to its original form using the corresponding key.

## Prerequisites

- **Python 3.x** must be installed on your system.
- Install the required libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/deveshpujnabi/encryption-and-decryption.git
   cd encryption-decryption-tool
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Program:**

   ```bash
   python encryption_decryption.py
   ```

4. **Menu Options:**

   - **1. Generate a new key:** Generates a new encryption key and displays it.
   - **2. Encrypt a message:** Prompts for a message and encrypts it using the provided key.
   - **3. Decrypt a message:** Prompts for an encrypted message and decrypts it using the provided key.
  

   - **4. Exit:** Exits the program.

## Folder Structure

Your project should be organized as follows:

```
encryption-decryption-tool/
│
├── encryption_decryption.py   # Your main Python script
├── README.md                  # The README file for your project
├── requirements.txt           # Dependencies for the project
└── LICENSE                    # License file (optional)
```

- **`encryption_decryption.py`**: Your main Python script containing the encryption and decryption code.
- **`README.md`**: Provides an overview of the project and instructions for use.
- **`requirements.txt`**: Lists the Python packages required for the project.
- **`LICENSE`**: (Optional) A file specifying the license under which your project is distributed.

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

## Code Explanation

- **generate_key():** Generates a new Fernet key for encryption and decryption.
- **encrypt_message(message, key):** Encrypts a given message using the provided key.
- **decrypt_message(encrypted_message, key):** Decrypts an encrypted message using the corresponding key.
- **main():** Handles the user interaction and menu options.

## Important Notes

- **Security:** The encryption key is displayed in plain text for demonstration purposes. In real-world applications, ensure that keys are securely stored.
- **Key Management:** Losing the encryption key means that you will not be able to decrypt the encrypted messages.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- This tool uses the [cryptography](https://cryptography.io/en/latest/) library for secure encryption and decryption.

---

This `README.md` provides clear guidance on the project’s structure, dependencies, and usage, ensuring that anyone can set it up and run it easily.
