import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--city", required=True, help="City to search for", type=str)
args = parser.parse_args()
city = args.city

url = f"https://api.openbrewerydb.org/v1/breweries?by_city={city}"

response = requests.get(url)

data = response.json()

class Brewery:
    id : str
    name : str
    brewery_type : str
    address_1 : str | None
    address_2 : str | None
    address_3 : str | None
    city : str
    state_province : str
    postal_code : str
    country : str
    longitude : float | None
    latitude : float | None
    phone : str | None
    website_url : str | None
    state : str
    street : str | None


    def __init__(self, data: dict):
        self.id = data["id"]
        self.name = data["name"]
        self.brewery_type = data["brewery_type"]
        self.address_1 = data.get("address_1")
        self.address_2 = data.get("address_2")
        self.address_3 = data.get("address_3")
        self.city = data["city"]
        self.state_province = data["state_province"]
        self.postal_code = data["postal_code"]
        self.country = data["country"]
        self.longitude = data.get("longitude")
        self.latitude = data.get("latitude")
        self.phone = data.get("phone")
        self.website_url = data.get("website_url")
        self.state = data["state"]
        self.street = data.get("street")

    def __str__(self):
        return f"{self.id} | {self.name} | {self.brewery_type} | {self.city}"

breweries = []

for item in data[:20]:
        brewery = Brewery(item)
        breweries.append(brewery)


for brewery in breweries:
    print(brewery)
