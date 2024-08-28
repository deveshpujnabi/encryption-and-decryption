from cryptography.fernet import Fernet

def generate_key():
  """
  Generates a secret key for encryption and decryption.
  """
  key = Fernet.generate_key()
  # Store the key securely (e.g., a file or keychain)
  print("Generated key:", key.decode())  # Display generated key for user to copy (optional)
  return key

def encrypt_message(message, key):
  """
  Encrypts a message using the provided key.
  """
  fernet = Fernet(key)
  encrypted_message = fernet.encrypt(message.encode())
  return encrypted_message

def decrypt_message(encrypted_message, key):
  """
  Decrypts an encrypted message using the provided key.
  """
  fernet = Fernet(key)
  decrypted_message = fernet.decrypt(encrypted_message).decode()
  return decrypted_message

def main():
  """
  Prompts the user for encryption or decryption and handles the process.
  """
  while True:
    print("\nMenu:")
    print("1. Generate a new key")
    print("2. Encrypt a message")
    print("3. Decrypt a message")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      key = generate_key()

    elif choice == '2':
      message = input("Enter your message to encrypt: ")
      encrypted_message = encrypt_message(message, key)
      print("Encrypted message:", encrypted_message.decode())
    elif choice == '3':
      encrypted_message = input("Enter the encrypted message to decrypt: ")
      try:
        decrypted_message = decrypt_message(encrypted_message.encode(), key)
        print("Decrypted message:", decrypted_message)
      except Fernet.InvalidKey:
        print("Invalid decryption key. Please check your key or the encrypted message.")
    elif choice == '4':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()
