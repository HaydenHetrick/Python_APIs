import requests
import os

def fetch_mars_rover_images():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {
        "sol": "1000",
        "api_key": "Yhttps://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=bP3garRuMgVgGYNk8HD6a7RrrWLCFeZoupBAryTz" 
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        rover_images = data["photos"][:3] 
        if not os.path.exists("mars_images"):
            os.makedirs("mars_images")

        for idx, image in enumerate(rover_images, 1):
            image_url = image["img_src"]
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open(f"mars_images/image{idx}.jpg", "wb") as f:
                    f.write(image_response.content)
                    print(f"Image {idx} saved successfully.")
            else:
                print(f"Failed to retrieve image {idx}.")
    else:
        print("Failed to fetch images.")

if __name__ == "__main__":
    fetch_mars_rover_images()
