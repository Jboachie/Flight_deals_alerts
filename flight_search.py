import requests
import datetime as dt
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "CkpktcEXiRKPlxUdxCpPnFXeQCP5i9pS"
headers = {
    "apikey": TEQUILA_API_KEY,
}

class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {
            "term": city_name,
            "location_types": "city",
                }
        response = requests.get(url=location_endpoint, headers= headers, params= query)
        response.raise_for_status()
        iatacode = (response.json()["locations"][0]["code"])
        return iatacode

    def get_flights(self, city_code):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        self.start_day = dt.datetime.now() + dt.timedelta(days=1)
        self.end_day = dt.datetime.now() + dt.timedelta(days=180)
        query = {
            "fly_from": "LON",
            "fly_to": city_code,
            "date_from": self.start_day.strftime("%d/%m/%Y"),
            "date_to": self.end_day.strftime("%d/%m/%Y"),
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "one_for_city":1,
            "curr": "GBP"
        }
        response = requests.get(url=search_endpoint, headers=headers, params=query)
        response.raise_for_status()

        self.data = response.json()["data"][0]
        self.data_price = response.json()["data"][0]["price"]

        self.fly_data = FlightData(price=self.data_price, airport_code=self.data["flyFrom"], arrival_code=self.data["flyTo"],
                              arrival_city= self.data["cityTo"], outbound_date=self.data["route"][0]["local_departure"].split("T")[0],
                              inbound_date=self.data["route"][1]["local_departure"].split("T")[0])

        return self.data_price
