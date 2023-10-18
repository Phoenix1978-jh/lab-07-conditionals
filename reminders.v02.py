#Write a Python program that:
#asks the user for the current hour (but in military time: 0-23), then
#converts the number from a string to a float,
#sets up a series of conditions based on the current hour, and
#prints one of the following reminders:
import datetime

#currentmilitarytime= input("Whats the current hour in military time 0-23?: ")
#now.hour= (float(currentmilitarytime))
now =datetime.datetime.now()
print(now.hour)

if(now.hour <= 5):
    print(now.hour)
elif(now.hour >5 and now.hour <7): 
    print(now.hour)
elif(now.hour>=7 and now.hour<9): 
    print(now.hour)
elif(now.hour >= 9 and now.hour <12): 
    print(now.hour)
elif(now.hour >= 12 and now.hour<13): 
    print(now.hour)
elif(now.hour >= 13 and now.hour <17): 
    print(now.hour)
elif(now.hour >= 17 and now.hour<19): 
    print(now.hour)
elif(now.hour >= 19 and now.hour <21): 
    print(now.hour)
elif(now.hour >= 21 and now.hour <23): 
    print(now.hour)

else:
    print("You didn’t type an acceptable value! (0-23)")
