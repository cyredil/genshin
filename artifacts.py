# Import packages

import genshin
import pandas as pd
import asyncio
from bin.utils import solve_geeTest


async def get_full_genshin_char_infos(client, cards):
    """
    """
    try:
        data = await client.get_genshin_detailed_characters(cards[0].uid)
    except genshin.GeetestError:
        await solve_geeTest(client)
        data = await client.get_genshin_detailed_characters(cards[0].uid)

    df = pd.DataFrame([vars(char) for char in data.characters])

    df = df[['id', 'name',
             'element',
             'rarity',
             'icon', 'display_image',
             'collab',
             'level', 'friendship',
             'skills',
             'constellation', 'constellations',
             'weapon_type', 'weapon',
             'artifacts',
             'selected_properties', 'base_properties',
             'extra_properties', 'element_properties']]
    return df


def recover_genshin_artifacts(data):
    """
    """
    arti_list = []

    for _, row in data.iterrows():
        for arti in row['artifacts']:
            arti_dic = {
                'char_id': row['id'],
                'char_name': row['name'],
                'char_element': row['element'],
                'arti_id': arti.id,
                'icon': arti.icon,
                'name': arti.name,
                'pos_name': arti.pos_name,
                'pos': arti.pos,
                'rarity': arti.rarity,
                'level': arti.level,
                'set': {'id': arti.set.id,
                        'name': arti.set.id,
                        'first_effect_active': arti.set.effects[0].active,
                        'second_effect_active': arti.set.effects[1].active},
                'main_stat': {'bonus': arti.main_stat.info.name,
                              'type': arti.main_stat.info.type,
                              'value': arti.main_stat.value,
                              'times': arti.main_stat.times},
                'sub_stats': {
                    f'sub_stat{i}': {'bonus': arti.sub_stats[i].info.name,
                                     'type': arti.sub_stats[i].info.type,
                                     'value': arti.sub_stats[i].value,
                                     'times': arti.sub_stats[i].times} for i in range(len(arti.sub_stats))}
            }
            arti_list.append(arti_dic)

    print(arti_list)
    return pd.DataFrame(arti_list)

"""
TO DO :
    - CALCULATE AN ARTIFACT CV
    - CALCULATE AN ARTICACT RV (with given parameters to consider)
"""

"""
from bin.login import login
import asyncio
client, cards = login()
from artifacts import *
g = asyncio.run(get_full_genshin_char_infos(client, cards))
f = recover_genshin_artifacts(g)

"""
