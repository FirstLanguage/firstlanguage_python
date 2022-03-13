from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle
import base64
import io

# Init client with apiKey. Environment will always be set to PRODUCTION for now.
client = Client(
    apikey='<Your_API_Key>',
    environment=Environment.PRODUCTION,)

# Create the input string and prep it to pass it to the API
reqbody = '{"input":{"text":"Today is a good day","lang":"ta"} }'

body = jsonpickle.decode(reqbody)

# Initialize the corresponding controller Basic or Advacned
adv_api_controller = client.advanced_api

# Call the corresponding API
res = adv_api_controller.get_translate(body)

print(res.generated_text)

# From URL:
#Prepare input
reqbody='{"input":{"lang":"ja","url": "https://drive.google.com/uc?id=1U8z6TUkuGOfhphEYnTuS6LJe3NWdGzFC", "contentType":"pdf","preserveFormat":"true"} }'
body = jsonpickle.decode(reqbody)

# Initialize the corresponding controller Basic or Advacned
advanced_api_controller = client.advanced_api


# Call the corresponding API
result = advanced_api_controller.get_translate(body)

if(body['input']['contentType'] == 'docx'):
     with open('output.docx', 'w') as f:
          f.write(result.text)
     f.close()
     
if(body['input']['contentType'] == 'pdf'):
     with open('output.pdf', 'wb') as f:
          f.write(result.text)
     f.close()
print("File saved to disk")

