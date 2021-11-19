# -*- coding: utf-8 -*-

"""
firstlanguage

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from firstlanguage_python.api_helper import APIHelper
from firstlanguage_python.configuration import Server
from firstlanguage_python.controllers.base_controller import BaseController 
from firstlanguage_python.http.auth.custom_header_auth import CustomHeaderAuth
from firstlanguage_python.models.responseclassify import Responseclassify
from firstlanguage_python.models.api_qa_response import ApiQaResponse
from firstlanguage_python.models.api_ner_response import ApiNerResponse
from firstlanguage_python.exceptions.errors_exception import ErrorsException
from firstlanguage_python.exceptions.api_classify_426_error_exception import ApiClassify426ErrorException
from firstlanguage_python.exceptions.m_426_error_exception import M426ErrorException


class AdvancedAPIsController(BaseController):

    """A Controller to access Endpoints in the firstlanguage API."""

    def __init__(self, config, call_back=None):
        super(AdvancedAPIsController, self).__init__(config, call_back)

    def get_classification(self,
                           body):
        """Does a POST request to /api/classify.

        # Stemmer : Defintion and it's usage
        # Languages covered:

        Args:
            body (object): Add a JSON Input as per the schema defined below

        Returns:
            Responseclassify: Response from the API. Classifies labels.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/classify'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise ErrorsException('Error output', _response)
        elif _response.status_code == 426:
            raise ApiClassify426ErrorException('Please use HTTPS protocol', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, Responseclassify.from_dictionary)

        return decoded

    def get_qa(self,
               body=None):
        """Does a POST request to /api/qa.

        # Stemmer : Defintion and it's usage
        # Languages covered:

        Args:
            body (object, optional): Add a JSON Input as per the schema
                defined below

        Returns:
            ApiQaResponse: Response from the API. Answer for the question
                posted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/qa'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise ErrorsException('Bad Request', _response)
        elif _response.status_code == 426:
            raise M426ErrorException('Please use HTTPS protocol', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, ApiQaResponse.from_dictionary)

        return decoded

    def get_ner(self,
                body=None):
        """Does a POST request to /api/ner.

        # Stemmer : Defintion and it's usage
        # Languages covered:

        Args:
            body (object, optional): Add a JSON Input as per the schema
                defined below

        Returns:
            list of ApiNerResponse: Response from the API. Array of Named
                Entites marked from the input given.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/ner'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise ErrorsException('Bad Request', _response)
        elif _response.status_code == 426:
            raise M426ErrorException('Please use HTTPS protocol', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, ApiNerResponse.from_dictionary)

        return decoded
