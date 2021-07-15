import process 
import time
#note that this program is designed to run in python 3.60

process.name = "Janet"  #setting the name of the AI



#main loop
while True:


    #getting the users audio and turning it into string
    text = process.getAudio()

    #it looks for hey, and the name of the "AI" then calls the process
    if "hey " + process.name in text:
        print(text) #debugging
        process.process(text)   #the process of checking commands
        time.sleep(1)   #wait after doing the process
        
    
