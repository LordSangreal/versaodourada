import json

mf = json.load(open('tools/repo/tools/rom_manifest_gold.json', encoding='utf-8'))

remaining_johto = [
    'BLACKTHORN_CITY', 'BLACKTHORN_GYM_1F', 'BLACKTHORN_GYM_2F',
    'BLACKTHORN_DRAGON_SPEECH_HOUSE', 'BLACKTHORN_EMYS_HOUSE',
    'BLACKTHORN_MART', 'BLACKTHORN_POKECENTER_1F',
    'DRAGONS_DEN_1F', 'DRAGONS_DEN_B1F',
    'ROUTE_36', 'ROUTE_36_NATIONAL_PARK_GATE', 'ROUTE_36_RUINS_OF_ALPH_GATE',
    'ROUTE_44', 'ROUTE_45', 'ROUTE_46',
    'RUINS_OF_ALPH_OUTSIDE', 'RUINS_OF_ALPH_INNER_CHAMBER',
    'RUINS_OF_ALPH_AERODACTYL_CHAMBER', 'RUINS_OF_ALPH_HO_OH_CHAMBER',
    'RUINS_OF_ALPH_KABUTO_CHAMBER', 'RUINS_OF_ALPH_OMANYTE_CHAMBER',
    'RUINS_OF_ALPH_RESEARCH_CENTER',
    'VICTORY_ROAD', 'VICTORY_ROAD_GATE',
    'HALL_OF_FAME', 'INDIGO_PLATEAU_POKECENTER_1F',
    'WILLS_ROOM', 'KOGAS_ROOM', 'BRUNOS_ROOM', 'KARENS_ROOM', 'LANCES_ROOM',
    'NATIONAL_PARK_BUG_CONTEST',
]

for m in remaining_johto:
    if m in mf['maps']:
        spec = mf['maps'][m]
        print('%s: group=%d, map=%d' % (m, spec['group'], spec['map']))
    else:
        print('%s: NOT FOUND' % m)
