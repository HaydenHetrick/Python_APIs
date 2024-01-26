import requests

def fetch_dog_api_data():
    url = "https://api.thedogapi.com/v1/breeds"
    request_headers = {
        "Content-Type": "application/json"
        "x-api-key": "live_USWuIH9WnZgCcvpUrEv75vWreINoEB8KK2ULfJrjhyr0KOLJ8I8Xnbgx7JJAliee"
    }
    response = requests.get(url, headers=request_headers)
    print("Response Status:", response.status_code)
    print("Response Text:", response.text)
    print("Response Headers:", response.headers)
    print("Request Headers:", response.request.headers)

if __name__ == "__main__":
    fetch_dog_api_data()