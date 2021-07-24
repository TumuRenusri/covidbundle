import requests

country=input("Enter the country:").capitalize()

request_link = f"https://corona.lmao.ninja/v2/countries/{country}"
header={'User-Agent':'Chrome/84.0.4147.105 Safari/537.36'}
response=requests.get(request_link,headers=header)
raw_JSON=response.json()
Total_countries=len(raw_JSON['country'])
print(f"country name:",raw_JSON['country'])
info = ''
while info != "3":
    print("press '1' to get todays information")
    print("press '2' to get all information")
    print("press '3' to Exit")
    x=input()
    if x == "1":
        print("-------------------------Todays Info-----------------------------------")
        print("Today cases---->{}\nToday Recoverd----->{}\nToday Death------->{}".format(
            raw_JSON['todayCases'], raw_JSON['todayRecovered'], raw_JSON['todayDeaths']))
    elif x=="2":
        print("--------------------------All Info----------------------------------")
        print("Total cases------>{}\nTest------>{}\nRecoverd------>{}\nActive------>{}\nDeath------>{}\nCritical------>{}".format(
            raw_JSON['cases'], raw_JSON['tests'], raw_JSON['recovered'], raw_JSON['active'], raw_JSON['deaths'], raw_JSON['critical']))
    elif x=="3":
        break;

   

