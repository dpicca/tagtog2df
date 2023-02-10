
from pathlib import Path
import json
import pandas as pd
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def _parse_json(data):
    annotatable_parts = data["annotatable"]["parts"]
    anncomplete = data["anncomplete"]
    sources = data["sources"]
    metas = data["metas"]

    entities_list = []
    relations_list = []
    for entity in data["entities"]:
        entities_list.append({
            "Class ID": entity["classId"],
            "Part": entity["part"],
            "Start": entity["offsets"][0]["start"],
            "Text": entity["offsets"][0]["text"],
            "Coordinates": entity["coordinates"],
            "Confidence State": entity["confidence"]["state"],
            "Confidence Who": entity["confidence"]["who"],
            "Confidence Prob": entity["confidence"]["prob"],
            "Fields": entity["fields"],
            "Normalizations": entity["normalizations"]
        })

    for relation in data["relations"]:
        relations_list.append({
            "Relation Class ID": relation["classId"],
            "Relation Type": relation["type"],
            "Relation Directed": relation["directed"],
            "Relation Entities": relation["entities"],
            "Relation Confidence State": relation["confidence"]["state"],
            "Relation Confidence Who": relation["confidence"]["who"],
            "Relation Confidence Prob": relation["confidence"]["prob"]
        })



    return entities_list, relations_list

def _find_match(col1, col2, col3):
    for values in col1:
        for value in values:
            values = value.split("|")
            if values[0] == col2 and values[1] == col3:
                return value
            return pd.NA

def allfiles_onedataframe(path):
    alldf=[]
    root_dir = Path(path)

    for p in root_dir.rglob('*.json'):
        with open(p) as user_file:
            logging.info(f'Reading file {user_file}')
            data = json.load(user_file)
        entities_list, relations_list = _parse_json(data)
        entities_df = pd.DataFrame(entities_list)
        if relations_list != []:
            relations_df = pd.DataFrame(relations_list)
            entities_df['relations'] = entities_df.apply(lambda x: _find_match(relations_df['Relation Entities'], x['Part'], x['Class ID']), axis=1)
            alldf.append(entities_df)
        else:
            alldf.append(entities_df)
    return pd.concat(alldf)



def allfiles_listdataframe(path):
    root_dir = Path(path)
    alldf=[]
    for p in root_dir.rglob('*.json'):
        with open(p) as user_file:
            logging.info(f'Reading file {user_file}')
            data = json.load(user_file)
        entities_list, relations_list = _parse_json(data)
        entities_df = pd.DataFrame(entities_list)
        if relations_list != []:
            relations_df = pd.DataFrame(relations_list)
            entities_df['relations'] = entities_df.apply(lambda x: _find_match(relations_df['Relation Entities'], x['Part'], x['Class ID']), axis=1)
            alldf.append(entities_df)
        else:
            alldf.append(entities_df)
    return alldf

def onefile_onedataframe(pathfile):
    logging.info('Reading file',pathfile)
    with open(pathfile) as user_file:
        data = json.load(user_file)
    entities_list, relations_list = _parse_json(data)
    entities_df = pd.DataFrame(entities_list)
    if relations_list != []:
        relations_df = pd.DataFrame(relations_list)
        entities_df['relations'] = entities_df.apply(lambda x: _find_match(relations_df['Relation Entities'], x['Part'], x['Class ID']), axis=1)
    return entities_df

