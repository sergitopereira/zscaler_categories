from helpers.zia_api_calls import ZsTalker
import requests
from helpers.logger import get_logger

def parse_file(file):
    with open(file, 'r') as f:
        file = f.readlines()
    urls = []
    for i in file:
        if i.startswith('#'):
            continue
        if i == "\n":
            continue
        urls.append(i.split()[0])
    return urls


def start(apikey, username, password, cloud, category_name, file):
    hp_log = get_logger(logger_name='categories', log_file='categories')
    hp_log.info(f"Starting to Execute script, category {category_name}")
    dbCategorizedUrls = parse_file(file)
    hp_log.info(f"obtained urls={dbCategorizedUrls}")
    zstalker = ZsTalker(cloud)
    zstalker.authenticate(apikey, username, password)
    categories = zstalker.list_url_categories(custom=True)
    for cat in categories:
        if cat['configuredName'] == category_name:
            hp_log.info(f"Existing configuration: {cat}")
            cat.update(dbCategorizedUrls=dbCategorizedUrls)
            try:
                resp = zstalker.update_call(payload=cat, url=f"/urlCategories/{cat['id']}")
                hp_log.info(f"Resulting configuration: {resp}")
            except requests.HTTPError as e:
                hp_log.info(f"Error: {e}")
            return
