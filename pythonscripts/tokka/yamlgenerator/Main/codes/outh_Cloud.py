# -*- coding: utf-8 -*-

from functools import wraps
import time

from django.conf import settings
from django.conf.urls import *
#from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required
from django.urls import *
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import *
#from axiom_requests_oauth.clients import TwoLeggedOAuth1
from urllib.parse import parse_qs
from urllib.parse import unquote

from cloud_status_dashboard.views import LogoutView, IndexView, TopicView, EventView, LoginView, PreferencesView, RedirectView

from cloud_status_dashboard.api_urls import urlpatterns as api_urls
from cloud_status_dashboard.admin import csd_admin_site

import base64
from base64 import urlsafe_b64decode, urlsafe_b64encode, b64encode, b64decode
import requests
from M2Crypto import BIO, RSA, EVP

from dajaxice.core import dajaxice_config

def oauth_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):

        def strip_quotes(string):
            if string.startswith('"'):
                string = string[1:]
            if string.endswith('"'):
                string = string[:len(string) - 1]

            return string

        auth = request.environ['HTTP_AUTHORIZATION']

        if auth.startswith("OAuth "):
            auth = auth[6:]

        auth_dict = {}
        auth_list = auth.split(", ")
        for auth_item in auth_list:
            name,val = auth_item.split("=")
            auth_dict[name] = strip_quotes(val)

        # If we do not have a token raise a 401
        if auth_dict['oauth_token'] is None:
            response = HttpResponse("Invalid / expired Token")
            response.status_code = 401
            return response

        #Validate the token is a syntactically valid, form-encoded data set
        oauth_token = auth_dict['oauth_token']

        oauth_token = unquote(oauth_token)
        token_data = parse_qs(oauth_token)

        if token_data['ConsumerKey'][0] is None or token_data['ExpiresOn'][0] is None or token_data['KeysVersion'][0] is None or token_data['RSASHA1'][0] is None or token_data['HMACSecrets'][0] is None:
            response = HttpResponse("Invalid content type")
            response.status_code = 401
            return response

        request_consumer_key = auth_dict['oauth_consumer_key']

        #validate that the token's consumer key matches the consumer key specified in the request
        if token_data['ConsumerKey'][0] != request_consumer_key:
            response = HttpResponse("Invalid consumer key")
            response.status_code = 401
            return response

        #validate that the token has not expired as indicated by the ExpiresOn parameter
        #(expire time of the token in seconds since Jan 1, 1970 00:00:00 GMT)

        expires_on = time.gmtime(int(token_data['ExpiresOn'][0]))

        if expires_on < time.gmtime():
            response = HttpResponse("Expired token")
            response.status_code = 401
            return response

        key_url = settings.CERNER_CARE_OAUTH1_ACCESS_KEY_URL.format(key=token_data['KeysVersion'][0])
        authbody = TwoLeggedOAuth1(settings.CERNER_CARE_OAUTH1_ACCESS_TOKEN_URL, settings.CERNER_CARE_OAUTH1_CLIENT_KEY, settings.CERNER_CARE_OAUTH1_CLIENT_SECRET)

        # Validate that the token ends with RSASHA1 value that is encoded properly
        begin_token, rsasha1_value = oauth_token.split('&RSASHA1=')

        if rsasha1_value.count('&') > 0:
            response = HttpResponse("Expired token")
            response.status_code = 401
            return response

        name_url = settings.CERNER_CARE_OAUTH1_CLIENT_NAME_URL.format(accountid=request_consumer_key)

        name_response = requests.get(name_url, auth=authbody, headers={'Accept': 'application/json'})
        client_mnemonic = name_response.json().get('client', None).get('mnemonic', None)

        request.META['CLIENT_MNEMONIC'] = client_mnemonic


        # Verify the RSASHA1 value as the signature of the rest of the token

        # Get the secret and public key to verify the authenticity of the access_token
        key_response = requests.get(key_url, auth=authbody)

        aes_secret_key = key_response.json().get('aesKey', None).get('secretKey', None)
        rsa_public_key = key_response.json().get('rsaKey', None).get('publicKey', None)

        newlined_added_rsa_public_key = []
        rsa_letter_count = 1

        for i in rsa_public_key:
            newlined_added_rsa_public_key.append(i)

            if rsa_letter_count % 75 == 0:
                newlined_added_rsa_public_key.append('\n')

            rsa_letter_count += 1

        newline_rsa_public_key = "".join(newlined_added_rsa_public_key)

        pem = "-----BEGIN PUBLIC KEY-----\n{0}\n-----END PUBLIC KEY-----".format(newline_rsa_public_key)

        bio = BIO.MemoryBuffer(pem)
        rsa = RSA.load_pub_key_bio(bio)

        pubkey = EVP.PKey()
        pubkey.assign_rsa(rsa)

        pubkey.verify_init()

        pubkey.verify_update(begin_token)

        if pubkey.verify_final(urlsafe_b64decode(token_data['RSASHA1'][0])) != 1:
            response = HttpResponse("Invalid signature")
            response.status_code = 401
            return response

        #Decrypt the HMACSecrets parameter to obtain the secrets used to sign the request
        secrets = AESEncryptionService().decrypt(urlsafe_b64decode(aes_secret_key.encode('ascii')), urlsafe_b64decode(token_data['HMACSecrets'][0]))
        discrete_secrets = parse_qs(secrets[16:])

        #Using the decrypted secrets, validate the signature on the request
        signature = unquote(auth_dict['oauth_signature'])

        if signature != (discrete_secrets['ConsumerSecret'][0] + '&' + discrete_secrets['TokenSecret'][0]):
            response = HttpResponse("Invalid signature")
            response.status_code = 401
            return response

        return view_func(request, *args, **kwargs)

    return _wrapped_view

class AESEncryptionService(object):
    def encrypt(self, key, msg):
        return self.__cipher(key, msg, 1)

    def decrypt(self, key, msg):
            decrypted = self.__cipher(key, msg, 0)
            return decrypted

    def __cipher(self, key, msg, op):
        iv = '\0' * 16
        iv.encode('ascii')
        cipher = EVP.Cipher(alg='aes_128_cbc', key=key, iv=iv, op=op)
        v = cipher.update(msg)
        v = v + cipher.final()
        del cipher
        return v

def perm_required(f):
    @wraps(f)
    @permission_required('whitelisted')
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

# Put permissions required on admin site
admin_urls = include(csd_admin_site.urls)
for url_pattern in admin_urls[0]:
    if isinstance(url_pattern, RegexURLResolver):
        for pattern in url_pattern.url_patterns:
            pattern._callback = perm_required(pattern._callback)
    else:
        url_pattern._callback = perm_required(url_pattern._callback)

# Put OAuth around api urls
service_api_urls = include(api_urls)
for url_pattern in service_api_urls[0]:
    url_pattern._callback = oauth_required(url_pattern._callback)

urlpatterns = patterns('',
    url(r'^login', RedirectView.as_view(), name='login'),
    url(r'^topics/?$', RedirectView.as_view(), name='index'),
    url(r'^preferences/?$', RedirectView.as_view(), name='preferences'),
    url(r'^about/?$', RedirectView.as_view(), name='about'),
    url(r'^$', redirect_to, {'url': reverse_lazy('index')}),
    url(r'^topics/(?P<slug>[-\w]+)/?$', RedirectView.as_view(), name='topic'),
    url(r'^events/(?P<slug>[-\w]+)/?$', RedirectView.as_view(), name='events'),
    url(r'^admin/', include(csd_admin_site.urls)),
    url(r'^auth/', include('social_auth.urls')),
    url(r'^auth/logout', LogoutView.as_view(), name='logout'),
    url(r'^api/?$', redirect_to,
        {'url': reverse_lazy(
            'redirect',
            kwargs={'version': '1'})
        }),
)

urlpatterns += patterns('',
    url(r'', redirect_to, {'url': reverse_lazy('redirect')}),
)

# We serve our own static because we don't care
if settings.DEPLOY_MODE in ('dev', 'sandbox', 'prod'):
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )