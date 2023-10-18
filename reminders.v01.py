#Write a Python program that:
#asks the user for the current hour (but in military time: 0-23), then
#converts the number from a string to a float,
#sets up a series of conditions based on the current hour, and
#prints one of the following reminders:
currentmilitarytime= input("Whats the current hour in military time 0-23?: ")
convertmilitarytime= (float(currentmilitarytime))

if(convertmilitarytime <= 5):
    print("Its early. You should be sleeping!")
elif(convertmilitarytime >5 and convertmilitarytime <7): 
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast…")
elif(convertmilitarytime >=7 and convertmilitarytime <9): 
    print("Time to go to work")
elif(convertmilitarytime >= 9 and convertmilitarytime <12): 
    print("You should be working!")
elif(convertmilitarytime >= 12 and convertmilitarytime <13): 
    print("Take your lunch break!")
elif(convertmilitarytime >= 13 and convertmilitarytime <17): 
    print("Do you feel that afternoon lull?”")
elif(convertmilitarytime >= 17 and convertmilitarytime <19): 
    print("Time to hit the gym…")
elif(convertmilitarytime >= 19 and convertmilitarytime <21): 
    print("Gotta eat that dinner.")
elif(convertmilitarytime >= 21 and convertmilitarytime <23): 
    print("Get that SLEEP. And rePEAT!")

else:
    print("You didn’t type an acceptable value! (0-23)")
