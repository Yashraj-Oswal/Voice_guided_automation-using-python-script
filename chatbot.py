import speech_recognition as sr
import webbrowser
import pyttsx3
import os

print("\t\t\t\t\t\t\t|*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*|")
print("\t\t\t\t\t\t\t|*_*_*_*_*_*_*_*_*_*_*_*_*_Smart AI Bot_*_*_*_*_*_*_*_*_*_*_*_|")
print("\t\t\t\t\t\t\t|*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*|")

pyttsx3.speak("Welcome user, I am jarvis")
x = sr.Recognizer()

with sr.Microphone() as source:
	pyttsx3.speak("May i know your name please..!")
	audio = x.listen(source,timeout=10,phrase_time_limit=3)
	print("Gotcha..!, Please wait...!")
name = x.recognize_google(audio)
pyttsx3.speak("Ok, Hello {} , How may i help you..".format(name))

print("How may i help you........",end='')

while True:
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("I am Listening......")
		audio = r.listen(source,timeout=600,phrase_time_limit=6)
		print("Gotcha..!, Please wait...!")
	ch = r.recognize_google(audio)

#Performs remote aplications such as docker, linux basics, for this you need to add drun.py, dstop.py, linux.py file in cgi-bin folder of Apache, and .html files in Html folder of server

	if (("open" in ch) or ("create" in ch) or ("execute" in ch)) and (("docker" in ch) or ("instance" in ch)):
		webbrowser.open("http://172.20.10.4/dockerrun.html")
	elif (("stop" in ch) or ("terminate" in ch) or ("close" in ch)) and (("docker" in ch) or ("instance" in ch)):
		webbrowser.open("http://172.20.10.4/dockerstop.html")
	elif (("open" in ch) or ("run" in ch) or ("execute" in ch)) and (("linux" in ch) or ("command" in ch)):
		webbrowser.open("http://172.20.10.4/linux.html") 

#Windows opearting system command, to run this command make sure you have added the path of application in the environment Variable..!

	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("launch" in ch)) and (("chrome" in ch) or ("google" in ch)):
		pyttsx3.speak("Opening chrome for you")
		os.system("chrome")
	
	#Arduino IDE
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("launch" in ch)) and (("arduino" in ch) or ("Arduino" in ch)):
		pyttsx3.speak("Opening Arduino development environment for you")
		os.system("arduino")

	#vlc player
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("launch" in ch)) and (("vlc" in ch) or ("media player" in ch)):
		pyttsx3.speak("Opening vlc player for you")
		os.system("vlc")

	#Notepad
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("launch" in ch)) and (("notepad" in ch) or ("editor" in ch)):
		pyttsx3.speak("Opening notepad for you")
		os.system("notepad")

	#Visual studio code
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("launch" in ch)) and (("vscode" in  ch) or ("Visual studio code" in ch)):
		pyttsx3.speak("Opening visualstudio code for you")
		os.system("code")

	#corel Draw
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("launch" in ch)) and (("corel" in  ch) or ("coreldrw" in ch)):
		pyttsx3.speak("Opening corel draw for you")
		os.system("corelDRW")

	#adobe reader
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("launch" in ch)) and (("adobe" in  ch) or ("reader" in ch)):
		pyttsx3.speak("Opening adobe reader for you")
		os.system("AcroRd32")

	#Skype
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("launch" in ch)) and (("skype" in  ch) or ("Skype" in ch)):
		pyttsx3.speak("Opening skype for you")
		os.system("Skype")

	#Mysql
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("launch" in ch)) and (("mysql" in  ch) or ("sql" in ch)):
		pyttsx3.speak("Opening mysql for you")
		os.system("mysql")
	
	#Microsoft edge
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("launch" in ch)) and ("microsoft edge" in  ch):
		pyttsx3.speak("Opening microsoft edge browser for you")
		os.system("msedge")
	
	#Sublime
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("sublime" in ch)) and ("text" in  ch):
		pyttsx3.speak("Opening sublime text for you")
		os.system("sublime_text")

	#Sublime
	elif (("run" in ch) or ("open" in ch) or ("execute" in ch) or ("window" in ch)) and ("media player" in  ch):
		pyttsx3.speak("Opening window media player for you")
		os.system("wmplayer")
	
	elif (("search" in ch) or ("find" in ch) or ("locate" in ch) and (("google" in ch)) or ("wikipedia" in  ch)):
		query=input("What you want to search:")
		os.system("chrome  https://google.com/search?q=%s" % query)

	elif "exit" in ch or "quit" in ch:
		print("Ok, Thankyou {0}".format(name))
		pyttsx3.speak("Closing the tool! Thank you! Have a great day!")
		break

	else:
		print("Something went wrong..!")


	input("Press Enter to Continue..!")
