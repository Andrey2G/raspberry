import dice

def sendRequest():
   url = "https://api.conducttr.com/v1.1/project/73/start"
   key = "2c7f81e654c7b28fe72fea9fca0af192053959ce2"
   headers = {'Authorization': "Bearer " + key }
   response = requests.get(url, headers=headersa)

dice.SETUP()

#ready!
while True:
    if dice.START():
        break
        
#send request to start the rolling (generate random value)
sendRequest()

#display the snake
qty=1
while 1:
     SNAKE(qty)
     qty=qty+1
     time.sleep(0.1)
     if qty == 7: qty = 1
