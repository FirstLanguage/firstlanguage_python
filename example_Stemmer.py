from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle
import pickle

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

'{"input":{"lang":"ja","url": "https://drive.google.com/uc?id=1JFV4lyT1Ajn_6jfmf5CXxw5bzQ0ra1V5", "contentType":"pdf","preserveFormat":"true"}}'
#reqbody='{"input":{"text":"Welcome to Google and FirstLanguage","lang":"en"} }'
reqbody='{"input":{"lang":"ja","url": "https://drive.google.com/uc?id=1JFV4lyT1Ajn_6jfmf5CXxw5bzQ0ra1V5", "contentType":"pdf","preserveFormat":"false"} }'
#reqbody='{"input":{"lang":"ja","url": "http://www.dhs.state.il.us/OneNetLibrary/27897/documents/Initiatives/IITAA/Sample-Document.docx", "contentType":"docx","preserveFormat":"true"} }'
body = jsonpickle.decode(reqbody)


result = advanced_api_controller.get_translate(body)
print(result)
# if(body['input']['contentType'] == 'docx'):
#   #store the binary value returned to a file  
#   with open('output.docx', 'wb') as f:
#     f.write(result.text)
#   f.close()
# if(body['input']['contentType'] == 'pdf'):
#   #store the binary value returned to a file  
#   with open('output.pdf', 'wb') as f:
#     f.write(result.text)
#   f.close()





