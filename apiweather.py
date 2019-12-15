import request.s
api_key='7881d37e4dmsh0c5fcde9f72fde2p13e1bdjsnec926f24a142'
base_url="http://api.openweathermap.org/data/2.5/weather?"
city_name=input("enter your city name:")
complete_url=base_url + "appid=" + api_key + "&q=" + city_name
response= requests.get(complete_url)
x= response.json()
print(x)