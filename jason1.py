"""
Jasnon - Python script to fetch and display the selected data from an url

"""


import requests

from collections import Counter

class BreweryData:

    BASE_URL = "https://api.openbrewerydb.org/breweries"



    def __init__(self, states):              #Initializes the BreweryData object with a list of states to fetch data for
        
        self.states = states

        self.data = {}




    def fetch_data(self):                  #Method to fetch brewery data for the initialized list of states
        
        for state in self.states:

            response = requests.get(self.BASE_URL, params={"by_state": state})

            if response.status_code == 200:
                self.data[state] = response.json()
            else:
                print("Error", response.status_code)




    def list_brewery_names(self):                   #Method to lists the names of all breweries in each given states
        
        print("Breweries in selected states:")

        for state, breweries in self.data.items():
            print(state)

            for brewery in breweries:
                print(brewery["name"])




    def count_breweries_by_state(self):            #Method to count breweries in each given states
        
        print("Count of breweries in each state:")

        for state, breweries in self.data.items():
            print(state, len(breweries))




    def count_brewery_types_by_city(self):        # Method to counts types of breweries in each city within each given states
        
        print("Types of breweries in each city:")

        for state, breweries in self.data.items():

            city_counter = Counter(brewery["city"] for brewery in breweries)
            print(state)

            for city, count in city_counter.items():
                print(city, count, "types of breweries")




    def breweries_with_websites(self):                #Counts and lists breweries with websites in each initialized state

        print("Count and list of breweries with websites:")

        for state, breweries in self.data.items():
            breweries_with_sites = [brewery["name"] for brewery in breweries if brewery["website_url"]]

            print(state, len(breweries_with_sites), "breweries with websites):")

            for brewery in breweries_with_sites:
                print(brewery)


if __name__ == "__main__":

    states = ["Alaska", "Maine", "New York"]

    brewery_data = BreweryData(states)

    brewery_data.fetch_data()                                 #To fetch data from URL
    
    brewery_data.list_brewery_names()                         #To list the brewery names
    
    brewery_data.count_breweries_by_state()                   #To get the count of breweries in the given state
    
    brewery_data.count_brewery_types_by_city()                #To get the count of breweries types in the given state
    
    brewery_data.breweries_with_websites()                    #To list the breweries that have websites in the given state