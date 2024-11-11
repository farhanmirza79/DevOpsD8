from pprint import pprint
import requests
# getting the response form the api, pass the url of the api, get the response code and prin the json response

def get_api_response(url):
    response = requests.get(url)
    print(response.status_code)
    json_response = response.json()
    pprint(json_response)
    data = json_response["data"]
    #print(data)
    for user in data:
        print(user["first_name"])
get_api_response("https://reqres.in/api/users?page=2")

print("*********************************************************************************")

#Post data to api, pass the url and  the data to be posted
def post_api_data(url, data):
    response = requests.post(url, data)
    print(response.status_code)
    print(response.text)

post_api_data("https://reqres.in/api/users",{
    "name": "morpheus",
    "job": "leader",
    "id": "295",
    "createdAt": "2024-09-24T13:25:01.348Z"
})

print("*********************************************************************************")

#Put data to api, pass the url

def put_api_data(url,data):
    response = requests.put(url,data)
    print(response.status_code)
    print(response.text)

put_api_data("https://reqres.in/api/users/2",{
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": "2024-09-24T13:53:09.635Z"
})

print("*********************************************************************************")

#Get - single user

def get_api_response(url,data):
    response = requests.get(url,data)
    print(response.status_code)
    json_response = response.json()
    pprint(json_response)

    pprint(['last_name'])
get_api_response("https://reqres.in/api/users/2",{
        "data": {"id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
})
