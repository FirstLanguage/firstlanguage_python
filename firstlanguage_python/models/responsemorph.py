# -*- coding: utf-8 -*-

"""
firstlanguage

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from firstlanguage_python.models.orignal_string import OrignalString


class Responsemorph(object):

    """Implementation of the 'responsemorph' model.

    TODO: type model description here.

    Attributes:
        orignal_string (OrignalString): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "orignal_string": 'orignalString'
    }

    def __init__(self,
                 orignal_string=None):
        """Constructor for the Responsemorph class"""

        # Initialize members of the class
        self.orignal_string = orignal_string

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
        orignal_string = OrignalString.from_dictionary(dictionary.get('orignalString')) if dictionary.get('orignalString') else None

        # Return an object of this model
        return cls(orignal_string)
