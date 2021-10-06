import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)

url = "https://postman-echo.com/get"
#url = "https://postman-echo.com/get?foo1=bar1&foo2=bar2"



#Get request
response = requests.get(url)
pp.pprint(response.json())


#Post to create new object
url1 = "https://postman-echo.com/post"
payload = {'key1': 'value'}
response1 = requests.post(url1, data=payload)

pp.pprint(response1.json())


#used for updating the existing data
url2 = "https://postman-echo.com/put"
payload2 = {'key1': 'value1'}
response2 = requests.put(url2, data=payload2)
pp.pprint(response2.json())


