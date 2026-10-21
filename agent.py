#!/usr/bin/env python3
"""Convenient CLI wrapper for Technocore Agent that auto-loads the passphrase."""

import os
import sys
from pathlib import Path

# Set working directory to script location
os.chdir(Path(__file__).parent)

# Patch getpass before importing adapter so default parameter binds to our wrapper
pass_file = Path("secrets/passphrase.txt")
if pass_file.exists():
    passphrase = pass_file.read_text().strip()
    import getpass
    getpass.getpass = lambda prompt="": passphrase

import adapter
if pass_file.exists():
    adapter.getpass.getpass = lambda prompt="": passphrase

if __name__ == "__main__":
    sys.exit(adapter.main())
