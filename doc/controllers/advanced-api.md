# Advanced APIs

Advanced text processing APIs

```python
advanced_api_controller = client.advanced_api
```

## Class Name

`AdvancedAPIsController`

## Methods

* [Get Classification](/fl-python/doc/controllers/advanced-api.md#get-classification)
* [Get QA](/fl-python/doc/controllers/advanced-api.md#get-qa)
* [Get NER](/fl-python/doc/controllers/advanced-api.md#get-ner)


# Get Classification

# Stemmer : Defintion and it's usage

# Languages covered:

```python
def get_classification(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Required | Add a JSON Input as per the schema defined below |

## Response Type

[`Responseclassify`](/fl-python/doc/models/responseclassify.md)

## Example Usage

```python
body = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = advanced_api_controller.get_classification(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](/fl-python/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiClassify426ErrorException`](/fl-python/doc/models/api-classify-426-error-exception.md) |


# Get QA

# Stemmer : Defintion and it's usage

# Languages covered:

```python
def get_qa(self,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Optional | Add a JSON Input as per the schema defined below |

## Response Type

[`ApiQaResponse`](/fl-python/doc/models/api-qa-response.md)

## Example Usage

```python
result = advanced_api_controller.get_qa()
```

## Example Response *(as JSON)*

```json
{
  "score": 0.028566665947437286,
  "start": 0,
  "end": 20,
  "answer": "உப்பு, புளி, மிளகாய்"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorsException`](/fl-python/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](/fl-python/doc/models/m426-error-exception.md) |


# Get NER

# Stemmer : Defintion and it's usage

# Languages covered:

```python
def get_ner(self,
           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Optional | Add a JSON Input as per the schema defined below |

## Response Type

[`List of ApiNerResponse`](/fl-python/doc/models/api-ner-response.md)

## Example Usage

```python
result = advanced_api_controller.get_ner()
```

## Example Response *(as JSON)*

```json
[
  {
    "entity_group": "PER",
    "word": "محمد",
    "start": "4",
    "end": "9"
  },
  {
    "entity_group": "LOC",
    "word": "برلين",
    "start": "18",
    "end": "24"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorsException`](/fl-python/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](/fl-python/doc/models/m426-error-exception.md) |

