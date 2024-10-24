
# importing packages
import requests
import genshin
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import asyncio


def scrap_promo_codes():
    """Function to scrap all promo codes available in
    'https://www.pockettactics.com/genshin-impact/codes'"""

    # Setting page requested
    page = requests.get('https://www.pockettactics.com/genshin-impact/codes')

    # Parsing page
    soup = bs(page.content, 'html.parser')

    # Selecting all lists
    lines = soup.findAll('li')

    # Separating lines in two categories:
    #   strong ones: usually recent code
    #   classic ones: usually old code
    # And only keeping the line with a '\u2013' separator (used to separate
    # code and rewards)
    strong_lines = [li for li in lines if (
        li.find('strong') and '–' in li.text)]
    classic_lines = [li for li in lines if (
        not (li.find('strong')) and '–' in li.text)]

    codes = []

    # Adding every strong lines to code with the game type, the code,
    # the awards and its recentness
    for line in strong_lines:
        game = 'genshin'
        code = line.find('strong').text
        award = line.text.split('–')[1].strip()
        recent = 'new'
        codes.append([game, code, award, recent])

    # Adding every recent lines to code with the game type, the code,
    # the awards and its recentness
    for line in classic_lines:
        game = 'genshin'
        line = line.text.split('–')
        code = line[0].strip()
        award = line[1].strip()
        recent = 'old'
        codes.append([game, code, award, recent])

    # Saving codes in a promo_codes.csv
    data = pd.DataFrame(codes, columns=['game', 'code', 'award', 'recent'])
    data.to_csv('bin/promo_codes.csv')

async def test_promo_code(code, award, client):
    """function to test a given promo code

    Args:
        code (str): Code to try out
        award (str): Expected award string to display
        client (genshin.client): Genshin client already logged in
    
    Returns:
        str: String with the test code result with detailed.
            (Code cain be 'claimable', 'Already claimed', 'Expired' or 
            Invalid)
    """

    # Waiting 5 seconds to test code to avoid genshin blocking the claim
    # (Due to too much claims)
    print(f'BOT: Testing code *{code}*...')
    time.sleep(5)

    # Try to redeem code with corresponding output
    try :
        await client.redeem_code(code)
        return (f'BOT: Succes! Code *{code}* claimed! You earned {award}!')
    except genshin.RedemptionClaimed:
        return f'BOT: *{code}* already claimed! You thief!'
    except genshin.RedemptionInvalid as e:
        if '-2001' in str(e): # -2001 correspond to an expired code
            return 'BOT: Code as Expired...'
        else:
            return 'BOT: Code is invalid...?'
    except:
        return 'BOT: Unexpected Error'


def test_promo_codes(df, client, new_only=True):
    """Testing all promo code on a client given the code dataframe 
    corresponding.

    Only test condes listed as activ by default (to avoid long run time)

    Args:
        df (pandas.DataFrame): Dataframe with all codes.
            (Should be generated using `scrap_promo_codes`)
        client (genshin.client): Genshin client succesfully logged in
        new_only (bool, optional): True (default) if function should test
            new codes only or old and new codes.
    """

    # Reading df
    df = pd.read_csv('bin/promo_codes.csv')

    # Kepping only new codes if new_only is True
    if new_only:
        df = df.loc[df['recent'] == 'new']
    
    count = 0
    # Claiming every code in df
    for ind, row in df.iterrows():
        r = asyncio.run(test_promo_code(row['code'], row['award'], client))

        count += int('succes' in r) # counting the number of succes
        print(r)
    print(f'BOT: No more new codes to try out! You redeemed {count} codes!')

if __name__ == '__main__':
    df = scrap_promo_codes()
    
    