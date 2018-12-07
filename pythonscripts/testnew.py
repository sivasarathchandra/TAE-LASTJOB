import requests
import re
import sys
import datetime
USERNAME = 'pramod@adnear.com'
PASSWORD = 'ka09ez9177'
LOGIN_URL = 'https://engage.adnear.net/login'


class Adnear(object):

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.session = None
        self.loginDone = False
        self.login()
        self.campaignDict = {}
        return

    def _get(self, url):
        res = self.session.get(url)
        return res

    def _post(self, url, data):
        res = self.session.post(url, data)
        return res

    def _getYesterday(self):
        return str(datetime.date.today() - datetime.timedelta(days=1))

    def login(self):
        self.session = requests.Session()
        response = self._get(LOGIN_URL)
        expr = '.*authenticity_token.*value="(.*)".*'
        reExp = re.compile(expr)
        for line in response.text.split('\n'):
            if 'authenticity_token' in line:
                token = reExp.match(line).group(1)

        data = {'utf8': True,
                'authenticity_token': token, AApmqD/F9KRsa1W6pZCIDIgIiFC8qOwjdW7M4cxPVlY
                'user[email]': 'pramod@adnear.com',
                'user[password]': 'ka09ez9177',
                'user[remember_me]': '0',
                'commit': ''}
        response = self._post(LOGIN_URL, data=data)
        if response.status_code == 200:
            print("Login Successful")
            self.loginDone = True

    def logout(self):
        self.loginDone = False

    def getAllCampaigns(self):
        date = self._getYesterday()
        get_url = 'https://engage.adnear.net/revenue/campaign/report/details?start_date={0}&end_date={1}'.format(date, date)
        print(get_url)
        if self.loginDone:
            response = self._get(get_url)
            expr = '.*" title="(Allspark: .*)"><span .*'
            expr2 = '.*<td><a href="/AdNear/campaigns/(.*)" title="All'
            expr3 = '.*" title="(.*)"></span'
            token = None
            for line in response.text.split('\n'):
                if 'Allspark: ' in line:
                    reExp = re.compile(expr)
                    token = reExp.match(line).group(1)
                    print(token)
                    reExp2 = re.compile(expr2)
                    item = reExp2.match(line).group(1)
                    print(item)
                    reExp3 = re.compile(expr3)
                    item2 = reExp3.match(line).group(1)
                    print(item2)
                    if ',' not in item:
                        campaignId = item
                        self.campaignDict[campaignId] = {}
                        self.campaignDict[campaignId]['name'] = token
                        self.campaignDict[campaignId]['country'] = item2
                    else:
                        token = None

        return self.campaignDict

    def getReport(self, campaignId):
        date = self._getYesterday()
        get_url_string = 'https://engage.adnear.net/AllSpark-Main/campaigns/%s/daily/report/details?start_date=%s&end_date=%s'
        exprImp = '.*<td class="f-count imps">(.*)<.*'
        exprClk = '.*<td class="f-count clks">(.*)<.*'
        if self.loginDone:
            get_url = get_url_string % (campaignId, date, date)
            print(get_url)
            response = self._get(get_url)
            for line in response.text.split('\n'):
                if line != '':
                    #print(repr(line))
                    if 'f-count imps' in line:
                        reExp = re.compile(exprImp)
                        self.campaignDict[campaignId][
                            'Imp'] = float(reExp.match(line).group(1))
                        print(self.campaignDict[campaignId]['Imp'])
                    if 'f-count clks' in line:
                        reExp = re.compile(exprClk)
                        self.campaignDict[campaignId][
                            'Clk'] = float(reExp.match(line).group(1))
                        print(self.campaignDict[campaignId]['Clk'])
                    if re.match('\bctr\b',line) is not None:
                        print(repr(line))
                        self.campaignDict[campaignId]['CTR'] = float(self.campaignDict[campaignId][
                                                                'Clk']) / float(self.campaignDict[campaignId]['Imp']) * 100

    def getAllReports(self):
        for campaignId in self.campaignDict.keys():
            self.getReport(campaignId)

    def getCampaignDetails(self, campaignId):
        get_url_string = 'https://engage.adnear.net/AllSpark-Main/campaigns/%s/edit'
        if self.loginDone:
            #if campaignId == 'all':
                #for campaignId in self.campaignDict.keys():
                    get_url = get_url_string % campaignId
                    response = self._get(get_url)
                    expr1 = '.*campaign_daily_targeting_count.*value="(.*)"'
                    expr2 = '.*campaign_total_targeting_count.*value="(.*)"'
                    expr3 = '.*campaign_start_time.*value="(.*)"'
                    expr4 = '.*campaign_end_time.*value="(.*)"'
                    expr5 = '.*"selected">(.*)<.*'
                    for line in response.text.split('\n'):
                        if 'campaign_daily_targeting_count' in line and 'value' in line:
                            reExp = re.compile(expr1)
                            self.campaignDict[campaignId][
                                'campaign_daily_targeting_count'] = reExp.match(line).group(1)
                        if 'campaign_total_targeting_count' in line and 'value' in line:
                            reExp = re.compile(expr2)
                            self.campaignDict[campaignId][
                                'campaign_total_targeting_count'] = reExp.match(line).group(1)
                        if 'campaign_start_time' in line and 'value' in line:
                            reExp = re.compile(expr3)
                            self.campaignDict[campaignId][
                                'campaign_start_time'] = reExp.match(line).group(1)
                        if 'campaign_end_time' in line and 'value' in line:
                            reExp = re.compile(expr4)
                            self.campaignDict[campaignId][
                                'campaign_end_time'] = reExp.match(line).group(1)
                        if  'campaign_advertiser_id' in line and 'selected' in line:
                            reExp = re.compile(expr5)
                            self.campaignDict[campaignId][
                                'advertiser_id'] = reExp.match(line).group(1)
        #for campaignId,values in self.campaignDict.items():
            #print(campaignId)
            #print(values)
                    
    def getAllCampaignDetails(self):
        for campaignId in self.campaignDict.keys():
            self.getCampaignDetails(campaignId)
