# TTS-Chatbot
A chatbot program that is being worked on with the intent of utilizing AI to respond to 
personalized conversation at a fast speed utilizing GPU acceloration, Hash tables, and more.

This project has started as pure spagetti code, but I'm working on adding modularity to it, such that it can utilize the GPU, doesn't need 
to use spagetti code, and uses hash tables however those work. 

At its current state, it uses the speech recognition module and gTTS to sort of just fill out hardcoded commands, but I plan on 
making this all modular, to the point where editing a txt file could add new things to command it to do.

I also plan on putting it on a server then having a phone version of the software that simply does the speech rec. then sends it
to the server to calculate a string/command response.

But for now, I'd like to impliment the following:
-chatbot style AI that can furfil responses in some kind advanced way
-modularity to the software that so you could add commands and remove them
easily, and also it could find stuff on your computer with needing to be told where it is (try where.exe in the console)
-Tensorflow GPU acceloration and such to make the program much faster
