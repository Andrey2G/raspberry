import requests
import time
import dice

def sendRequest():
    print("send request to generate the value")
    url = "https://api.conducttr.com/v1.1/project/73/start"
    key = "2c7f81e654c7b28fe72fea9fca0af192053959ce2"
    headers = {'Authorization': "Bearer " + key }
    response = requests.get(url, headers=headers)

dice.SETUP()

#ready!
print("Ready!")
while True:
    if dice.START():
        break
        
#send request to start the rolling (generate random value)
sendRequest()

#display the snake
print("snake")
qty=1
startTime=time.time()
while time.time() - startTime<3:
     dice.SNAKE(qty)
     qty=qty+1
     time.sleep(0.1)
     if qty == 7: qty = 1

print("exit from snake")
#waiting Ctrl+C
while True:
    time.sleep(1)

