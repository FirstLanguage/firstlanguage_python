# Advanced AP Is

```python
advanced_ap_is_controller = client.advanced_ap_is
```

## Class Name

`AdvancedAPIsController`

## Methods

* [Get Classification](../../doc/controllers/advanced-ap-is.md#get-classification)
* [Get QA](../../doc/controllers/advanced-ap-is.md#get-qa)
* [Get Table QA](../../doc/controllers/advanced-ap-is.md#get-table-qa)
* [Get Image Caption](../../doc/controllers/advanced-ap-is.md#get-image-caption)
* [Get NER](../../doc/controllers/advanced-ap-is.md#get-ner)
* [Get Summary](../../doc/controllers/advanced-ap-is.md#get-summary)
* [Get Translate](../../doc/controllers/advanced-ap-is.md#get-translate)


# Get Classification

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
| `body` | [`object`](../../$m/) | Body, Required | Add a JSON Input as per the schema defined below<br><br>**Size limit:**<br><br>1MB for both text and URL input<br><br>**URL Input:**<br><br>For URL, we now accept 4 contentTypes.<br><br>* html<br>* plaintext<br>* pdf<br>* docx<br><br>If you are providing Google drive or Google Spreadsheet url, ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Drive link:<br><br>https://drive.google.com/uc?id=idofthefile |

## Response Type

[`Responseclassify`](../../doc/models/responseclassify.md)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"input":{"context":"context6","lang":"lang6","labels":[{"key1":"val1","key2":"val2"},{"key1":"val1","key2":"val2"},{"key1":"val1","key2":"val2"}]}}}')

result = advanced_ap_is_controller.get_classification(body)
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
| 400 | Error output | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`ApiClassify426ErrorException`](../../doc/models/api-classify-426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |


# Get QA

A Question Answering System retrieves the answer relevant to the question given by the user. A question answering system can be used for building a text based chatbots, search engines etc. Our question answering system  is mutilingual and supports 100 + languages. Please use ISO 639-2 2 digit language code  to get results. For example, use 'en' for English, 'ta' for Tamil, 'hi' for Hindi, 'fr' for French etc.

For ISO code reference, please check the link https://www.loc.gov/standards/iso639-2/php/code_list.php

```python
def get_qa(self,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`object`](../../$m/) | Body, Optional | Add a JSON Input as per the schema defined below<br><br>**Size limit:**<br><br>1MB for both text and URL input<br><br>**URL Input:**<br><br>For URL, we now accept 4 contentTypes.<br><br>* html<br>* plaintext<br>* pdf<br>* docx<br><br>If you are providing Google drive or Google Spreadsheet url, ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Drive link:<br><br>https://drive.google.com/uc?id=idofthefile |

## Response Type

[`ApiQaResponse`](../../doc/models/api-qa-response.md)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"input":{"question":"எவை மூன்றும் எப்போதும் ஒன்றாகவே இருக்கும்?","lang":"ta","context":"உப்பு, புளி, மிளகாய் மூன்றும் எப்போதும் ஒன்றாகவே இருக்கும். ஒருநாள், “குழம்பிற்கு யார் முக்கியம்? நீயா! நானா!” என்று சண்டை போட்டன. மூன்று பேரும் தனிதனியாகச் சென்று குழம்பில் சேரலாம் என்று முடிவு செய்தன. முதல் நாள், உப்பு மட்டும் குழம்பில் சேர்ந்து கொண்டது. “ஆ! ஒரே உப்பு! வாயில் வைக்க முடியவில்லை!” என்று எல்லோரும் கத்தினார்கள்"}}}')

result = advanced_ap_is_controller.get_qa(body)
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
| 400 | Bad Request | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](../../doc/models/m426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |


# Get Table QA

# TableQA : Defintion and it's usage

Table QA uses TAPAS based model to get answers from table input. The table can be parsed into a JSON object or it can be a link to a CSV file. Currently only Plain CSV file is supported.

This API works only for English language currently

Example for flattend table in JSON Format:<br/>
{"Cities": ["Paris, France", "London, England", "Lyon, France"], "Inhabitants": ["2.161", "8.982", "0.513"]}

The API can return the original table rows from which the answer was extracted based on the flag 'sendBackRows'

```python
def get_table_qa(self,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`object`](../../$m/) | Body, Optional | Add a JSON Input as per the schema defined below. For URL input, if you are providing Google drive or Google Spreadsheet url ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Spreadsheet link:<br><br>https://docs.google.com/spreadsheets/d/1TtzPAHqpaTB7Ltdq0zwZ8FamF7O9aC4KH4EpmwI/export?format=csv&gid=151344200<br><br>Example for Google Drive link:<br><br>https://drive.google.com/uc?id=idofthefile<br><br>For Flat table input check the example. |

## Response Type

[`List of ApiTableqaResponse`](../../doc/models/api-tableqa-response.md)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"input":{"flattable":{"Cities":["Paris, France","London, England","Lyon, France"],"Inhabitants":["2.161","8.982","0.513"]},"sendBackRows":false,"questions":["How many inhabitants in France","How Many inhabitants in England"]}}}')

result = advanced_ap_is_controller.get_table_qa(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "query": "How many inhabitants in France",
    "answer": [
      "SUM > 2.674"
    ],
    "rows": [
      "Paris, France,2.161",
      "Lyon, France,0.513"
    ]
  },
  {
    "query": "How Many inhabitants in England",
    "answer": [
      "SUM > 8.982"
    ],
    "rows": [
      "London, England,8.982"
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](../../doc/models/m426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |


# Get Image Caption

# Image Captioning with Visual Attention : Defintion and it's usage

Image Captioning is the process of generating textual description of an image. It uses both Natural Language Processing and Computer Vision to generate the captions.

This API works generates only English Captions

<b>Enterprise Plan Alert:</b> For Enterprise Users GPU powered endpoint can be provisioned. <b> This will reduce the response time of the API by alomst 90%.</b>

```python
def get_image_caption(self,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiImagecaptionRequest`](../../doc/models/api-imagecaption-request.md) | Body, Optional | Add a JSON Input as per the schema defined below.<br><br>For URL, if you are providing Google drive or Google Spreadsheet url ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Drive:<br><br>https://drive.google.com/uc?id=idofthefile |

## Response Type

[`ApiImagecaptionResponse`](../../doc/models/api-imagecaption-response.md)

## Example Usage

```python
body = ApiImagecaptionRequest()
body.input = Input9()
body.input.url = 'https://i.redd.it/v1fvin01ynv51.jpg'

result = advanced_ap_is_controller.get_image_caption(body)
```

## Example Response *(as JSON)*

```json
{
  "generated_caption": "A view of a beach with a sun shining over it"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](../../doc/models/m426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |


# Get NER

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
| `body` | [`object`](../../$m/) | Body, Optional | Add a JSON Input as per the schema defined below<br><br>**Size limit:**<br><br>1MB for both text and URL input<br><br>**URL Input:**<br><br>For URL, we now accept 4 contentTypes.<br><br>* html<br>* plaintext<br>* pdf<br>* docx<br><br>If you are providing Google drive or Google Spreadsheet url, ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Drive link:<br><br>https://drive.google.com/uc?id=idofthefile |

## Response Type

[`List of ApiNerResponse`](../../doc/models/api-ner-response.md)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"input":{"text":"إسمي محمد وأسكن في برلين","lang":"ar"}}}')

result = advanced_ap_is_controller.get_ner(body)
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
| 400 | Bad Request | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](../../doc/models/m426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |


# Get Summary

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
| `body` | [`object`](../../$m/) | Body, Optional | Add a JSON Input as per the schema defined below<br><br>**Size limit:**<br><br>1MB for both text and URL input<br><br>**URL Input:**<br><br>For URL, we now accept 4 contentTypes.<br><br>* html<br>* plaintext<br>* pdf<br>* docx<br><br>If you are providing Google drive or Google Spreadsheet url, ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Drive link:<br><br>https://drive.google.com/uc?id=idofthefile |

## Response Type

[`ApiSummaryResponse`](../../doc/models/api-summary-response.md)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"input":{"text":"Videos that say approved vaccines are dangerous and cause autism, cancer or infertility are among those that will be taken down, the company said. The policy includes the termination of accounts of anti-vaccine influencers. Tech giants have been criticised for not doing more to counter false health information on their sites. In July, US President Joe Biden said social media platforms were largely responsible for people\'s scepticism in getting vaccinated by spreading misinformation, and appealed for them to address the issue. YouTube, which is owned by Google, said 130,000 videos were removed from its platform since last year, when it implemented a ban on content spreading misinformation about Covid vaccines. In a blog post, the company said it had seen false claims about Covid jabs spill over into misinformation about vaccines in general. The new policy covers long-approved vaccines, such as those against measles or hepatitis B. We\'re expanding our medical misinformation policies on YouTube with new guidelines on currently administered vaccines that are approved and confirmed to be safe and effective by local health authorities and the WHO, the post said, referring to the World Health Organization.","lang":"en"}}}')

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
| 400 | Bad Request | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](../../doc/models/m426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |


# Get Translate

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
| `body` | [`object`](../../$m/) | Body, Optional | Add a JSON Input as per the schema defined below<br><br>**Size limit:**<br><br>1MB for both text and URL input<br><br>**URL Input:**<br><br>For URL, we now accept 4 contentTypes.<br><br>* html<br>* plaintext<br>* pdf<br>* docx<br><br>If you are providing Google drive or Google Spreadsheet url, ensure that you provide a link which can download the file directly and not the share link.<br><br>Example for Google Drive link:<br><br>https://drive.google.com/uc?id=idofthefile<br><br>**preserveFormat Flag:**<br><br>When true:<br><br>This applies only for PDF and DOCX content types. The API will try to maintain the source file formatting. DOCX files will mostly work without any issues. But for PDF files, the API will try to maintain the format but it is not guaranteed. Scanned documents will also not work. For PDF files, if the target language font is not renderred properly, please report the issue at info@firstlanguage.in<br><br>When false:<br><br>If the flag is false, then the API will simply read all text in the PDF and docx files and translate and send the response back as plaintext. |

## Response Type

[`ApiTranslateResponse`](../../doc/models/api-translate-response.md)

## Example Usage

```python
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"input":{"text":"Today is a good day","lang":"ta"}}}')

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
| 400 | Bad Request | [`ErrorsException`](../../doc/models/errors-exception.md) |
| 426 | Please use HTTPS protocol | [`M426ErrorException`](../../doc/models/m426-error-exception.md) |
| 429 | Too Many Requests | `APIException` |

