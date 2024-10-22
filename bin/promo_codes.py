import requests
import genshin
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import asyncio


def scrap_promo_codes():
    page = requests.get('https://www.pockettactics.com/genshin-impact/codes')
    soup = bs(page.content, 'html.parser')

    lines = soup.findAll('li')

    strong_lines = [li for li in lines if (
        li.find('strong') and '–' in li.text)]
    classic_lines = [li for li in lines if (
        not (li.find('strong')) and '–' in li.text)]

    codes = []

    for line in strong_lines:
        game = 'genshin'
        code = line.find('strong').text
        award = line.text.split('–')[1].strip()
        recent = 'new'
        codes.append([game, code, award, recent])

    for line in classic_lines:
        game = 'genshin'
        line = line.text.split('–')
        code = line[0].strip()
        award = line[1].strip()
        recent = 'old'
        codes.append([game, code, award, recent])

    data = pd.DataFrame(codes, columns=['game', 'code', 'award', 'recent'])
    data.to_csv('promo_codes.csv')

async def test_promo_code(code, award, client):
    print(f'BOT: Testing code *{code}*...')
    time.sleep(5)
    try :
        await client.redeem_code(code)
        return (f'BOT: Code *{code}* claimed! You earned {award}!')
    except genshin.RedemptionClaimed:
        return f'BOT: *{code}* already claimed! You thief!'
    except genshin.RedemptionInvalid as e:
        if '-2001' in str(e):
            return 'BOT: Code as Expired...'
        else:
            return 'BOT: Code is invalid...?'
    except:
        return 'BOT: Unexpected Error'


def test_promo_codes(df, client, new_only=True):
    df = pd.read_csv('bin/promo_codes.csv')
    if new_only:
        df = df.loc[df['recent'] == 'new']
        
    for ind, row in df.iterrows():
        print(asyncio.run(test_promo_code(row['code'], row['award'], client)))
    print('BOT: No more new codes to try out!')

if __name__ == '__main__':
    df = scrap_promo_codes()
    
    