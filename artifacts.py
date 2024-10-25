# Import packages

import genshin
import pandas as pd
import asyncio

async def recover_genshin_user_infos(client, cards):
    return await client.get_genshin_user(cards[0].uid)

def recover_genshin_character_infos(genshin_user_infos):
    data = pd.DataFrame(asyncio.run(genshin_user_infos.characters),
                        columns=['release_id', 'name', 'element', 'rarity',
                                   'icon', 'collab',
                                   'level', 'friendship_level',
                                   'constellation', 'weapon', 'artifacts',
                                   'constellations', 'outfits'])

    return data

def recover_genshin_artifacts(df):
    data_artifacts = pd.DataFrame(columns=['name',
                                           'flower', 'plum',
                                            'hourglass', 'coup', 'hat'])
    
    for ind, row in df.iterrows():
        data_artifacts.iloc[-1] = pd.DataFrame(row['artifacts'])

    return data_artifacts

"""
TO DO : 
    - CALCULATE AN ARTIFACT CV 
    - CALCULATE AN ARTICACT RV (with given parameters to consider)
New dataframe ?
"""