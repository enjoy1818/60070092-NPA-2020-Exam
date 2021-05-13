import requests
import json

def main():
    # Resource URL
    hostname = "10.0.15.103"
    username = "admin"
    password = "cisco"
    url = "https://{}/restconf/data/ietf-interfaces:interfaces/interface=Loopback60070092/".format(hostname)

    command = ''
    webex_bearer_token = "NjU0MWFjYTgtYmM0MS00NjBkLTg5MjctODU3NTQ3YjMyYmYxMDJjYmIwOWMtNGEx_PF84_consumer"
    webex_room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3"
    message_response = {}
    headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    }

    response = requests.request("GET", url, headers=headers, auth=(username, password), verify=False)
    data = json.loads(response.text)
    print(data['ietf-interfaces:interface']['enabled'])

    while command.lower() != "exit":
        message = get_message(webex_bearer_token, webex_room_id)
        if message_response == message:
            # print(message)
            continue
        else:
            message_response = message
            command = message['items'][0]['text']
            print(command)
        if "60070092" == command:
            response = requests.request("GET", url, headers=headers, auth=(username, password), verify=False)
            data = json.loads(response.text)
            if data['ietf-interfaces:interface']['enabled'] == True:
                interface_status = 'Loopback60070092 - Operational status is up'
            else:
                interface_status = 'Loopback60070092 - Operational status is down'
            webex_response = sent_to_webex(webex_bearer_token, webex_room_id, interface_status)
            print(webex_response)
    if command.lower() == 'exit':
        webex_response = sent_to_webex(webex_bearer_token, webex_room_id, "Bot ends")

def sent_to_webex(webex_bearer_token, webex_room_id, text):
    webex_url = "https://webexapis.com/v1/messages"
    webex_auth = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(webex_bearer_token)}
    webex_payload = {"roomId":webex_room_id, 'text':text}
    webex_response = requests.post(url=webex_url, headers=webex_auth, json=webex_payload).json()
    return webex_response

def get_message(webex_bearer_token, webex_room_id):
    webex_url = "https://webexapis.com/v1/messages"
    webex_auth = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(webex_bearer_token)}
    webex_param = {"roomId":webex_room_id, 'max':1}
    webex_response = requests.get(url=webex_url, headers=webex_auth, params=webex_param).json()
    return webex_response
    # print(webex_response)
 
main()
