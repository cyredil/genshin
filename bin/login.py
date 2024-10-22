
# Import the credentials module
import asyncio
import genshin
from .utils import load_credentials, get_record_cards

async def authenticate(credentials):
    mail = credentials[0]
    password = credentials[1]

    # login with username and password
    client = genshin.Client()

    if int(credentials[5])==0:
        client.default_game = genshin.Game.GENSHIN
    elif int(credentials[5])==1:
        client.default_game = genshin.Game.STARRAIL
    
    if int(credentials[6])==0:
        client.region = genshin.Region.OVERSEAS
    else:
        client.region = genshin.Region.CHINESE
    
    cookies = await client.login_with_password(mail, password)
    cookies = str(cookies).split(' ')

    ltuid = cookies[5].split('=')[1][1:-1]
    ltoken = cookies[3].split('=')[1][1:-1]
    cookies_dic = {'ltuid_v2': ltuid,
                   'ltoken_v2': ltoken
                   }

    client.set_cookies(cookies_dic) # cookie header

    return client

# Run the credentials GUI function
def login():
    cred = load_credentials('bin/credentials.ini')
    client = asyncio.run(authenticate(cred))
    cards = asyncio.run(get_record_cards(client))
    print('??')

    return cred, client, cards
    
if __name__ == "__main__":
    a, b, c = login()