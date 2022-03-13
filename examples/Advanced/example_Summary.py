from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle

# Init client with apiKey. Environment will always be set to PRODUCTION for now.
client = Client(
    apikey='<Your_API_Key>',
    environment=Environment.PRODUCTION,)

# Create the input string and prep it to pass it to the API
reqbody = '{"input":{"text":"We at FirstLanguage Technologies build state-of-the-art NLP APIsolutions for your\
     business at lowest price in the market. FirstLanguageTechnologies was founded in the year 2021 with a mission\
          to spread NLP technology across the world. NLP for the masses is our motto. We provide API services which\
               are simple to use, easy to integrate and can be understood very easily by anyone.\
                    FirstLanguage provides basics APIssuch as, stemmer, POS Tagger, Morphological Analyzer.\
                         and Lemmatizer. The advanced APIs provided by FirstLanguage are,Question Answering,\
                              Table Question Answering, Summarization and Machine Translation. \
                              All these APIs are built using state-of-the art deeplearning models fine tuned by us \
                                  and works for 100 plus languages.","lang":"en"} }'
body = jsonpickle.decode(reqbody)

# Initialize the corresponding controller Basic or Advacned
adv_api_controller = client.advanced_api

# Call the corresponding API
res = adv_api_controller.get_summary(body)

print(res.summary)

# From URL:
reqbody = '{"input":{"lang":"","url": "", "contentType":""} }'
body = jsonpickle.decode(reqbody)
decoded_url = bytes("https://docs.google.com/document/d/1p8ER__mGPlu59zCrqH1PxNNao92qBsq-/export?format=docx",
                    "utf-8").decode("unicode_escape")

body["input"]["lang"] = "en"
body["input"]["url"] = decoded_url
body["input"]["contentType"] = "docx"


# Initialize the corresponding controller Basic or Advacned
adv_api_controller = client.advanced_api

# Call the corresponding API
res = adv_api_controller.get_summary(body)

print(res.summary)
