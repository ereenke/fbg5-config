import requests

url = "http://192.168.1.33"

# Get files list
response = requests.get(url + "/server/files/list?root=gcodes")

if response.status_code == 200:
    data = response.json()

    # Sort filenames
    latest_file = max(data["result"], key=lambda x: x['modified'])
    #print(latest_file['path'])

    # Start print with latest file
    response = requests.post(url + "/printer/print/start", json={"filename": latest_file['path']} )
    #print(response)

else:
    print("ERROR:", response.status_code)



