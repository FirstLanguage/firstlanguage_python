# -*- coding: utf-8 -*-
import random
"""
firstlanguage

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]


class CustomHeaderAuth:

    @staticmethod
    def apply(config, http_request):
        """ Add custom authentication to the request.

        Args:
            config (Configuration): The Configuration object which holds the
                authentication information.
            http_request (HttpRequest): The HttpRequest object to which
                authentication will be added.

        """
        #Pick a random user agent
        user_agent = random.choice(user_agent_list)
        http_request.add_header("apikey", config.apikey)
        http_request.add_header("User-Agent", user_agent)
        http_request.add_header("Accept", "application/json")
        http_request.add_header("Accept-Encoding", "gzip, deflate")