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

try:
    api_url: str = 'https://jsonplaceholder.typicode.com/posts/'
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
    data_edit: object = {
        'userId': 5,
        'title' : 'nivel',
        'body': '10'
    }

    response = requests.post(url=api_url, json=data_edit)
    # response = requests.post(url=api_url_error, json=post_data)
    data = response.json()
    status_code: int = response.status_code
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
def ai_geminis(api_key: str = '', prompt: str = '') -> object:
    result: object = {
        'status_code': 200,
        'result': {},
    }

    try:
        print('')
        ai_obj: object = {
            'company': {
                'deep_mint': {
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
            #'x-goog-api-key': f'{ai_obj['company']['deep_mint']['api_token']}',
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

        api_url_geminis: str = f'{ai_obj['company']['deep_mint']['api_url']}'
        api_url_geminis += f'/{ai_obj['company']['deep_mint']['models']['geminis']['flash-2.5']}'
        api_url_geminis += f':{ai_obj['company']['deep_mint']['operation_type']['generate_content']}'

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
ai_apy_key = os.environ.get('AI_GEMINIS_API')
result: object = ai_geminis(
    api_key=ai_apy_key, 
    prompt='Hola, por favor hazme un poema super corto sobre python.'
)

result_str = f'status code: {result['status_code']}\n'
result_str += f'ressult: {json.dumps(obj=result['result'], indent=2)}\n'

if result:
    if result['status_code'] == 200:
        # print(f'status code: {result['status_code']}')
        # print(json.dumps(obj=result['result'], indent=2))
        print(result_str)
    else:
        # print(f'status code: {result['status_code']}')
        # print(json.dumps(obj=result['result'], indent=2))
        print(result_str)