"""
Jasnon - Python script to fetch and display the selected data from an url

"""

import requests

class CountryData:
    def __init__(self, url):                 # Constructor to initialize the URL

        self.url = url
        

    def fetch_data(self):                   # Method to fetch data from the URL and get the server status code

        response = requests.get(self.url)

        if response.status_code == 200:
            self.data = response.json()
            return ("Data fetched successfully with status code:", response.status_code)
        else:
            return ("Error Status code: ", response.status_code)



    def display_countries_and_currencies(self):   # Method to display names of countries, their currencies, and currency symbols
        
        if self.data is None:
            return "Data not found"

        for country in self.data:                 # To Access the country name
            
            if "name" in country and "common" in country["name"]:
                country_name = country["name"]["common"]
            else:
                break



            if 'currencies' in country:       # To Access the currency name and symbol if present

                for currency_code in country["currencies"]:
                    currency_info = country["currencies"][currency_code]
                    currency_name = currency_info["name"] if 'name' in currency_info else "Unknown Currency"
                    currency_symbol = currency_info["symbol"] if "symbol" in currency_info else ""

                    print(country_name, currency_name, currency_symbol)




    def display_countries_with_dollar(self):     # Method to display all countries with Dollar as currency
        
        print("Countries with Dollar as their currency:")

        for country in self.data:
                if "name" in country and "common" in country["name"]:
                  country_name  = country["name"]["common"]
                else:
                    break
        
                if 'currencies' in country:
#Using $ symbol to display the list of countries that have $ as its currency as the name of the currency have counry name along with the "dollar" - Eg: Singapore Dollar

                    for currency_symbol in country["currencies"]:   

                      currency_symbol = country["currencies"][currency_symbol]

                      if "name" in currency_symbol and currency_symbol["symbol"] == "$":
                        
                        print(country_name)
                        break



    def display_countries_with_euro(self):         # Method to display all countries with Euro as currency
        

        print("Countries with Euro as their currency:")
        
        for country in self.data:
            if "name" in country and "common" in country["name"]:
                country_name = country["name"]["common"]
            else:
                break

            if "currencies" in country:

                for currency_code in country["currencies"]:

#using currency name to display the list of countries that have Euro as its currency as the name of the currency have only "Euro"

                    currency_info = country["currencies"][currency_code]

                    if "name" in currency_info and currency_info["name"] == "Euro":
                        
                        print(country_name)
                        break


url = "https://restcountries.com/v3.1/all"

country_data = CountryData(url)

print(country_data.fetch_data())

country_data.display_countries_and_currencies()

country_data.display_countries_with_dollar()

country_data.display_countries_with_euro()

