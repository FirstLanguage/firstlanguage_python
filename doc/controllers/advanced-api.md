# Advanced APIs

Advanced text processing APIs

```python
advanced_api_controller = client.advanced_api
```

## Class Name

`AdvancedAPIsController`

## Methods

* [Get Classification](/firstlanguage_python/doc/controllers/advanced-api.html#get-classification)
* [Get QA](/firstlanguage_python/doc/controllers/advanced-api.html#get-qa)
* [Get NER](/firstlanguage_python/doc/controllers/advanced-api.html#get-ner)
* [Get Summary](/firstlanguage_python/doc/controllers/advanced-api.html#get-summary)
* [Get Translate](/firstlanguage_python/doc/controllers/advanced-api.html#get-translate)


# Get Classification

# Text Classification  : Defintion and it's usage

A text classifier identifies the categories of the text given as input. Classifying the texts is one of the powerful preprocessing technique in topic identification and sentiment classification (product reviews, movie reviews etc)and indexing the texts while building a search system.

# Languages covered:

| Languages  | ISO Code |
|------------|----------|
| Arabic     | ar       |
| Bulgarian  | bg       |
| Chinese    | zh       |
| English    | en       |
| French     | fr       |
| German     | de       |
| Greek      | el       |
| Hindi      | hi       |
| Russian    | ru       |
| Spanish    | es       |
| Swahili    | sw       |
| Thai       | th       |
| Turkish    | tr       |
| Urdu       | ur       |
| Vietnamese | vi       |

```python
def get_classification(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Required | Add a JSON Input as per the schema defined below |

## Response Type

[`Responseclassify`](/firstlanguage_python/doc/models/responseclassify.html)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"value":{"input":{"context":"context4","lang":"lang4","labels":[{"key1":"val1","key2":"val2"}]}}}')

result = advanced_api_controller.get_classification(body)
```

## Example Response *(as JSON)*

```json
{
  "labels": [
    "positive",
    "negative"
  ],
  "scores": [
    0.9966060519218445,
    0.0033939925488084555
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error output | [`ErrorsException`](/firstlanguage_python/doc/models/errors-exception.html) |
| 426 | Please use HTTPS protocol | [`ApiClassify426ErrorException`](/firstlanguage_python/doc/models/api-classify-426-error-exception.html) |
| 429 | Too Many Requests | `APIException` |


# Get QA

# QA : Defintion and it's usage

A Question Answering System retrieves the answer relevant to the question given by the user. A question answering system can be used for building a text based chatbots, search engines etc. Our question answering system  is mutilingual and supports 100 + languages. Please use ISO 639-2 2 digit language code  to get results. For example, use 'en' for English, 'ta' for Tamil, 'hi' for Hindi, 'fr' for French etc.

For ISO code reference, please check the link https://www.loc.gov/standards/iso639-2/php/code_list.php

```python
def get_qa(self,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Optional | Add a JSON Input as per the schema defined below |

## Response Type

[`ApiQaResponse`](/firstlanguage_python/doc/models/api-qa-response.html)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"value":{"input":{"question":"எவை மூன்றும் எப்போதும் ஒன்றாகவே இருக்கும்?","lang":"ta","context":"உப்பு, புளி, மிளகாய் மூன்றும் எப்போதும் ஒன்றாகவே இருக்கும். ஒருநாள், “குழம்பிற்கு யார் முக்கியம்? நீயா! நானா!” என்று சண்டை போட்டன. மூன்று பேரும் தனிதனியாகச் சென்று குழம்பில் சேரலாம் என்று முடிவு செய்தன. முதல் நாள், உப்பு மட்டும் குழம்பில் சேர்ந்து கொண்டது. “ஆ! ஒரே உப்பு! வாயில் வைக்க முடியவில்லை!” என்று எல்லோரும் கத்தினார்கள்"}}}')
result = advanced_api_controller.get_qa(body)
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
| 400 | Bad Request | [`ErrorsException`](/firstlanguage_python/doc/models/errors-exception.html) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](/firstlanguage_python/doc/models/m426-error-exception.html) |
| 429 | Too Many Requests | `APIException` |


# Get NER

# Named Entity Recognition : Defintion and it's usage

Named Entity Recognitiion  (NER) is extracting the specific Nouns such as, Person Names, Location names, Organization Names, Currency , Dates. It is a classification task. NER can be used as a sub-task in applications such as Search Systems, Chatbots, Question Answering systems, Text Summarization etc.

# Languages covered:

| Languages          | ISO Code |
|--------------------|----------|
| Arabic             | ar       |
| Chinese            | zh       |
| Dutch              | nl       |
| English            | en       |
| French             | fr       |
| German             | de       |
| Italian            | it       |
| Latvian            | lv       |
| Portuguese         | pt       |
| Spanish            | es       |

For other languages we cannot guarantee results but you can try with ISO code.
For ISO code reference, please check the link https://www.loc.gov/standards/iso639-2/php/code_list.php

```python
def get_ner(self,
           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Optional | Add a JSON Input as per the schema defined below |

## Response Type

[`List of ApiNerResponse`](/firstlanguage_python/doc/models/api-ner-response.html)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"value":{"input":{"text":"إسمي محمد وأسكن في برلين","lang":"ar"}}}')
result = advanced_api_controller.get_ner(body)
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
| 400 | Bad Request | [`ErrorsException`](/firstlanguage_python/doc/models/errors-exception.html) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](/firstlanguage_python/doc/models/m426-error-exception.html) |
| 429 | Too Many Requests | `APIException` |


# Get Summary

# Summarization : Defintion and it's usage

Summarization generates a crisp content of the large input text which is highly coherent.

| Languages               | ISO Code |
|-------------------------|----------|
| Amharic                 | am       |
| Arabic                  |  ar      |
| Azerbaijani             |  az      |
| Bengali                 |  bn      |
| Burmese                 |  my      |
| Chinese                 |  zh      |
| English                 |  en      |
| French                  |  fr      |
| Gaelic; Scottish Gaelic | gd       |
| Gujarati                |  gu      |
| Hausa                   |  ha      |
| Hindi                   |  hi      |
| Igbo                    |  ig      |
| Indonesian              |  id      |
| Japanese                |  ja      |
| Kirghiz; Kyrgyz         | ky       |
| Korean                  |  ko      |
| Marathi                 |  mr      |
| Nepali                  |  ne      |
| Oromo                   | om       |
| Persian                 | fa       |
| Portuguese              |  pt      |
| Punjabi                 |  pa      |
| Pushto; Pashto          | ps       |
| Rundi                   | rn       |
| Russian                 | ru       |
| Serbian                 |  sr      |
| Sinhala; Sinhalese      |  si      |
| Somali                  |  so      |
| Spanish; Castilian      |  es      |
| Swahili                 |  sw      |
| Tamil                   |  ta      |
| Telugu                  |  te      |
| Thai                    |  th      |
| Tigrinya                |  ti      |
| Turkish                 |  tr      |
| Ukrainian               |  uk      |
| Urdu                    |  ur      |
| Uzbek                   |  uz      |
| Vietnamese              |  vi      |
| Welsh                   |  cy      |
| Yoruba                  |  yo      |

```python
def get_summary(self,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Optional | Add a JSON Input as per the schema defined below |

## Response Type

[`ApiSummaryResponse`](/doc/models/api-summary-response.html)

## Example Usage

```python
body = jsonpickle.decode('{"input":{"text":"Videos that say approved vaccines are dangerous and cause autism, cancer or infertility are among those that will be taken down, the company said. The policy includes the termination of accounts of anti-vaccine influencers. Tech giants have been criticised for not doing more to counter false health information on their sites. In July, US President Joe Biden said social media platforms were largely responsible for people\'s scepticism in getting vaccinated by spreading misinformation, and appealed for them to address the issue. YouTube, which is owned by Google, said 130,000 videos were removed from its platform since last year, when it implemented a ban on content spreading misinformation about Covid vaccines. In a blog post, the company said it had seen false claims about Covid jabs spill over into misinformation about vaccines in general. The new policy covers long-approved vaccines, such as those against measles or hepatitis B. We\'re expanding our medical misinformation policies on YouTube with new guidelines on currently administered vaccines that are approved and confirmed to be safe and effective by local health authorities and the WHO, the post said, referring to the World Health Organization.","lang":"en"}}')

result = advanced_ap_is_controller.get_summary(body)
```

## Example Response *(as JSON)*

```json
{
  "summary": "YouTube has announced a ban on videos spreading misinformation about Covid vaccines."
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorsException`](/doc/models/errors-exception.html) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](/doc/models/m426-error-exception.html) |
| 429 | Too Many Requests | `APIException` |


# Get Translate

# Translation : Defintion and it's usage

Machine Translation is translating the text automatically from  one language to another langauge.

# Languages covered:

| Languages                             | ISO Code   |
|---------------------------------------|------------|
|  Abkhazian                            |   ab       |
|  Afrikaans                            |   af       |
|  Amharic                              |   am       |
|  Bashkir                              |   ba       |
|  Catalan; Valencian                   |   ca       |
|  Chechen                              |   ce       |
|  Corsican                             |   co       |
|  Chuvash                              |   cv       |
|  Ewe                                  |   ee       |
|  English                              |   en       |
|  Basque                               |   eu       |
|  Fijian                               |   fj       |
|  French                               |   fr       |
|  Galician                             |   gl       |
|  Gujarati                             |   gu       |
|  Manx                                 |   gv       |
|  Hebrew                               |   he       |
|  Haitian; Haitian Creole              |   ht       |
|  Armenian                             |   hy       |
|  Indonesian                           |   id       |
|  Igbo                                 |   ig       |
|  Icelandic                            |   is       |
|  Japanese                             |   ja       |
|  Kalaallisut; Greenlandic             |   kl       |
|  Ganda                                |   lg       |
|  Lingala                              |   ln       |
|  Malagasy                             |   mg       |
|  Marshallese                          |   mh       |
|  Macedonian                           |   mk       |
|  Mongolian                            |   mn       |
|  Nauru                                |   na       |
|  Bokmål, Norwegian; Norwegian Bokmål  |   nb       |
|  Chichewa; Chewa; Nyanja              |   ny       |
|  Ossetian; Ossetic                    |   os       |
|  Pushto; Pashto                       |   ps       |
|  Romansh                              |   rm       |
|  Rundi                                |   rn       |
|  Sango                                |   sg       |
|  Samoan                               |   sm       |
|  Shona                                |   sn       |
|  Somali                               |   so       |
|  Albanian                             |   sq       |
|  Tamil                                |   ta       |
|  Tigrinya                             |   ti       |
|  Turkmen                              |   tk       |
|  Tonga                                |   to       |
|  Turkish                              |   tr       |
|  Tsonga                               |   ts       |
|  Tatar                                |   tt       |
|  Tahitian                             |   ty       |
|  Ukrainian                            |   uk       |
|  Vietnamese                           |   vi       |
|  Walloon                              |   wa       |
|  Xhosa                                |   xh       |
|  Yoruba                               |   yo       |
|  Zulu                                 |   zu       |

```python
def get_translate(self,
                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Optional | Add a JSON Input as per the schema defined below |

## Response Type

[`ApiTranslateResponse`](/doc/models/api-translate-response.html)

## Example Usage

```python
body = '{"input":{"text":"அவள் வேகமாக ஓடினாள்","lang":"ta"} }'

result = advanced_ap_is_controller.get_translate(body)
```

## Example Response *(as JSON)*

```json
{
  "generated_text": "இன்று நல்ல நாள்."
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorsException`](/doc/models/errors-exception.html) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](/doc/models/m426-error-exception.html) |
| 429 | Too Many Requests | `APIException` |

