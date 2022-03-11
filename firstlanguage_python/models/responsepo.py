# -*- coding: utf-8 -*-

"""
firstlanguage_python

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import os
from firstlanguage_python.utilities.schema_validator_wrapper import SchemaValidatorWrapper
from jsonschema import ValidationError
from firstlanguage_python.api_helper import APIHelper


class Responsepo(object):

    """Implementation of the 'responsepo' model.

    TODO: type model description here.

    Attributes:
        original_text (string): TODO: type description here.
        postag (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "original_text": 'originalText',
        "postag": 'postag'
    }

    def __init__(self,
                 original_text=None,
                 postag=None):
        """Constructor for the Responsepo class"""

        # Initialize members of the class
        self.original_text = original_text
        self.postag = postag

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
        original_text = dictionary.get('originalText')
        postag = dictionary.get('postag')

        # Return an object of this model
        return cls(original_text,
                   postag)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
