from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle

#Init client with apiKey. Environment will always be set to PRODUCTION for now.
client = Client(
    apikey='<Your_API_Key>',
    environment=Environment.PRODUCTION,)

#Create the input string and prep it to pass it to the API
reqbody='{"input":{"context":"உப்பு, புளி, மிளகாய் மூன்றும் எப்போதும் ஒன்றாகவே இருக்கும். ஒருநாள், “குழம்பிற்கு யார் முக்கியம்? நீயா! நானா!” என்று சண்டை போட்டன. மூன்று பேரும் தனிதனியாகச் சென்று குழம்பில் சேரலாம் என்று முடிவு செய்தன. முதல் நாள், உப்பு மட்டும் குழம்பில் சேர்ந்து கொண்டது. “ஆ! ஒரே உப்பு! வாயில் வைக்க முடியவில்லை!” என்று எல்லோரும் கத்தினார்கள்","lang":"ta","question": "எவை மூன்றும் எப்போதும் ஒன்றாகவே இருக்கும்?"} }'
body = jsonpickle.decode(reqbody)

#Initialize the corresponding controller Basic or Advacned
adv_api_controller = client.advanced_api

#Call the corresponding API
result = adv_api_controller.get_qa(body)

print("Score: ",result.score)
print("Start index of the answer in the context: ",result.start)
print("End index of the answer in the context: ",result.end)
print("Answer: ",result.answer)


#From URL:
reqbody = '{"input":{"lang":"","url": "", "contentType":""} }'
body = jsonpickle.decode(reqbody)
decoded_url = bytes("https://docs.google.com/document/d/1p8ER__mGPlu59zCrqH1PxNNao92qBsq-/export?format=docx", "utf-8").decode("unicode_escape") 

body["input"]["lang"] = "en"
body["input"]["url"] = decoded_url
body["input"]["contentType"] = "docx"
body["input"]["question"] = ["What is FirstLanguage's motto?"]

#Initialize the corresponding controller Basic or Advacned
adv_api_controller = client.advanced_api

#Call the corresponding API
result = adv_api_controller.get_qa(body)

print("Score: ",result.score)
print("Start index of the answer in the context: ",result.start)
print("End index of the answer in the context: ",result.end)
print("Answer: ",result.answer)