import requests


print("Welcome to travel APP:")
print("What u want to do:")

while True:
    choice = input("1.check Weather \n2. View Food \n3. Check currency \n4. Exit \n")
    if choice == "1":
        try:
            city = input("Enter the city name:")
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e06b9dbdeb5f13f05cb3fcfc4e2c8899&units=metric"
            )
            user = response.json()
            print("City is :", city)
            print("Tempeature:", user["main"]["temp"])
            print("Desctiption:", user["weather"][0]["description"])
        except requests.exceptions.RequestException as e:
            print("Request Error", e)

    elif choice == "2":
        foodapi = "https://dummyjson.com/products/category/groceries"
        food = requests.get(foodapi)
        print("\n🍔 Food Items Available:")
        data = food.json()
        for item in data["products"][:5]:
            print(f"- {item['title']} | Price: ${item['price']}")

    elif choice == "3":
        currencyapi = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_IbFngrhW1zUEe4WgEEsspbTFih5HHIjAllweQ88P"
        curr = input("which currenry want to check")
        res = requests.get(currencyapi)
        user = res.json()
        print(user["data"][curr])

    elif choice == "4":
        break

    elif choice == "5":

        url = "https://apidojo-booking-v1.p.rapidapi.com/properties/list-by-map"

        querystring = {
            "room_qty": "1",
            "guest_qty": "1",
            "bbox": "14.291283,14.948423,120.755688,121.136864",
            "search_id": "none",
            "children_age": "11,5",
            "price_filter_currencycode": "USD",
            "categories_filter": "class::1,class::2,class::3",
            "languagecode": "en-us",
            "travel_purpose": "leisure",
            "children_qty": "2",
            "order_by": "popularity",
            "offset": "0",
            "arrival_date": "2025-09-10",  
            "departure_date": "2025-09-15",
        }

        headers = {
            "x-rapidapi-key": "409db41f82msh237004e068b5a07p10f0c0jsne29e3d64065c",
            "x-rapidapi-host": "apidojo-booking-v1.p.rapidapi.com",
        }

        response = requests.get(url, headers=headers, params=querystring)
        print(response.json())

    else:
        print("Invalid operator")
 
