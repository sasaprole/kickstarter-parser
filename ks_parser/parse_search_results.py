from bs4 import BeautifulSoup

class ProjectsFromResultsParser():

    def parse(self, result):
        soup = BeautifulSoup(result, 'html.parser')
        data = soup.findAll('div')
        return data
