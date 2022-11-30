import re

class Helper():

    @staticmethod
    def validate_url(url):
        url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
        return bool(re.match(url_pattern, url))

    @staticmethod
    def validate_port(port):
        if(port != 80):
            return False
        else:
            return True