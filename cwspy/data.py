from datetime import datetime
from collections import namedtuple

BASE_URL = 'http://conworkshop.com/'

class User(namedtuple('User', 'uid name gender bio country karma')):
    @property
    def link(self):
        '''Return a URL in a string to the user's profile page on CWS.'''
        return ''.join([BASE_URL, 'view_profile.php?m=', self.uid])

    @property
    def avatar(self):
        '''Return a URL in a string to the user's avatar image on CWS.'''
        return ''.join([BASE_URL, 'ava/', self.uid, '.png'])

defaultUser = User('', '', 'Other', '', 'Unknown', [0,0])

Type = namedtuple('Type', 'code desc')
defaultType = Type('', '')

Status = namedtuple('Status', 'code desc')
defaultStatus = Status('', '')

class Language(namedtuple('Language', ['code', 'name', 'native_name', 'ipa',
                                       'lang_type', 'owners', 'overview', 'public',
                                       'status', 'registered', 'word_count', 'karma'])):
    @property
    def link(self):
        '''Return a URL in a string to the language's page on CWS.'''
        return ''.join([BASE_URL, 'view_language.php?l=', self.code])

    @property
    def flag(self):
        '''Return a URL in a string to the language's flag image on CWS.'''
        return ''.join([BASE_URL, 'img/flags/', self.code, '.png'])

defaultLanguage = Language('', '', '', '', defaultType, [], '', True,
                           defaultStatus, datetime.now(), 0, [0,0])
