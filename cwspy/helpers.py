import re

from . import errors

def resolve(val):
    id_regex = re.compile('\A(S?\d+)\Z')
    return val if id_regex.match(val) else "@" + str(val)

def check_for_errors(response):
    if response['err_idx'] > 0:
        raise errors.APIError(response['err_msg'])
