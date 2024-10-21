import genshin
from dailies.bin.bin import load_credentials

def authenticate():
    credentials = load_credentials('dailies/credentials.ini')
    mail = credentials[0]
    password = credentials[1]

    # set browser cookies
    client = genshin.Client()
    client.set_browser_cookies()


    # login with username and password
    client = genshin.Client()
    cookies = client.login_with_password(mail, password)

    client.set_cookies(cookies)

    return client

if __name__ == "__main__":
    authenticate()