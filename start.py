import time
import random
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from ks_fetcher.fetch_projects import KickstarterProjectsFetcher
from ks_parser.parse_search_results import ProjectsFromResultsParser
import sys
kf = KickstarterProjectsFetcher(1,50)


client = MongoClient()
ks_db = client.kickstarter
ks_searches = ks_db.searches
ks_projects = ks_db.projects

def fetch_data(from_page,to_page):
    for i in range(from_page, to_page):
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
    i = 0
    for entry in ks_searches.find():
        try:
            # if i > 1:
            #     break
            i += 1
            projects = parser.parse(entry['result'])
            for project in projects:
                try:
                    entry_id = ks_projects.insert_one(dict(project)).inserted_id
                except DuplicateKeyError:
                    print('Key already exists')
            #ile_to_write = open('file'+str(i)+'.txt', 'w')
            #file_to_write.write(projects[0])
        except:
            print("error while parsing", sys.exc_info()[0])

parse_data()
