import re
import requests

URL_ONE = 'http://services.devhealtheintent.net/rc-dashboard-config-service/age_categories'
session = requests.Session()
data = {"Authorization":"OAuth oauth_token:ConsumerKey%3Dc0c11d7a-48c1-461d-8be9-56e9fb60b28f%26ExpiresOn%3D1522399881%26HMACSecrets%3DFTJ9EDMHu4pvPveucXDy1KsfKO_MJDu6vT1pcg8V5EUgWnjgO69Gc6y6XfdJebbFlV9xjBrUib5pYQNSlMq5LgwV-weUOQ_pcaTCGOBYvrtAWfHQlpV9ybqIhCmYJ5bdWzpyK9DWV7ciGyrggdGdVg%253D%253D%26KeysVersion%3Dfcecee6b-0c23-4df5-a332-799f9a515c16%26RSASHA1%3Df29DJad1c9mLvunI8xVMiHykKydEANGMh0n-9aQTtdIh7Wjfr_269ZClFUJQBXPkWt7gWW4NFDcHByI3iuxn3JbXEBiirZHWWTtNCrtP0gBeAV09MeUaBKCIxzZ3xWzVb9bY-ABrcjnglciRa4c1wtpwxadpzvYQZz9mfGyCNPxTVxRreV2k_56Ceqi7Q-ptoqkzvxn4vMwjieC99iBO5GdcJW5AnDqcktOxvJvD37dTau460WVAsHZrVMo2ZYXs7aNx7rDdTLBZEtHgMjqnca8B9mRd-thLNucWe8-S6TpEmby4Sl5FgE---oSonVJwXsos0_3vxhXL2foIHyBipA%253D%253D, oauth_consumer_key=c0c11d7a-48c1-461d-8be9-56e9fb60b28f, oauth_signature_method=PLAINTEXT, oauth_timestamp=1522396281, oauth_nonce=273488122989588, oauth_version=1.0, oauth_signature=Jjftdr7d_z7kjM1_GTXKskfQZs9aCD1l%267j3bl51rD0T2b6hjoEI1jaZhbgv2-ZD_", "Accept":"application/json", "Content-Type":"application/json"}
response = session.get(URL_ONE, data)
for line in response.text.split('\n'):
    print(line)

