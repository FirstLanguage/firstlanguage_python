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


class Input10(object):

    """Implementation of the 'Input10' model.

    TODO: type model description here.

    Attributes:
        question (string): Question to be answered from the context loaded in
            memory
        lang (string): Language of the question

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "question": 'question',
        "lang": 'lang'
    }

    def __init__(self,
                 question=None,
                 lang=None):
        """Constructor for the Input10 class"""

        # Initialize members of the class
        self.question = question
        self.lang = lang

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
        question = dictionary.get('question')
        lang = dictionary.get('lang')

        # Return an object of this model
        return cls(question,
                   lang)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)