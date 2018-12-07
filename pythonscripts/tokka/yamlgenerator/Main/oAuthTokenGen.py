from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
import requests
import oauthlib
import pprint


client = oauthlib.oauth1.Client('c0c11d7a-48c1-461d-8be9-56e9fb60b28f', client_secret='Jjftdr7d_z7kjM1_GTXKskfQZs9aCD1l')
uri, headers, body = client.sign('https://oauth.devcareaware.com/oauth/')
pprint.pprint(headers)

twitter = OAuth1Session('c0c11d7a-48c1-461d-8be9-56e9fb60b28f',
                            client_secret='Jjftdr7d_z7kjM1_GTXKskfQZs9aCD1l',
                            resource_owner_key='revcycleanalytics@gmail.com',
                            resource_owner_secret='rcanalytics1')
url = 'https://oauth.sandboxcareaware.com/oauth/'
r = twitter.get(url)
print(r.text)

# oauth = OAuth1Session('99bb308b-0a2b-4547-a967-b6287914469d', client_secret='cHowMqwBMh2N4ShhBDrbcRZNLzo76VrA')
# param = {'oauth_callback':'http://127.0.0.1:3000/oauth/callback'}
# url = "https://authorization.devcerner.com/introspection"
# fetch_response = oauth.get(url)
# print(fetch_response.text)
#
# r = test.get(url,params=param)
# print(r.content)
# param2 = {'oauth_token_secret':'ZdeQr4C_ne8CUHI7XG46uOaPpDlXcayd'}
# r = test.get(url,params=param2)
# print(r.content)

# st = 'OAuth'
# final_str = ""
# str1 = ""
# str2 = ""
# client = oauthlib.oauth1.Client('99bb308b-0a2b-4547-a967-b6287914469d', client_secret='cHowMqwBMh2N4ShhBDrbcRZNLzo76VrA')
# url = "https://authorization.devcerner.com/introspection"
# uri, headers, body = client.sign(url)
# print(uri)
# print(headers)

# for k,v in headers.items():
#     if k == 'Authorization':
#         s1 = v.split(",")
#         for i in range(0,6):
#             if i==0:
#                 s2 = s1[0].split(" ")
#                 final_str = final_str+s2[1]+","
#             elif i<5:
#                 final_str = final_str +s1[i]+","
#             else:
#                 final_str = final_str +s1[i]
# #print(final_str)
# #print(st +" "+ str(r.text) + final_str)
# for line in r.text.split('='):
#     l2 = line.split('&')
#     if l2[0].startswith('o'):
#         str1 = l2[0]
#     elif l2[0].startswith('C'):
#         str2 = l2[0]
#
# str1 = str1 + "=" + '"' + str2 + '"'
# print(st +" "+ str1 + "," + final_str)