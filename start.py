import time
import random
from pymongo import MongoClient
from ks_fetcher.fetch_projects import KickstarterProjectsFetcher
from ks_parser.parse_search_results import ProjectsFromResultsParser
kf = KickstarterProjectsFetcher(1,50)


client = MongoClient()
ks_db = client.kickstarter
ks_searches = ks_db.searches

def fetch_data(from_page,to_page):
    for i in range(from_page,to_page):
        print(i)
        result, url_to_fetch = kf.fetch_next()
        entry = {
            "URL":url_to_fetch,
            "result":result
        }
        print(url_to_fetch)
        entry_id = ks_searches.insert_one(entry).inserted_id
        time.sleep(random.randint(0, 10))

def parse_data():
    parser = ProjectsFromResultsParser()
    for entry in ks_searches.find():
        try:
            print(parser.parse(entry['result']))
        except:
            print("error while parsing")

parse_data()
