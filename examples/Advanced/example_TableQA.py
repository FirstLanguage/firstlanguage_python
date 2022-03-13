from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle

#Init client with apiKey. Environment will always be set to PRODUCTION for now.
client = Client(
    apikey='<Your_API_Key>',
    environment=Environment.PRODUCTION,)

#Create the input string and prep it to pass it to the API
reqbody='{"input":{"flattable":{"Cities":["Paris, France","London, England","Lyon, France"],"Inhabitants":["2.161","8.982","0.513"]},"sendBackRows":false,"questions":["How many inhabitants in France","How Many inhabitants in England"]} }'
body = jsonpickle.decode(reqbody)

#Initialize the corresponding controller Basic or Advacned
adv_api_controller = client.advanced_api

#Call the corresponding API
result = adv_api_controller.get_table_qa(body)

for item in result:
    print("Query: ",item.query)
    print("Answers: ",item.answer)
   



#From URL:
reqbody = '{"input":{"questions":"","url": "","sendBackRows":"false"} }'
body = jsonpickle.decode(reqbody)
decoded_url = bytes("https://drive.google.com/uc?id=1IpBFNs4FlRRbDzL_XPtmGHou_Rvc5Mvq", "utf-8").decode("unicode_escape") 


body["input"]["url"] = decoded_url
body["input"]["questions"] = ["How many inhabitants in France"]

#Initialize the corresponding controller Basic or Advacned
adv_api_controller = client.advanced_api

#Call the corresponding API
result = adv_api_controller.get_table_qa(body)

for item in result:
    print("Query: ",item.query)
    print("Answers: ",item.answer)
