from datetime import datetime

BASE_URL = "http://conworkshop.com/"

class User():

    def __init__(self, user_id='', name='', gender='Other', bio='',
                 country='Unknown', karma=[0,0]):
        self.id = user_id
        self.name = name
        self.gender = gender
        self.bio = bio
        self.country = country
        self.karma = karma

    def generate_link(id):
        return BASE_URL + "view_profile.php?m=" + self.id

class Language():

    class Type():
        def __init__(self, code='', desc=''):
            self.code = code
            self.desc = desc

    class Status():
        def __init__(self, code='', desc=''):
            self.code = code
            self.desc = desc


    def __init__(self, code='', name='', native_name='', ipa='',
                 lang_type=None, owners=[], overview='', public=True,
                 status='', registered=datetime.now(), word_count=0,
                 karma=[0,0]):
        self.code = code
        self.name = name
        self.native_name = native_name
        self.ipa = ipa
        self.type = lang_type
        self.owners = owners
        self.overview = overview
        self.public = public
        self.status = status
        self.registered = registered
        self.word_count = word_count
        self.karma = karma


    def mk_link(id):
        return BASE_URL + "view_language.php?l=" + self.code
