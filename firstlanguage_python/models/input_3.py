# -*- coding: utf-8 -*-

"""
firstlanguage

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Input3(object):

    """Implementation of the 'Input3' model.

    TODO: type model description here.

    Attributes:
        url (string): URL where the content is hosted.
        lang (string): Allowed language code. Refer Allowed languages
            section.
        content_type (string): Allowed values or html or text. If html is
            specified all html tags and special characters will be stripped
            before processing.
        labels (list of object): Labels to classify

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url": 'url',
        "lang": 'lang',
        "content_type": 'contentType',
        "labels": 'labels'
    }

    def __init__(self,
                 url=None,
                 lang=None,
                 content_type=None,
                 labels=None):
        """Constructor for the Input3 class"""

        # Initialize members of the class
        self.url = url
        self.lang = lang
        self.content_type = content_type
        self.labels = labels

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        url = dictionary.get('url')
        lang = dictionary.get('lang')
        content_type = dictionary.get('contentType')
        labels = dictionary.get('labels')

        # Return an object of this model
        return cls(url,
                   lang,
                   content_type,
                   labels)