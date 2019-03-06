import speech_recognition as sr
import time

from naoqi import ALProxy


tts = ALProxy("ALTextToSpeech", "192.168.0.118", 9559)
motionProxy  = ALProxy("ALMotion", "192.168.0.118", 9559)



r = sr.Recognizer()
r.energy_threshold = 1000 #3000 using laptop microphone
r.dynamic_energy_threshold = False
motionProxy.setStiffnesses("Head", 1.0)
motionProxy.setAngles("HeadPitch",-0.28448866808,0.05)
time.sleep(10)
tts.say('Could you pick the the bottle behind the sports ball')
while(True):
		with sr.Microphone() as source:
			time.sleep(2)
			audio = r.listen(source, timeout = None)
			try:
				r = sr.Recognizer()
				r.energy_threshold = 1000
				r.dynamic_energy_threshold = False
				catched = r.recognize_google(audio,key = None, language = "en-US", show_all = False)
				print (catched)

				if 'took' in catched.lower() or 'it' in catched.lower() and not 'okay' in catched.lower() :
					tts.say('Let me check!')
					time.sleep(0.5)
					motionProxy.setAngles("HeadPitch",0.36477381367,0.05)
					time.sleep(4)
					motionProxy.setAngles("HeadPitch",-0.28448866808,0.05)
					time.sleep(2)
					tts.say('Congratulations! \\eos=1\\ You took the \\emph=1\\  correct one!')
					break
				#if 'object' in catched.lower() or 'which' in catched.lower() or 'pick' in catched.lower():
				#	motionProxy.wbEnableEffectorControl("Head", False)
			except sr.UnknownValueError:
				print("I could not understand, please repeat what you said")
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))

