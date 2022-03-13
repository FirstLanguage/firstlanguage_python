from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle

#Init client with apiKey. Environment will always be set to PRODUCTION for now.
client = Client(
    apikey='<Your_API_Key>',
    environment=Environment.PRODUCTION,)

#Create the input string and prep it to pass it to the API
reqbody='{"input":{"text":"Smiling makes everyone happy","lang":"en"} }'
body = jsonpickle.decode(reqbody)

#Initialize the corresponding controller Basic or Advacned
basic_api_controller = client.basic_api

#Call the corresponding API
result = basic_api_controller.get_morph(body)
morph = result.original_string
#Parse the result
print(morph)
morphDict = {"originalText": [], "morphFeatures": []}
for key in morph:  
        morphDict["originalText"].append(str(key))
        value=""
        for items in morph[key]:
            if value != "":
                value += "|"
            value += str(items)+"="+str(morph[key][items][0])        
        morphDict["morphFeatures"].append(value)     

print(morphDict)

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
result = basic_api_controller.get_morph(body)
morph = result.original_string
#Parse the result
print(morph)
morphDict = {"originalText": [], "morphFeatures": []}
for key in morph:  
        morphDict["originalText"].append(str(key))
        value=""
        for items in morph[key]:
            if value != "":
                value += "|"
            value += str(items)+"="+str(morph[key][items][0])        
        morphDict["morphFeatures"].append(value)     

print(morphDict)
