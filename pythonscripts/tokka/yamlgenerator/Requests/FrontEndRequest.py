import re
import requests

LOGIN_URL = "https://sandboxcernercare.com/accounts/login?returnTo=https%3A%2F%2Fstaginghealtheintent.com%2Fsession-api%2Fprotocol%2Fopenid2%2Fsso%3FlookupId%3DeyJpZCI6IjkwN2I4NzUyLWNiMzQtNGE1MC05MGZjLWM2OWU5MWI4NDdlNCIsInRhcmdldFJvb3QiOiJodHRwczovL2FkdmVudGlzdGhlYWx0aHN5c3RlbS5hbmFseXRpY3Muc3RhZ2luZ2hlYWx0aGVpbnRlbnQuY29tL2V4cGxvcmUvcmV2ZW51ZV9jeWNsZS9jb25maWcvY29uZmlnL2FnZV9jYXRlZ29yeSIsInRpbWUiOiIyMDE4LTA0LTA2VDA5OjM5OjAyLjg3MFoiLCJyZWFsbUlkIjoiQ1NmSDFKOURFQllfYjJubVlEeGptLWlXa1V4TXFzV0UifQ"
USERNAME = "revcycleanalytics@gmail.com"
PASSWORD = "rcanalytics1"

class Cerner(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.session = None
        self.loginDone = False
        self.login()
        return

    def _get(self, url):
        res = self.session.get(url)
        return res

    def _post(self, url, data):
        res = self.session.post(url, data)
        return res

    def login(self):
        self.session = requests.Session()
        response = self._get(LOGIN_URL)
        data = {'authUsername': 'revcycleanalytics @ gmail.com',
        'authPassword': 'rcanalytics1',
        'usingPassword': 1,
        'login': 'Log  In'}
        response = self._post(LOGIN_URL, data=data)
        if response.status_code == 200:
            print("Login Successful")
            self.loginDone = True
        else:
            print("Login Failed")

    def ageCategories(self):
        get_url = "https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category"
        if self.loginDone:
            response = self._get(get_url)
            for line in response.text.split('\n'):
                print(line)
