import json
import requests
headers = {"Authorization": "Bearer ya29.a0ARrdaM89siORpFtrJLd_JeFEo3bbAx_2AqCmefB4TN7yamRDfQI5VLS3xqUvLBcctBYiJ0FgSu7cqIC0Cz_MfMm_dpt406uPb8XL5T__6TKrSBG88VKESlsw9vJUoW7yNrubUp3tu-atXyHKfM7VHk5LQfw0"}
para = {
    "name": "Inventory.txt",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./Inventory.txt", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print("Sucess,Inventory Sent to Drive!")
