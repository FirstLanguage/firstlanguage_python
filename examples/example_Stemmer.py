from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle


client = Client(
    apikey='079cc45f-bbb2-4f01-ac27-63ff9a2d82b5',
    environment=Environment.PRODUCTION,)

reqbody='{"input":{"text":"அவள் வேகமாக ஓடினாள்","lang":"ta"} }'

body = jsonpickle.decode(reqbody)
basic_api_controller = client.basic_api

result = basic_api_controller.get_stemmer(body)

for res in result:
  print("Original Text passed: "+res.orginal_text)
  print("Stemmed result: "+res.stem)
