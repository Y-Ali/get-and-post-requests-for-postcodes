import requests

post_codes = requests.get('https://api.postcodes.io/postcodes/en37an')

#print(post_codes.json()['result'].keys())


#print(post_codes.json()['result']['country'])

for i in post_codes.json()['result']:
    #print("key:", i)
    print(i, ": ",post_codes.json()['result'][i])
