from base64 import b64encode
import requests
import json


class JiraREST_Create():
    def createJira():
        post_url = 'https://jira2.cerner.com/rest/api/2/issue/'
        put_url = 'https://jira2.cerner.com/rest/api/2/issue/RCANALYTIC-25682/attachments/'
        userAndPass = b64encode(b"SC057441:Pavan$1251").decode("ascii")
        get_headers = {'Authorization': 'Basic %s' % userAndPass}
        put_headers = {'Authorization': 'Basic %s' % userAndPass, 'X-Atlassian-Token':'no-check'}

        # data = {
        #         "fields": {
        #                     "project": {
        #                                     "key": "RCANALYTIC"
        #                                 },
        #                     "summary": "Creating an issue via REST - Sample Jira 2",
        #                     "description": "Creating an issue via REST API",
        #                     "issuetype": {
        #                                     "name": "Defect"
        #                                 },
        #                     "reporter" : {"name":"SD056953"},
        #                     "assignee": {"name": "SD056953"},
        #                     "customfield_14801":["HealtheAnalytics Reporting"], #Solution Detail
        #                     "customfield_14802": ["Revenue Cycle HealtheAnalytics Reporting"], #JIRA Group
        #                     "customfield_10703":{                  #Frequency
        #                                             "self":"https://jira2.cerner.com/rest/api/2/customFieldOption/10400",
        #                                             "value":"Frequent",
        #                                             "id":"10400"
        #                                         },
        #                     "customfield_10208":{ #Lifecycle step found
        #                                             "self":"https://jira2.cerner.com/rest/api/2/customFieldOption/19002",
        #                                             "value":"System",
        #                                             "id":"19002"
        #                                         },
        #                     "customfield_10309":{  #Severity
        #                                             "self":"https://jira2.cerner.com/rest/api/2/customFieldOption/10208",
        #                                             "value":"Functional",
        #                                             "id":"10208"
        #                                         },
        #                     "customfield_14800":["Revenue Cycle Analytics"], #Solution
        #                     "attachment": [
        #                         {
        #                             "filename": "output.json",
        #                             "mimeType": "application/json"
        #                         },
        #                     ],
        #                     }
        #         }

        data = {
                "fields": {
                            "attachment": [
                                {
                                    "filename": "output.json",
                                    "mimeType": "application/text"
                                },
                            ],
                            }
                }

        data = json.dumps(data)

        # files = {'file': open('output.txt', 'rb')}
        r = requests.post(put_url, files={
            'file': open('output.json', 'r'),
                'comment':"Uploaded automatically.",
                'minorEdit':"false"
                }, headers=put_headers)
        print(r.status_code)
        print(r.text)

        # put_req = requests.put(url=put_url, data=data, headers = put_headers)

        # post_req = requests.post(url=post_url, data=data, headers=put_headers)

        # print(put_req.text)


if __name__ == '__main__':
    JiraREST_Create.createJira()