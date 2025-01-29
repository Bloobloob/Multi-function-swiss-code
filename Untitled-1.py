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
        '6': ("File Organizer", file_organizer),
        '7': ("File Hasher", advanced_file_hasher),
        '8': ("JSON Data Handler", json_data_handler),
        '9': ("Prime Number Finder", prime_finder),
        '10': ("Basic Network Scanner", network_scanner),
        '11': ("System Uptime Checker", uptime_checker)
    }
    selected_functions = []
    print("Welcome to the Swiss-Code")
    while True:
        print("Select functions you want to use separated by commas or just type 'start' to start")
        for key, (name, _) in available_functions.items():
            print(f"{key}. {name}")
        selection = input("Enter your choices: ")
        if selection.lower() == 'start':
            break
        else:
            choices = selection.split(',')
            for choice in choices:
                choice = choice.strip()
                if choice in available_functions and choice not in selected_functions:
                    selected_functions.append(choice)
    return selected_functions, available_functions

def calculator():
    print("Calculator: Enter your expression like (5 * 4 + 6):")
    expression = input("Expression: ")
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

def unit_converter():
    print("1. Kilometers to Miles \n2. Celsius to Fahrenheit \n3. Kilogram to Pounds")
    choice = input("Choose conversion type: ")
    value = float(input("Enter value: "))
    conversions = {"1": value * 0.621371, "2": (value * 9/5) + 32, "3": value * 2.20462}
    print(f"Converted value: {conversions.get(choice, 'Invalid choice')}")

def password_generator():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated Password: {password}")

def to_do_list():
    tasks = []
    while True:
        action = input("(A)dd task, (V)iew tasks, (D)elete task, (Q)uit: ").lower()
        if action == 'a':
            task = input("Enter task: ")
            tasks.append(task)
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
    with open(path, "rb") as f:
        file_content = f.read()
    hashes = {
        'MD5': hashlib.md5(file_content).hexdigest(),
        'SHA-1': hashlib.sha1(file_content).hexdigest(),
        'SHA-256': hashlib.sha256(file_content).hexdigest()
    }
    for algo, hash_value in hashes.items():
        print(f"{algo} Hash: {hash_value}")

def json_data_handler():
    print("1. Create JSON \n2. Read JSON")
    choice = input("Select option: ")
    if choice == '1':
        data = {}
        key = input("Enter key: ")
        value = input("Enter value: ")
        data[key] = value
        with open("data.json", "w") as f:
            json.dump(data, f)
    elif choice == '2':
        with open("data.json", "r") as f:
            print(json.load(f))

def prime_finder():
    num = int(input("Enter a number: "))
    if num < 2:
        print("Not a prime number.")
        return
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number.")
            return
    print("It is a prime number!")

def network_scanner():
    hostname = input("Enter hostname to check: ")
    try:
        ip = socket.gethostbyname(hostname)
        print(f"IP Address of {hostname}: {ip}")
    except socket.gaierror:
        print("Unable to resolve hostname.")

def uptime_checker():
    uptime_seconds = time.time() - os.stat('/proc/1').st_ctime
    uptime_string = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
    print(f"System Uptime: {uptime_string}")

if __name__ == "__main__":
    selected_functions, available_functions = main_menu()
    while True:
        print("\nAvailable Functions:")
        for key in selected_functions:
            print(f"{key}. {available_functions[key][0]}")
        choice = input("Choose an option (or 'exit' to quit): ")
        if choice.lower() == "exit":
            break
        elif choice in selected_functions:
            available_functions[choice][1]()
        else:
            print("Invalid choice.")
