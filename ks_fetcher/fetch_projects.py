from urllib.request import urlopen

class KickstarterProjectsFetcher():
    _starting_url = \
    "https://www.kickstarter.com/discover/advanced?sort=most_funded&seed=2531927&page="

    def __init__(self,
                 start_page,
                 end_page,
                 starting_url=_starting_url):
        self.start_page = start_page
        self.curr_page = start_page
        self.end_page = end_page
        self.starting_url = starting_url

    def __str__(self):
        return "Starting URL: {}\nStart page: {}\nEnd page: {}".format(
            self.starting_url,
            self.start_page,
            self.end_page)

    def fetch_next(self):
        _url_to_fetch = self.starting_url + str(self.curr_page)
        _result = urlopen(_url_to_fetch).read()
        self.curr_page += 1
        return (_result, _url_to_fetch)
