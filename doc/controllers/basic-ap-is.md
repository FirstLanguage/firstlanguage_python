# Basic AP Is

```python
basic_ap_is_controller = client.basic_ap_is
```

## Class Name

`BasicAPIsController`

## Methods

* [Get Stemmer](../../doc/controllers/basic-ap-is.md#get-stemmer)
* [Get Lemma](../../doc/controllers/basic-ap-is.md#get-lemma)
* [Get Morph](../../doc/controllers/basic-ap-is.md#get-morph)
* [Get Postag](../../doc/controllers/basic-ap-is.md#get-postag)


# Get Stemmer

A word takes different inflectional forms. For instance, the word, "Compute" can take the forms, "computing", "computation",  and "computerize". The NLP applications such as Search Engines and Information Extraction would want to store the base or stem of the word, i.e "Compute" instead of accomodating all its inflected forms. This will yield in dimensionality reduction and incerases the efficiency of the system. The stemmer cuts the prefix and suffix of a word.

# Languages covered:

Our stemmer works for the following  26 languages.

| Languages    | ISO Code   |
|--------------|------------|
|  Arabic      |  ar        |
|  Catalan     |  ca        |
|  Danish      |  da        |
|  German      |  de        |
|  Greek       |  el        |
|  English     |  en        |
|  Spanish     |  es        |
|  Basque      |  eu        |
|  Finnish     |  fi        |
|  French      |  fr        |
|  Irish       |  ga        |
|  Hindi       |  hi        |
|  Hungarian   |  hu        |
|  Indonesian  |  id        |
|  Italian     |  it        |
|  Lithuanian  |  lt        |
|  Nepali      |  ne        |
|  Dutch       |  nl        |
|  Norwegian   |  no        |
|  Portuguese  |  pt        |
|  Romanian    |  ro        |
|  Russian     |  ru        |
|  Serbian     |  sr        |
|  Swedish     |  sv        |
|  Tamil       |  ta        |
|  Turkish     |  tr        |

```python
def get_stemmer(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`object`](../../$m/) | Body, Required | Add a JSON Input as per the schema defined below<br><br>**Size limit:**<br><br>1MB for both text and URL input<br><br>**URL Input:**<br><br>For URL, we now accept 4 contentTypes.<br><br>* html<br>* plaintext<br>* pdf<br>* docx<br><br>If you are providing Google drive or Google Spreadsheet url, ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Drive link:<br><br>https://drive.google.com/uc?id=idofthefile |

## Response Type

[`List of Responsestem`](../../doc/models/responsestem.md)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"input":{"text":"அவள் வேகமாக ஓடினாள்","lang":"ta"}}}')

result = basic_ap_is_controller.get_stemmer(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "originalText": "அவள்",
    "stem": "அவள்"
  },
  {
    "originalText": "வேகமாக",
    "stem": "வேகம்"
  },
  {
    "originalText": "ஓடினாள்",
    "stem": "ஓடி"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiStemmer426ErrorException`](../../doc/models/api-stemmer-426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |


# Get Lemma

Lemmatizer is similar to stemmer that gives the stemmed version of a word but lemmatizer differs from the stemmer in giving a meaningful stem or the lemma. For instance, for the word, "smiling", the stemmer would give, "smil", stemming the suffix, "ing" but the lemmatizer would give the meaningful stem, "smile". lemmatizers can be used in applications such as,  Machine Translation, Search Engines, Text Summarization etc.

# Languages covered:

| Languages          | ISO Code |
|--------------------|----------|
| Catalan            | ca       |
| Danish             | da       |
| Dutch              | nl       |
| English            | en       |
| French             | fr       |
| German             | de       |
| Greek              | el       |
| Italian            | it       |
| Lithuanian         | lt       |
| Macedonian         | mk       |
| Norwegian (Bokmål) | nb       |
| Polish             | pl       |
| Portuguese         | pt       |
| Romanian           | ro       |
| Russian            | ru       |
| Spanish            | es       |

```python
def get_lemma(self,
             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`object`](../../$m/) | Body, Required | Add a JSON Input as per the schema defined below<br><br>**Size limit:**<br><br>1MB for both text and URL input<br><br>**URL Input:**<br><br>For URL, we now accept 4 contentTypes.<br><br>* html<br>* plaintext<br>* pdf<br>* docx<br><br>If you are providing Google drive or Google Spreadsheet url, ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Drive link:<br><br>https://drive.google.com/uc?id=idofthefile |

## Response Type

[`List of Responselemma`](../../doc/models/responselemma.md)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"input":{"text":"Smiling makes everyone happy","lang":"en"}}}')

result = basic_ap_is_controller.get_lemma(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "originalText": "Smiling",
    "lemmatized": "smile"
  },
  {
    "originalText": "makes",
    "lemmatized": "make"
  },
  {
    "originalText": "everyone",
    "lemmatized": "everyone"
  },
  {
    "originalText": "happy",
    "lemmatized": "happy"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiLemmatize426ErrorException`](../../doc/models/api-lemmatize-426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |


# Get Morph

Morphological Analyzer analyzes how a word is formed. It breaks a word into smaller units called, "morphemes" and gives a clue on the pattern of words of a particular langauge.  It can be used for building applications such as,  Machine Translation, Text Summarization, Search systems etc.

# Languages covered:

| Languages          | ISO Code |
|--------------------|----------|
| Catalan            | ca       |
| Danish             | da       |
| Dutch              | nl       |
| English            | en       |
| French             | fr       |
| German             | de       |
| Greek              | el       |
| Italian            | it       |
| Japanese           | ja       |
| Lithuanian         | lt       |
| Macedonian         | mk       |
| Norwegian (Bokmål) | nb       |
| Polish             | pl       |
| Portuguese         | pt       |
| Russian            | ru       |
| Spanish            | es       |

```python
def get_morph(self,
             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`object`](../../$m/) | Body, Required | Add a JSON Input as per the schema defined below<br><br>**Size limit:**<br><br>1MB for both text and URL input<br><br>**URL Input:**<br><br>For URL, we now accept 4 contentTypes.<br><br>* html<br>* plaintext<br>* pdf<br>* docx<br><br>If you are providing Google drive or Google Spreadsheet url, ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Drive link:<br><br>https://drive.google.com/uc?id=idofthefile |

## Response Type

[`Responsemorph`](../../doc/models/responsemorph.md)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"input":{"text":"Let us begin the API development.","lang":"en"}}}')

result = basic_ap_is_controller.get_morph(body)
```

## Example Response *(as JSON)*

```json
{
  "Let": {
    "VerbForm": [
      "Inf"
    ],
    "Case": [
      "Acc"
    ],
    "Number": [
      "Sing"
    ],
    "Person": [
      "1"
    ],
    "PronType": [
      "Art"
    ],
    "Definite": [
      "Def"
    ],
    "NounType": [
      "Prop"
    ]
  },
  "us": {
    "VerbForm": [
      "Inf"
    ],
    "Case": [
      "Acc"
    ],
    "Number": [
      "Sing"
    ],
    "Person": [
      "1"
    ],
    "PronType": [
      "Art"
    ],
    "Definite": [
      "Def"
    ],
    "NounType": [
      "Prop"
    ]
  },
  "begin": {
    "VerbForm": [
      "Inf"
    ],
    "Case": [
      "Acc"
    ],
    "Number": [
      "Sing"
    ],
    "Person": [
      "1"
    ],
    "PronType": [
      "Art"
    ],
    "Definite": [
      "Def"
    ],
    "NounType": [
      "Prop"
    ]
  },
  "the": {
    "VerbForm": [
      "Inf"
    ],
    "Case": [
      "Acc"
    ],
    "Number": [
      "Sing"
    ],
    "Person": [
      "1"
    ],
    "PronType": [
      "Art"
    ],
    "Definite": [
      "Def"
    ],
    "NounType": [
      "Prop"
    ]
  },
  "API": {
    "VerbForm": [
      "Inf"
    ],
    "Case": [
      "Acc"
    ],
    "Number": [
      "Sing"
    ],
    "Person": [
      "1"
    ],
    "PronType": [
      "Art"
    ],
    "Definite": [
      "Def"
    ],
    "NounType": [
      "Prop"
    ]
  },
  "development": {
    "VerbForm": [
      "Inf"
    ],
    "Case": [
      "Acc"
    ],
    "Number": [
      "Sing"
    ],
    "Person": [
      "1"
    ],
    "PronType": [
      "Art"
    ],
    "Definite": [
      "Def"
    ],
    "NounType": [
      "Prop"
    ]
  },
  ".": {
    "VerbForm": [
      "Inf"
    ],
    "Case": [
      "Acc"
    ],
    "Number": [
      "Sing"
    ],
    "Person": [
      "1"
    ],
    "PronType": [
      "Art"
    ],
    "Definite": [
      "Def"
    ],
    "NounType": [
      "Prop"
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiMorph426ErrorException`](../../doc/models/api-morph-426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |


# Get Postag

Parts of Speech Tagger, which is shortly known as POS Tagger is a software that automatically finds the word classes, when a text input is given. The text input can be a word, a sentence or a set of sentences. The word classes are the grammatical categories such as, Noun, Verb, Adverb etc. The category assigned to each word is called as a tag. A set of tags, each indicating a grammatical category is called, "tagsets". POS tagging is a mandatory pre-processing for most of the Natural Language Processing Applications such as, Information Extraction, Information Retreival systems and Summary generation systems. A POS Tagger is a language-dependent software as the grammar rules will differ for every language. For instance, a word ending with "ing" might indicate a "Verb" in English but this will not be applicable for other languages.

# Languages covered:

| Languages          | ISO Code |
|--------------------|----------|
| Chinese            | zh       |
| Dutch              | nl       |
| English            | en       |
| German             | de       |
| Italian            | it       |
| Lithuanian         | lt       |
| Polish             | pl       |
| Romanian           | ro       |
| Tamil              | ta       |

```python
def get_postag(self,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`object`](../../$m/) | Body, Required | Add a JSON Input as per the schema defined below<br><br>**Size limit:**<br><br>1MB for both text and URL input<br><br>**URL Input:**<br><br>For URL, we now accept 4 contentTypes.<br><br>* html<br>* plaintext<br>* pdf<br>* docx<br><br>If you are providing Google drive or Google Spreadsheet url, ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Drive link:<br><br>https://drive.google.com/uc?id=idofthefile |

## Response Type

[`List of Responsepo`](../../doc/models/responsepo.md)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"input":{"text":"Let us begin the API development.","lang":"en"}}}')

result = basic_ap_is_controller.get_postag(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "originalText": "Let",
    "postag": "VERB"
  },
  {
    "originalText": "us",
    "postag": "PRON"
  },
  {
    "originalText": "begin",
    "postag": "VERB"
  },
  {
    "originalText": "the",
    "postag": "DET"
  },
  {
    "originalText": "API",
    "postag": "PROPN"
  },
  {
    "originalText": "development",
    "postag": "NOUN"
  },
  {
    "originalText": ".",
    "postag": "PUNCT"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiPostag426ErrorException`](../../doc/models/api-postag-426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |
