from cryptography.fernet import Fernet
import json
import os

class PasswordManager:
    def __init__(self, key_filename="key.key", data_filename="passwords.json"):
        self.key_filename = key_filename
        self.data_filename = data_filename
        self.load_key()
        self.load_data()

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_filename, "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        if not os.path.exists(self.key_filename):
            self.generate_key()
        with open(self.key_filename, "rb") as key_file:
            self.key = key_file.read()

    def encrypt(self, data):
        cipher_suite = Fernet(self.key)
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data

    def decrypt(self, encrypted_data):
        cipher_suite = Fernet(self.key)
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
        return decrypted_data

    def load_data(self):
        if os.path.exists(self.data_filename):
            with open(self.data_filename, "r") as data_file:
                encrypted_data = data_file.read()
                self.data = json.loads(self.decrypt(encrypted_data))
        else:
            self.data = {}

    def save_data(self):
        encrypted_data = self.encrypt(json.dumps(self.data))
        with open(self.data_filename, "w") as data_file:
            data_file.write(encrypted_data)

    def add_password(self, website, username, password):
        if website in self.data:
            print("Password for this website already exists. Updating...")
        self.data[website] = {"username": username, "password": password}
        self.save_data()
        print("Password added/updated successfully!")

    def get_password(self, website):
        if website in self.data:
            return self.data[website]["password"]
        else:
            return None

def main():
    manager = PasswordManager()

    while True:
        print("\nOptions:")
        print("1. Add/Update password")
        print("2. Get password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter the website: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            manager.add_password(website, username, password)

        elif choice == "2":
            website = input("Enter the website: ")
            password = manager.get_password(website)
            if password:
                print(f"Password for {website}: {password}")
            else:
                print("Password not found.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
