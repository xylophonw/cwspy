import requests

import errors
import helpers
import data

BASE_URI = 'http://conworkshop.com/api/'

class API():

    def get_user(self, val):
        val = helpers.resolve(val)

        response = requests.get(BASE_URI + 'USER/' + val).json()

        helpers.check_for_errors(response)

        response = response['out']
        attribs = {
            'user_id': response['USER_ID'],
            'name': response['USER_NAME'],
            'gender': response['USER_GENDER'],
            'bio': response['USER_BIO'],
            'country': response['USER_COUNTRY'],
            'karma': response['KARMA'],
        }

        return data.User(**attribs)

    def get_lang(self, val):

        response = requests.get(BASE_URI + 'LANG/' + val).json()

        helpers.check_for_errors(response)

        response = response['out']
        attribs = {
            'code': response['CODE'],
            'name': response['NAME'],
            'native_name': response['NATIVE_NAME'],
            "ipa": response["IPA"],
            'lang_type': self.get_lang_type(response['TYPE']),
            'owners': response['OWNERS'],
            'overview': response['OVERVIEW'],
            'public': response['PUBLIC'],
            'status': self.get_lang_status(response['STATUS']),
            'registered': response['REGISTERED'],
            'word_count': response['WORD_COUNT'],
            'karma': response['KARMA']
        }

        return data.Language(**attribs)

    def get_lang_type(self, val):

        response = requests.get(BASE_URI + 'LANG/TYPE/' + val).json()

        helpers.check_for_errors(response)

        response = response['out']
        attribs = {
            'code': response['TYPE'].upper(),
            'desc': response['DESC']
        }

        return data.Language.Type(**attribs)

    def get_lang_status(self, val):

        response = requests.get(BASE_URI + 'LANG/STATUS/' + val).json()

        helpers.check_for_errors(response)

        response = response['out']
        attribs = {
            'code': response['STATUS'].upper(),
            'desc': response['DESC']
        }

        return data.Language.Status(**attribs)
