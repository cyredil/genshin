
# Import the credentials module
import asyncio
import genshin
import bin.utils as utils
import bin.credentials as credentials
import bin.authentication as authentication

# Run the credentials GUI function
if __name__ == "__main__":
    credentials.credentials_gui()

    cred = utils.load_credentials('bin/credentials.ini')

    client = asyncio.run(authentication.authenticate())
    asyncio.run(utils.claim_reward(client))
    account_infos = asyncio.run(utils.get_account_infos(client, int(cred[5])))
    print(account_infos)
    