#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
## UPDATE GOOGLE SHEETS WITH COUNTRY CODES
# for x in sheet_data:
#     if x["iataCode"] == "":
#        flight = FlightSearch()
#        x["iataCode"] = flight.get_destination_code(x["city"])
#
# data_manager.destination_data = sheet_data
# data_manager.update_destination_codes()

for city in sheet_data:
    try:
        flight = FlightSearch()
        flight_price = flight.get_flights(city["iataCode"])
        print(f"{city["city"]} : £{flight_price}")
    except IndexError:
        print(f"No flights found for {city["city"]}")

    if flight_price < city["lowestPrice"]:
        message = (f"Low price alert! Only £{flight_price} to fly from London-{flight.fly_data.departure_airport_code} to "
                   f"{flight.fly_data.arrival_city_name}-{flight.fly_data.arrival_airport_code} from {flight.fly_data.outbound_date} "
                   f"to {flight.fly_data.inbound_date}")

        notification = NotificationManager(message)


