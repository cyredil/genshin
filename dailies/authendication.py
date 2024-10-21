import genshin

file = open('dailies/credentials.txt', 'r')
credentials = file.read().split(':', 1)
file.close()
mail = credentials[0]
password = credentials[1]

# set browser cookies
client = genshin.Client()
client.set_browser_cookies()


# login with username and password
client = genshin.Client()
cookies = client.login_with_password(mail, password)
print(cookies)