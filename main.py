import sys
import os

# Add the 'dailies' subfolder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'dailies'))

# Import the credentials module
import credentials

# Run the credentials GUI function
if __name__ == "__main__":
    credentials.credentials_gui()