
# Import the credentials module
import asyncio
import genshin
from .utils import load_credentials, get_record_cards

async def authenticate(credentials):
    """authentication function

    ONLY LOG WITH GENSHIN USERNAME AND PASSWORD FOR NOW
    (WIP)

    Args:
        credentials (list): List with all credentials stored in credentials
            file
    
    Returns:
        genshin.Client: Genshin Client with cookies rightfully set
    """

    # Saving connection infos
    mail = credentials[0]
    password = credentials[1]

    # creating client
    client = genshin.Client()

    # Setting connection game
    if int(credentials[5])==0:
        client.default_game = genshin.Game.GENSHIN
    elif int(credentials[5])==1:
        client.default_game = genshin.Game.STARRAIL
    
    # Setting region server
    if int(credentials[6])==0:
        client.region = genshin.Region.OVERSEAS
    else:
        client.region = genshin.Region.CHINESE

    # Connecting with mail and password
    cookies = await client.login_with_password(mail, password)

    return client, cookies


def login(filepath='bin/credentials.ini'):
    """Login and retrieve main infos for user

    Returns:
        genshin.Client: Genshin client with set cookies
        genshin.Cards: Genshin cards object with all cards associated with
            the account
    """
    # Loading credentials of user
    cred = load_credentials(filepath)

    # log in with user credentials
    client, _ = asyncio.run(authenticate(cred))

    # Retrieve user cardes
    cards = asyncio.run(get_record_cards(client))

    return client, cards

# def captcha_solve(filepath='bin/credentials.ini'):
#     # Loading credentials of user
#     cred = load_credentials(filepath)

#     # Retriving cookies
#     _, cookies = asyncio.run(authenticate(cred))
#     cookies = dict(cookies)


#     app = Flask(__name__)

#     @app.route('/set_cookies')
#     def set_cookies():
#         # Setting the cookies
#         response = make_response(redirect('https://www.hoyolab.com/home/events'))
#         for key, value in cookies.items():
#             response.set_cookie(key, value)
#             print(key, value)
#         return response
    
#     app.run(debug=True, port=8052, use_reloader=False)
    
# if __name__ == "__main__":
#     captcha_solve("credentials.ini")

# from bin.login import login, captcha_solve
    