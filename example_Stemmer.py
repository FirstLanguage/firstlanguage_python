from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle


client = Client(
    apikey='63af276e-34fe-4fd5-a474-0c69847f25e1',
    environment=Environment.PRODUCTION,)

reqbody='{"input":{"text":"அவள் வேகமாக ஓடினாள்","lang":"ta"} }'

body = jsonpickle.decode(reqbody)
basic_api_controller = client.basic_api

advanced_api_controller = client.advanced_api

result = basic_api_controller.get_stemmer(body)

for res in result:
  print("Original Text passed: "+res.orginal_text)
  print("Stemmed result: "+res.stem)

reqbody='{"input":{"text":"Welcome to Google and FirstLanguage","lang":"en"} }'

body = jsonpickle.decode(reqbody)

result = advanced_api_controller.get_translate(body)

print(result)

reqbody='{"input":{"url":"https://i.redd.it/v1fvin01ynv51.jpg"} }'

body = jsonpickle.decode(reqbody)

result = advanced_api_controller.get_image_caption(body)

print("generated caption: "+result.generated_caption)

