from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle

#Init client with apiKey. Environment will always be set to PRODUCTION for now.
client = Client(
    apikey='<Your_API_Key>',
    environment=Environment.PRODUCTION,)

#From URL:
reqbody = '{"input":{"url": ""} }'
body = jsonpickle.decode(reqbody)
decoded_url = bytes("https://i.redd.it/v1fvin01ynv51.jpg", "utf-8").decode("unicode_escape") 


body["input"]["url"] = decoded_url


#Initialize the corresponding controller Basic or Advacned
adv_api_controller = client.advanced_api

#Call the corresponding API
result = adv_api_controller.get_image_caption(body)

print("Caption: ",result.generated_caption)
