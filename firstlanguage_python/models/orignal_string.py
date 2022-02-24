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


class OrignalString(object):

    """Implementation of the 'OrignalString' model.

    TODO: type model description here.

    Attributes:
        morph_attr (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "morph_attr": 'morph_attr'
    }

    def __init__(self,
                 morph_attr=None):
        """Constructor for the OrignalString class"""

        # Initialize members of the class
        self.morph_attr = morph_attr

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
        morph_attr = dictionary.get('morph_attr')

        # Return an object of this model
        return cls(morph_attr)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
