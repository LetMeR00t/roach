# Copyright (C) 2018 Jurriaan Bremer.
# Copyright (C) 2018 Hatching B.V.
# This file is part of Roach - https://github.com/jbremer/roach.
# See the file 'docs/LICENSE.txt' for copying permission.

import re

# https://stackoverflow.com/a/52082649
DOMAIN_REGEX = (
    "^(?=.{1,255}$)(?!-)[A-Za-z0-9\-]{1,63}(\.[A-Za-z0-9\-]{1,63})*\.?(?<!-)$"
)

# The regex as we use it in Cuckoo.
URL_REGEX = (
    # HTTP/HTTPS.
    "(https?:\\/\\/)"
    "((["
    # IP address.
    "(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\."
    "(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\."
    "(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\."
    "(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])]|"
    # Or domain name.
    "[a-zA-Z0-9\\.-]+)"
    # Optional port.
    "(\\:\\d+)?"
    # URI.
    "(/[\\(\\)a-zA-Z0-9_:%?=/\\.-]*)?"
)

class Verify(object):
    @staticmethod
    def ascii(s):
        return bool(re.match("^[\x20-\x7f]*$", s, re.DOTALL))

    @staticmethod
    def domain(s):
        return bool(re.match(DOMAIN_REGEX, s, re.DOTALL))

    @staticmethod
    def url(s):
        return bool(re.match(URL_REGEX, s, re.DOTALL))
