import speech_recognition as sr
text=[]
# obtain path to audio file in the same folder as this script
import os
os.chdir('<path>')
for f in os.listdir():
	#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)),)

	# use the audio file as the audio source
	r = sr.Recognizer()
	audio_file = sr.AudioFile(f)
	with audio_file as source:
	    audio = r.record(source)  # read the entire audio file

	# recognize speech using Google Speech Recognition Library
	try:
	    text= r.recognize_google(audio)
	except sr.UnknownValueError:
	    print("Could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Speech Recognition service; {0}".format(e))

	with open(f+'_text_.txt','w') as of:
		of.write(text)
