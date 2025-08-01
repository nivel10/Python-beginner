import os
# os.system('clear')
os.system('cls')

from dotenv import load_dotenv
load_dotenv()

# ---------------------------------------
# GET - with out packages
print('')
import urllib.request
import json

api_url: str = ''
api_headers: object = {}
data: any = {}
status_code: int = 0
data_json: any = ''
data_edit: object = {}
response: any = {}
result: object = {}
ai_response: str = ''

try:
    api_url = 'https://jsonplaceholder.typicode.com/posts/'
    response = urllib.request.urlopen(api_url)
    data = response.read()
    data_json = json.loads(data.decode('utf-8'))

    print(data_json)

    response.close()
except urllib.error.URLError as e:
    print('Error: {e}')

# ---------------------------------------
# GET - with packages
print('')
import requests

response = requests.get(api_url)
data = response.json()
print(data)

print(data[0])

# ---------------------------------------
# POST
try:
    print('')
    api_url_error = f'https://jsonplaceholder.typecode.c'
    data_edit = {
        'userId': 5,
        'title' : 'nivel',
        'body': '10'
    }

    response = requests.post(url=api_url, json=data_edit)
    # response = requests.post(url=api_url_error, json=post_data)
    data = response.json()
    status_code = response.status_code
    print(f'result: {data}\nstatus code: {status_code}')
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')


# ---------------------------------------
# PUT
print('')
try:
    data_edit = {
        'id': 1,
        'userId': 1,
        'title': 'foo',
        'body': 'bar'
    }
    response = requests.put(url=f'{api_url}/1', json=data_edit)
    data = response.json()
    status_code = response.status_code

    print(f'result: {data}\nstatus code: {status_code}')
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')


# ---------------------------------------
# PATCH
print('')
try:
    data_edit = {
        # 'id': 1,
        # 'userId': 1,
        'title': 'new foo title',
        #'body': 'new bar'
    }
    response = requests.patch(url=f'{api_url}/1', json=data_edit)
    data = response.json()
    status_code = response.status_code

    print(f'result: {data}\nstatus code: {status_code}')
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')


# -------------------------------------------
print('')
def ai_deepmind(api_key: str = '', prompt: str = '') -> object:
    result= {
        'status_code': 200,
        'result': {},
    }

    try:
        print('')
        ai_obj: object = {
            'company': {
                'deep_mind': {
                    # 'api_token': '',
                    'models': {
                        'geminis': {
                            'flash-2.0': 'gemini-2.0-flash',
                            'flash-2.5': 'gemini-2.5-flash'
                        },
                    },
                    'operation_type': {
                        'generate_content': 'generateContent'
                    },
                    # 'api_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
                    'api_url': 'https://generativelanguage.googleapis.com/v1beta/models',
                }
            }
        }

        api_headers: object = {
            'Content-Type': 'application/json',
            #'x-goog-api-key': f'{ai_obj['company']['deep_mind']['api_token']}',
            'x-goog-api-key': api_key,
        }

        data_edit = {
            'contents': [
                {
                    'parts': [
                        {
                            # 'text': 'Hello, how are you today?'
                            'text': prompt,
                        }   
                    ]
                }
            ]
        }

        api_url_geminis: str = f'{ai_obj['company']['deep_mind']['api_url']}'
        api_url_geminis += f'/{ai_obj['company']['deep_mind']['models']['geminis']['flash-2.5']}'
        api_url_geminis += f':{ai_obj['company']['deep_mind']['operation_type']['generate_content']}'

        # print(api_url_geminis)
        # print(api_headers)
        # print(data_edit)

        response = requests.post(url=api_url_geminis, json=data_edit, headers=api_headers)
        data = response.json()
        #print(data)

        result['result'] = data
    except Exception as e:
        # print(f'Error: {e}')
        result['status_code'] = 400
        result['result'] = e

    return result


result_str: str = ''
# ai_response: str = ''
ai_deepmind_api: str = os.environ.get('AI_GEMINIS_API')
result= ai_deepmind(
    api_key=ai_deepmind_api, 
    prompt='Hola, por favor hazme un poema super corto sobre python.'
)

result_str = f'status code: {result['status_code']}\n'
result_str += f'ressult: {json.dumps(obj=result['result'], indent=2)}\n'

if result:
    if result['status_code'] == 200:
        # # print(f'status code: {result['status_code']}')
        # # print(json.dumps(obj=result['result'], indent=2))
        # print(result_str)
        ai_response = result['result']['candidates'][0]['content']['parts'][0]['text']
        print(ai_response)
        print('')
    else:
        # print(f'status code: {result['status_code']}')
        # print(json.dumps(obj=result['result'], indent=2))
        print(result_str)

# -------------------------------------------
print('')
def ai_deepseek(api_key: str = '', model: str = '', prompt: str = '') -> object:
    result= {'status_code': 200, 'result': {}} 
    try:
        api_url = f'https://api.deepseek.com/chat/completions'
        api_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        data = {
            # 'model': f'{model}:free',
            'model': model,
            'messages': [
                {'role': 'user', 'content': prompt,},
            ],
            'stream': False,
        }

        response = requests.post(url=api_url, json=data, headers=api_headers)

        result['result'] = response.json()
        return result
    except Exception as e:
        result['status_code'] = 400
        result['result'] = e
        return result

ai_deepseek_api: str = os.environ.get('AI_DEEPSEEK_API')
result = ai_deepseek(
    api_key=ai_deepseek_api, 
    model='deepseek-chat',
    # model='deepseek/deepseek-chat:free',
    prompt='Hola, por favor hazme un poema corto de python. Gracias'
)

if result:
    if result['status_code'] == 200:
        if 'error' in result['result']:
            ai_response = json.dumps(obj=result['result']['error'], indent=2)
            print(f'{ai_response}')
        else:
            ai_response = json.dumps(obj=result['result'], indent=2)
            print(ai_response)
    else:
        print(json.dumps(obj=result['result'], indent=2))