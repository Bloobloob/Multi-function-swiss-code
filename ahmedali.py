import os
import time
import random
import string
import hashlib
import json
import socket
import platform
import uuid
from datetime import datetime

def main_menu():
    available_functions = {
        '1': ("Calculator", calculator),
        '2': ("Unit Converter", unit_converter),
        '3': ("Password Generator", password_generator),
        '4': ("To-Do List", to_do_list),
        '5': ("Detailed System Info", detailed_system_info),
        '6': ("File Hasher", advanced_file_hasher),
        '7': ("JSON Data Handler", json_data_handler),
        '8': ("Prime Number Finder", prime_finder),
        '9': ("Basic Network Scanner", network_scanner),
        '10': ("System Uptime Checker", uptime_checker)
    }

    while True:
        print("\nWelcome to the Swiss-Code")
        print("Select a function:")
        for key, (name, _) in available_functions.items():
            print(f"{key}. {name}")
        print("Type 'exit' to quit.")

        choice = input("Enter your choice: ").strip()
        
        if choice.lower() == 'exit':
            print("Goodbye!")
            break
        elif choice in available_functions:
            print(f"\nRunning {available_functions[choice][0]}...\n")
            available_functions[choice][1]()
        else:
            print("Invalid choice. Please select a valid option.")

def calculator():
    expression = input("Enter expression (e.g., 5 * 4 + 6): ")
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

def unit_converter():
    print("1. Kilometers to Miles\n2. Celsius to Fahrenheit\n3. Kilograms to Pounds")
    choice = input("Choose conversion type: ")
    try:
        value = float(input("Enter value: "))
        conversions = {"1": value * 0.621371, "2": (value * 9/5) + 32, "3": value * 2.20462}
        print(f"Converted value: {conversions.get(choice, 'Invalid choice')}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def password_generator():
    try:
        length = int(input("Enter password length: "))
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def to_do_list():
    tasks = []
    while True:
        action = input("(A)dd, (V)iew, (D)elete, (Q)uit: ").lower()
        if action == 'a':
            tasks.append(input("Enter task: "))
        elif action == 'v':
            print("Tasks:", tasks)
        elif action == 'd':
            task = input("Enter task to delete: ")
            if task in tasks:
                tasks.remove(task)
        elif action == 'q':
            break

def detailed_system_info():
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Hostname: {socket.gethostname()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"UUID: {uuid.uuid1()}")

def advanced_file_hasher():
    path = input("Enter file path: ")
    try:
        with open(path, "rb") as f:
            file_content = f.read()
        hashes = {
            'MD5': hashlib.md5(file_content).hexdigest(),
            'SHA-1': hashlib.sha1(file_content).hexdigest(),
            'SHA-256': hashlib.sha256(file_content).hexdigest()
        }
        for algo, hash_value in hashes.items():
            print(f"{algo} Hash: {hash_value}")
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")

def json_data_handler():
    print("1. Create JSON\n2. Read JSON")
    choice = input("Select option: ")
    if choice == '1':
        data = {}
        key = input("Enter key: ")
        value = input("Enter value: ")
        data[key] = value
        with open("data.json", "w") as f:
            json.dump(data, f)
        print("Data saved to data.json")
    elif choice == '2':
        try:
            with open("data.json", "r") as f:
                print(json.load(f))
        except FileNotFoundError:
            print("data.json not found. Please create the file first.")

def prime_finder():
    try:
        num = int(input("Enter a number: "))
        if num < 2 or any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)):
            print("Not a prime number.")
        else:
            print("It is a prime number!")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def network_scanner():
    hostname = input("Enter hostname to check: ")
    try:
        ip = socket.gethostbyname(hostname)
        print(f"IP Address of {hostname}: {ip}")
    except socket.gaierror:
        print("Unable to resolve hostname.")

def uptime_checker():
    try:
        uptime_seconds = time.time() - os.stat('/proc/1').st_ctime
        uptime_string = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
        print(f"System Uptime: {uptime_string}")
    except Exception:
        print("Unable to fetch system uptime on this OS.")

if __name__ == "__main__":
    main_menu()
