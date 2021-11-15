# Basic AP Is

Basic NLP text processing APIs

```python
basic_ap_is_controller = client.basic_ap_is
```

## Class Name

`BasicAPIsController`

## Methods

* [Get Stemmer](/fl-python/doc/controllers/basic-ap-is.md#get-stemmer)
* [Get Lemma](/fl-python/doc/controllers/basic-ap-is.md#get-lemma)
* [Get Morph](/fl-python/doc/controllers/basic-ap-is.md#get-morph)
* [Get Postag](/fl-python/doc/controllers/basic-ap-is.md#get-postag)


# Get Stemmer

# Stemmer : Defintion and it's usage

A word takes different inflectional forms. For instance, the word, "Compute" can take the forms, "computing", "computation",  and "computerize". The NLP applications such as Search Engines and Information Extraction would want to store the base or stem of the word, i.e "Compute" instead of accomodating all its inflected forms. This will yield in dimensionality reduction and incerases the efficiency of the system. The stemmer cuts the prefix and suffix of a word.

# Languages covered:

Our stemmer works for the following  26 languages. Our stemmer works using the snowball stemmer algorithm which is also known as Porter 2 Stemming algorithm.

1. Tamil
2. Hindi
3. English
4. Arabic
5. Basque
6. Catalan
7. Danish
8. Dutch
9. Finnish
10. French
11. German
12. Greek
13. Hungarian
14. Indonesian
15. Irish
16. Italian
17. Lithuanian
18. Nepali
19. Norwegian
20. Portuguese
21. Romanian
22. Russian
23. Serbian
24. Spanish
25. Swedish
26. Turkish

```python
def get_stemmer(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Required | Add a JSON Input as per the schema defined below |

## Response Type

[`List of Responsestem`](/fl-python/doc/models/responsestem.md)

## Example Usage

```python
body = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = basic_ap_is_controller.get_stemmer(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](/fl-python/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiStemmer426ErrorException`](/fl-python/doc/models/api-stemmer-426-error-exception.md) |


# Get Lemma

# Stemmer : Defintion and it's usage

# Languages covered:

```python
def get_lemma(self,
             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Required | Add a JSON Input as per the schema defined below |

## Response Type

[`List of Responselemma`](/fl-python/doc/models/responselemma.md)

## Example Usage

```python
body = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = basic_ap_is_controller.get_lemma(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](/fl-python/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiLemmatize426ErrorException`](/fl-python/doc/models/api-lemmatize-426-error-exception.md) |


# Get Morph

# Stemmer : Defintion and it's usage

# Languages covered:

```python
def get_morph(self,
             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Required | Add a JSON Input as per the schema defined below |

## Response Type

[`Responsemorph`](/fl-python/doc/models/responsemorph.md)

## Example Usage

```python
body = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = basic_ap_is_controller.get_morph(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](/fl-python/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiMorph426ErrorException`](/fl-python/doc/models/api-morph-426-error-exception.md) |


# Get Postag

**So, What is a POS Tagger?**

Parts Of Speech Tagger, which is shortly known as POS Tagger is a software that automatically finds the word classes, when a text input is given. The text input can be a word, a sentence or a set of sentences. The word classes are the grammatical categories such as, Noun, Verb, Adverb etc. These category assigned to each word is a tag. A set of tags, each indicating a grammatical category is called, "tagsets". POS tagging is a mandatory pre processing for most of the Natural Language Processing Applications such as, Information Extraction, Information Retreival systems and Summary generation systems.

**Is POS Tagger, a language-independent software?**

No. A POS Tagger is a language-dependent software as the grammar rules will differ for every language. For instance, A word ending with "ing" might indicate a Verb" in English but this will not be applicable for other languages.

**For what languages, our  POS Tagger API will work?**

At present, our POS Tagger API works for English and Tami Languages. Soon we will extend the APIs to accomodate more languages.

**How Precise are our POS Tagger API?**

will update accuracy metrics soon .....

```python
def get_postag(self,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Required | Add a JSON Input as per the schema defined below |

## Response Type

[`List of Responsepo`](/fl-python/doc/models/responsepo.md)

## Example Usage

```python
body = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = basic_ap_is_controller.get_postag(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](/fl-python/doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiPostag426ErrorException`](/fl-python/doc/models/api-postag-426-error-exception.md) |

