from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle

#Init client with apiKey. Environment will always be set to PRODUCTION for now.
client = Client(
    apikey='<Your_API_Key>',
    environment=Environment.PRODUCTION,)

#Create the input string and prep it to pass it to the API
reqbody='{"input":{"text":"அவள் வேகமாக ஓடினாள்","lang":"ta"} }'
body = jsonpickle.decode(reqbody)

#Initialize the corresponding controller Basic or Advacned
basic_api_controller = client.basic_api

#Call the corresponding API
result = basic_api_controller.get_stemmer(body)

#Parse the result
for res in result:
  print("Original Text passed: "+res.original_text)
  print("Stemmed result: "+res.stem)


#From URL:
reqbody = '{"input":{"lang":"","url": "", "contentType":""} }'
body = jsonpickle.decode(reqbody)
decoded_url = bytes("https://drive.google.com/uc?id=1U8z6TUkuGOfhphEYnTuS6LJe3NWdGzFC", "utf-8").decode("unicode_escape") 

body["input"]["lang"] = "en"
body["input"]["url"] = decoded_url
body["input"]["contentType"] = "pdf"

#Initialize the corresponding controller Basic or Advacned
basic_api_controller = client.basic_api

#Call the corresponding API
result = basic_api_controller.get_stemmer(body)

#Parse the result
for res in result:
  print("Original Text passed: "+res.original_text)
  print("Stemmed result: "+res.stem)