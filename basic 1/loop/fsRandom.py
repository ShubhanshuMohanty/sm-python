import random #importing random module to generate random numbers 
#Simulating temperature readings 
for i in range (1, 11): 
    temperature = random.randint(20, 100) 
    print (f"Reading (i): Temperature (temperature] °C") 
    if temperature > 70:
        print("Danger! High temperature detected. Stopping monitoring.") 
        break # Stop monitoring when temperature exceeds 