from bs4 import BeautifulSoup
from .KickstarterProject import KickstarterProject
import json
class ProjectsFromResultsParser():

    def parse(self, result):
        soup = BeautifulSoup(result, 'html.parser')
        divs = soup.findAll('div')

        projects = []
        for div in divs:
            if div.get('data-project'):
                d = json.loads(div.get('data-project'))
                ksp = KickstarterProject(d['id'])
                projects.append(ksp)
        return projects
