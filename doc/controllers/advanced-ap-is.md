# Advanced AP Is

Advanced text processing APIs

```python
advanced_ap_is_controller = client.advanced_ap_is
```

## Class Name

`AdvancedAPIsController`

## Methods

* [Get Classification](/doc/controllers/advanced-ap-is.md#get-classification)
* [Get QA](/doc/controllers/advanced-ap-is.md#get-qa)
* [Get NER](/doc/controllers/advanced-ap-is.md#get-ner)


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

[`Responseclassify`](/doc/models/responseclassify.md)

## Example Usage

```python
body = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = advanced_ap_is_controller.get_classification(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiClassify426ErrorException`](/doc/models/api-classify-426-error-exception.md) |


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

[`ApiQaResponse`](/doc/models/api-qa-response.md)

## Example Usage

```python
result = advanced_ap_is_controller.get_qa()
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
| 400 | Bad Request | [`ErrorsException`](/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](/doc/models/m426-error-exception.md) |


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

[`List of ApiNerResponse`](/doc/models/api-ner-response.md)

## Example Usage

```python
result = advanced_ap_is_controller.get_ner()
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
| 400 | Bad Request | [`ErrorsException`](/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](/doc/models/m426-error-exception.md) |

