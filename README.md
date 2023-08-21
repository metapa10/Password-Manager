# Password Manager

The Simple Password Manager is a Python project that allows users to store and manage their passwords securely. The application uses the `cryptography` library for encryption and decryption of passwords, ensuring the safety of sensitive information.

## Features

- Add and update passwords for various websites.
- Retrieve passwords for websites when needed.
- Encryption of passwords for secure storage.
- Command-line interface for easy interaction.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x is installed on your system.
- The `cryptography` library is installed. You can install it using `pip`:

  ```
  pip install cryptography
  ```

## Getting Started

1. Clone the repository or download the project files.

2. Open a terminal/command prompt and navigate to the project directory.

3. Run the `password_manager.py` script:

   ```
   python password_manager.py
   ```

## Usage

Upon running the script, you will be presented with a simple command-line interface. You can perform the following actions:

1. **Add/Update Password**: Store or update passwords for websites.
2. **Get Password**: Retrieve passwords for websites.
3. **Exit**: Terminate the application.

Follow the prompts to interact with the password manager.

## Security

The Simple Password Manager uses the `cryptography` library to encrypt and decrypt passwords. The encryption key is generated and stored locally for security purposes.

Please be cautious when handling your encryption key (`key.key`). Losing this file will result in the inability to access your passwords.

## Acknowledgments

- This project was motivated by the need for a simple and secure way to manage passwords.
- The `cryptography` library was instrumental in ensuring password security.

