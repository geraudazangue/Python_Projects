#pip install requests
import requests
response = requests.get('https://api.github.com')
#response.status_code
'''
response.content
response.text
response.headers
response.headers['Content-Type']
response.elapsed.total_seconds()
'''
'''from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
'''
'''
requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get')
requests.get('https://api.github.com/user', auth=('username', 'pass'))
'''
'''
#import urllib.request
sites = [url1, url2]
for url in sites:
    with urllib.request.urlopen(url) as u:
        page = u.read()
        print(url,len(page))
'''
