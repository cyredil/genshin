
# Import the credentials module
import dailies.credentials as credentials
import dailies.authentication as authentication

# Run the credentials GUI function
if __name__ == "__main__":
    credentials.credentials_gui()
    cookies = authentication.authenticate()