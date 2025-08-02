import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

match os.name:
    case 'nt':
        os.system('cls')
    case 'posix':
        os.system('clear')
    case 'java':
        print(os.name)

class Vehicle:

    # class atribute
    type = 'fou wheeled vehicle.'

    # special method tha build the object
    def __init__(self, mark: str = '', model: str = '', color: str = ''):
        # instance attributes
        self.mark = mark
        self.model = model
        self.color = color

    # current method
    def start_vehicle(self):
        # print(f'The vehicle mark: {self.mark}, model: {self.model}, color: {self.color}. Start')
        print(f'The vehicle mark: {self.mark} and model: {self.model}. Start')

my_auto_1: Vehicle = Vehicle(mark='Ford', model='Bronco', color='blue')
print('')
my_auto_1.start_vehicle()
print(f'Mark: {my_auto_1.mark}')
print(my_auto_1.type)


my_auto_2: Vehicle = Vehicle(mark='Toyota', model='Machito', color='Grey')
print('')
my_auto_2.start_vehicle()
print(f'Mark: {my_auto_2.mark}')
print(my_auto_2.type)


# --------------------------------------------
print('')
class AI_API:
    def __init__(self, api_key: str = '', api_url: str = '', model: str = '', type: int = 0, ):
        self.api_key = api_key
        self.api_url = api_url
        self.model = model
        self.type = type

    def call(self, promt: str = '') -> object:
        result: object = {'status_code': int, 'result': object}
        result['status_code'] = 200
        try:
            api_headers: object = {
                'Content-Type': 'application/json',
            }
            api_data: object = {}

            match self.type:
                case 0:
                    api_headers['x-goog-api-key'] = self.api_key
                    api_data: object = {
                        'contents': [
                            {
                                'parts': [
                                    {
                                        'text': promt,
                                    }
                                ]
                            }
                        ]
                    }
                case 1:
                    api_headers['Authorization'] = f'Bearer {self.api_key}'
                    api_data: object = {
                        'model': self.model,
                        'messages': [
                            {'role': 'user', 'content': promt, }
                        ],
                        'stream': False
                    }

            response: object = requests.post(
                url=self.api_url,
                json=api_data,
                headers=api_headers
            )

            result['result'] = response.json()
            return result
        except Exception as ex:
            result['status_code'] = 400
            result['result'] = ex
            return result

# -------------------------------------------------------
print('')
deepmind = AI_API(
    api_key=os.environ.get('AI_GEMINIS_API'),
    api_url='https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent',
    model='',
    type=0
)

prompt: str = 'Hola, por favor hazme un poema corto sobre la musica. Gracias'
result_str: str = ''
result: object = {'status_code': int, 'result': object}
result = deepmind.call(promt=prompt)

if result:
    if result['status_code'] == 200:
        # # print(result)
        # result_str = json.dumps(obj=result['result'], indent=2)
        # print(result_str)
        print(result['result']['candidates'][0]['content']['parts'][0]['text'])
        print('')
    else:
        result_str = f'status code: {result['status_code']}\n'
        # # result_str += f'result: {json.dumps(result['result'], indent=2)}\n'
        # result_str += f'result: {json.dumps(result['result'], indent=2)}\n'
        result_str += f'result: {result['result']}\n'
        print(result_str)
else:
    print('The process is not executed')

# ------------------------------------------
print('')
deepseek = AI_API(
    api_key=os.environ.get('AI_DEEPSEEK_API'),
    api_url='https://api.deepseek.com/chat/completions',
    model='deepseek-chat',
    type=1,
)

result = deepseek.call(promt=prompt)

if result:
    if result['status_code'] == 200:
        if 'error' in result['result']:
            result_str = json.dumps(obj=result, indent=2)
            print(result_str)
        else:
            print(result)
    else:
        # print(result)
        result_str = json.dumps(obj=result, indent=2)
        print(result_str)
else: 
    print('The process is not executed')