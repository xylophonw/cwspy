from datetime import datetime

BASE_URL = "http://conworkshop.com/"
BASE_FLAG_URL = "http://conworkshop.com/img/flags/"
BASE_AVA_URL = "http://conworkshop.com/ava/"


class User():
    """A class representing a user on CWS."""

    def __init__(self, user_id='', name='', gender='Other', bio='',
                 country='Unknown', karma=[0,0]):
        """Make a new instance of User.

        Arguments:
        user_id - the ID used by CWS to identify users (defaults to '')
        name - the user's display name (defaults to '')
        gender - the user's selected gender, one of 'Male', 'Female', 'Cyborg',
        or 'Other' (defaults to 'Other')
        bio - the user's about text (defaults to '')
        country - the user's selected country (defaults to 'Unknown')
        karma - the user's upvotes and downvotes (defaults to [0,0])
        """

        self.id = user_id
        self.name = name
        self.gender = gender
        self.bio = bio
        self.country = country
        self.karma = karma

    def mk_link(self):
        """Return a URL in a string to the user's profile page on CWS."""
        return BASE_URL + "view_profile.php?m=" + self.id

    def mk_ava_link(self):
        """Return a URL in a string to the user's avatar image on CWS."""
        return BASE_AVA_URL + self.id + ".png"

class Language():
    """A class representing a language on CWS."""

    class Type():
        """A class representing the language's type, e.g. a priori, a posteriori."""

        def __init__(self, code='', desc=''):
            """Make a new language type object.

            Arguments:
            code - an abbreviation of the type used for identification
            desc - a human readable name for the type"""

            self.code = code
            self.desc = desc

    class Status():
        """A class representing the language's status, e.g. new, functional."""

        def __init__(self, code='', desc=''):
            """Make a new language status object.

            Arguments:
            code - an abbreviation of the status used for identification
            desc - a human readable name for the status"""

            self.code = code
            self.desc = desc


    def __init__(self, code='', name='', native_name='', ipa='',
                 lang_type=None, owners=[], overview='', public=True,
                 status=None, registered=datetime.now(), word_count=0,
                 karma=[0,0]):
        """Make a new instance of Language.

        Arguments:
        code - a three digit A-Z code used to identify the language (defaults to '')
        name - the language's English name (defaults to '')
        native_name - the language's name, in the language (defaults to '')
        ipa - the IPA pronunciation of the native name (defaults to '')
        lang_type - an instance of the Type class (defaults to None)
        owners - a list of the user IDs of the language owners (defaults to [])
        overview - the language's description (defaults to '')
        public - whether the language's dictionary is publically visible (defaults to True)
        status - an instance of the Status class (defaults to None)
        registered - i have no idea what the format for this is (defaults to datetime.now())
        word_count - the number of words in the language (defaults to 0)
        karma - the language's upvotes and downvotes (defaults to [0,0])
        """

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


    def mk_link(self):
        """Return a URL in a string to the language's page on CWS."""
        return BASE_URL + "view_language.php?l=" + self.code

    def mk_flag_link(self):
        """Return a URL in a string to the language's flag image on CWS."""
        return BASE_FLAG_URL + self.code + ".png"
