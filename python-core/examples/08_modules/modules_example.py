"""Modules example.

This module demonstrates importing from the standard library and
from a local module (helpers.py) in the same folder.
"""

import math
import os
from datetime import datetime

import helpers
from helpers import celsius_to_fahrenheit

# Standard library modules
print("Square root of 16:", math.sqrt(16))
print("Current working directory:", os.getcwd())
print("Current time:", datetime.now())

# Local module: accessed via the module name
print("App name:", helpers.APP_NAME)

# Local module: imported function used directly
print("25C in Fahrenheit:", celsius_to_fahrenheit(25))

if __name__ == "__main__":
    print("Running modules_example.py directly.")
