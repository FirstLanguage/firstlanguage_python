# Enterprise Only

```python
enterprise_only_controller = client.enterprise_only
```

## Class Name

`EnterpriseOnlyController`


# Get QA Enterprise

# QA : Defintion and it's usage

A Question Answering System retrieves the answer relevant to the question given by the user. A question answering system can be used for building a text based chatbots, search engines etc. Our question answering system  is mutilingual and supports 100 + languages. Please use ISO 639-2 2 digit language code  to get results. For example, use 'en' for English, 'ta' for Tamil, 'hi' for Hindi, 'fr' for French etc.

For ISO code reference, please check the link https://www.loc.gov/standards/iso639-2/php/code_list.php

```python
def get_qa_enterprise(self,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiQuestionRequest`](/doc/models/api-question-request.md) | Body, Optional | Add a JSON Input as per the schema defined below |

## Response Type

[`ApiQuestionResponse`](/doc/models/api-question-response.md)

## Example Usage

```python
body = ApiQuestionRequest()
body.input = Input10()
body.input.question = 'Who is father of Arya Stark?'
body.input.lang = 'en'

result = enterprise_only_controller.get_qa_enterprise(body)
```

## Example Response *(as JSON)*

```json
{
  "answer": "உப்பு, புளி, மிளகாய்"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorsException`](/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](/doc/models/m426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |

