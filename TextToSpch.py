#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 11:59:13 2021

@author: akhil_kk
"""

from gtts import gTTS
from playsound import playsound
# This module is imported so that we can

# play the converted audio using mpg123
import os


# Language in which you want to convert
language = 'en' 
 
import pyttsx3 
  

# Function to convert text to
# speech
def SpeakText(commandString, model="google"): 
    if model=="google":
        myobj = gTTS(text=commandString, lang=language, slow=False)
        # Saving the converted audio in a mp3 file named
        myobj.save("TempGenFiles/spch.mp3")
        #print(mytext)
        # Playing the converted file
        os.system("mpg123 TempGenFiles/spch.mp3")
        
    elif model=='pyttx':
        # Initialize the engine
        engine = pyttsx3.init()
        engine.setProperty('rate',200)   
        engine.setProperty('voice','english+f3')
        engine.say(commandString) 
        engine.runAndWait()        

