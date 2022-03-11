# -*- coding: utf-8 -*-

"""
firstlanguage_python

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from firstlanguage_python.api_helper import APIHelper
from firstlanguage_python.configuration import Server
from firstlanguage_python.controllers.base_controller import BaseController
from firstlanguage_python.models.api_question_response import ApiQuestionResponse
from firstlanguage_python.exceptions.errors_exception import ErrorsException
from firstlanguage_python.exceptions.m_426_error_exception import M426ErrorException
from firstlanguage_python.exceptions.api_exception import APIException


class EnterpriseOnlyController(BaseController):

    """A Controller to access Endpoints in the firstlanguage_python API."""
    def __init__(self, config, auth_managers, call_back=None):
        super(EnterpriseOnlyController, self).__init__(config, auth_managers, call_back)

    def get_qa_enterprise(self,
                          body=None):
        """Does a POST request to /api/question.

        A Question Answering System retrieves the answer relevant to the
        question given by the user. A question answering system can be used
        for building a text based chatbots, search engines etc. Our question
        answering system  is mutilingual and supports 100 + languages. Please
        use ISO 639-2 2 digit language code  to get results. For example, use
        'en' for English, 'ta' for Tamil, 'hi' for Hindi, 'fr' for French
        etc.
        For ISO code reference, please check the link
        https://www.loc.gov/standards/iso639-2/php/code_list.php
        For enterprise, the context for the questions will be stored in
        memory. The context can be read from wide range of file and any number
        of files.

        Args:
            body (ApiQuestionRequest, optional): Add a JSON Input as per the
                schema defined below

        Returns:
            ApiQuestionResponse: Response from the API. Answer for the
                question posted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/question'
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
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise ErrorsException('Bad Request', _response)
        elif _response.status_code == 426:
            raise M426ErrorException('Please use HTTPS protocol', _response)
        elif _response.status_code == 429:
            raise APIException('Too Many Requests', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, ApiQuestionResponse.from_dictionary)

        return decoded