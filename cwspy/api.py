import urllib.request
import json

from . import data
from . import helpers

BASE_URI = 'http://conworkshop.com/api/'

class API():

    def get_user(self, val):
        val = helpers.resolve(val)

        response = urllib.request.urlopen(''.join([BASE_URI, 'USER/', val])).read()
        response = json.loads(response)

        helpers.check_for_errors(response)

        response = response['out']
        attribs = {
            'uid': response['USER_ID'],
            'name': response['USER_NAME'],
            'gender': response['USER_GENDER'],
            'bio': response['USER_BIO'],
            'country': response['USER_COUNTRY'],
            'karma': response['KARMA'],
        }

        return data.defaultUser._replace(**attribs)

    def get_lang(self, val):

        response = urllib.request.urlopen(''.join([BASE_URI, 'LANG/', val])).read()
        response = json.loads(response)

        helpers.check_for_errors(response)

        response = response['out']
        attribs = {
            'code': response['CODE'],
            'name': response['NAME'],
            'native_name': response['NATIVE_NAME'],
            'ipa': response['IPA'],
            'lang_type': self.get_lang_type(response['TYPE']),
            'owners': response['OWNERS'],
            'overview': response['OVERVIEW'],
            'public': response['PUBLIC'],
            'status': self.get_lang_status(response['STATUS']),
            'registered': response['REGISTERED'],
            'word_count': response['WORD_COUNT'],
            'karma': response['KARMA']
        }

        return data.defaultLanguage._replace(**attribs)

    def get_lang_type(self, val):

        response = urllib.request.urlopen(''.join([BASE_URI, 'LANG/TYPE/', val])).read()
        response = json.loads(response)

        helpers.check_for_errors(response)

        response = response['out']
        attribs = {
            'code': response['TYPE'].upper(),
            'desc': response['DESC']
        }

        return data.defaultType._replace(**attribs)

    def get_lang_status(self, val):

        response = urllib.request.urlopen(''.join([BASE_URI, 'LANG/STATUS/', val])).read()
        response = json.loads(response)

        helpers.check_for_errors(response)

        response = response['out']
        attribs = {
            'code': response['STATUS'].upper(),
            'desc': response['DESC']
        }

        return data.defaultStatus._replace(**attribs)
