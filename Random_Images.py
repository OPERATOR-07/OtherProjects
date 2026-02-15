# This Program will overwrite the "img.jpg" file whenever you run it to save space
# Makesure you have Pillow module installed in your python environment with "pip install pillow"
import requests
from PIL import Image
url = "https://picsum.photos/300"
response = requests.get(url)

if response.status_code == 200:
	with open("img.jpg", "wb") as f:
	    f.write(response.content)
	print("Image saved")
	
	Image.open("img.jpg").show()

else:
    print(f"Error: {response.ststus_code}")
