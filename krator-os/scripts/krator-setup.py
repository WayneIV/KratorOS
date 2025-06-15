#!/usr/bin/env python3
"""Interactive setup wizard for Krator OS."""
import getpass
import subprocess

print("Welcome to Krator OS setup wizard")

username = input("Create user name [krator]: ") or "krator"
password = getpass.getpass("Password: ")

subprocess.run(["adduser", "--disabled-password", "--gecos", "", username], check=True)
subprocess.run(["chpasswd"], input=f"{username}:{password}", text=True, check=True)

print("User created. You can now log in as", username)

