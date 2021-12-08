from helpers.http_helper import HttpHelper
import time


class ZsTalker(object):
    """
    Zscaler API talker
    Documentation: https://help.zscaler.com/zia/api
    """

    def __init__(self, cloud_name):
        self.base_uri = f'https://{cloud_name}/api/v1'
        self.hp_http = HttpHelper(host=self.base_uri, verify=True)
        self.jsessionid = None
        self.version = '1.2'

    def _obfuscateApiKey(self, seed):
        """
        Internal method to Obfuscate the API key
        :param seed: API key
        :return: timestamp,obfuscated key
        """
        now = int(time.time() * 1000)
        n = str(now)[-6:]
        r = str(int(n) >> 1).zfill(6)
        key = ""
        for i in range(0, len(str(n)), 1):
            key += seed[int(str(n)[i])]
        for j in range(0, len(str(r)), 1):
            key += seed[int(str(r)[j]) + 2]
        return now, key

    def authenticate(self, apikey, username, password):
        """
        Method to authenticate.
        :param apikey: type string: API key
        :param username: type string: A string that contains the email ID of the API admin
        :param password:  type string: A string that contains the password for the API admin
        :return:  JSESSIONID. This cookie expires by default 30 minutes from last request
        """
        timestamp, key = self._obfuscateApiKey(apikey)

        payload = {
            "apiKey": key,
            "username": username,
            "password": password,
            "timestamp": timestamp
        }
        url = '/authenticatedSession'
        response = self.hp_http.post_call(url=url, payload=payload)
        self.jsessionid = response.cookies['JSESSIONID']

    def list_url_categories(self, custom=False):
        """
        Gets information about all or custom URL categories
        :param custom: Boolean, if True it will return custom categories only
        :return: json
        """

        if custom:
            url = '/urlCategories?customOnly=true'
        else:
            url = '/urlCategories'
        response = self.hp_http.get_call(url, cookies={'JSESSIONID': self.jsessionid}, error_handling=True)
        return response.json()

    def update_call(self, url, payload):
        """
        Generic PUT call. This call will overwrite all the configuration with the new payload
        :param url: url of Zscaler API call
        :param payload: type json. Payload
        """
        response = self.hp_http.put_call(url, payload=payload, cookies={'JSESSIONID': self.jsessionid},
                                         error_handling=True)
        return response.json()
