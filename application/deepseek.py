import http.client
import json

class DeepseekChat:
    def __init__(self, api_key, base_url="api.deepseek.com"):
        self.api_key = api_key
        self.base_url = base_url

    def send_message(self, message):
        conn = http.client.HTTPSConnection(self.base_url)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

        payload = json.dumps({
            "message": message
        })

        conn.request("POST", "/v1/chat", body=payload, headers=headers)

        response = conn.getresponse()
        data = response.read()
        conn.close()

        if response.status == 200:
            return json.loads(data.decode("utf-8"))
        else:
            raise Exception(f"API request failed with status {response.status}: {data.decode('utf-8')}")

# Kullanım örneği
api_key = "sk-2dcb49dd59ed4604905447649051658d"
chat = DeepseekChat(api_key)

try:
    response = chat.send_message("Merhaba, nasılsın?")
    print("Deepseek Cevabı:", response)
except Exception as e:
    print("Hata:", e)