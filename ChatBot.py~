import random
import cv2 

camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
def get_image():
 retval, im = camera.read()
 return im

for i in xrange(ramp_frames):
 temp = get_image()

camera_capture = get_image()
file = "your_pic.png"

cv2.imwrite(file, camera_capture) 
del(camera)

TALK = True

memory = []
greetings = ['hola', 'hello', 'hi','hey!','Hello','Hi','yo','yoo','heyy','hii']
questions = ['How are you?','How are you doing?','what you upto?','whaddup','watcha doing']
responses = ['Okay','I am fine','nm..','bored']
validations = ['yes','yeah','yea','no','No','Nah','nah']
verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]
abuse=["cunt","mofo","bitch","whore","slut","bastard","dick","pussy","ass","asshole","motherfucker","bc","mc","chuth"]
print("Hey! Im CB , whats your name?")
name=raw_input()
while TALK:

	userInput = raw_input(">>>"+name+": ")
	if userInput =="ok" or userInput=="k":
		reply="so.."
		reply+=random.choice(questions)
		print(reply)
		memory.append((userInput,reply))
	elif userInput =="lol" or userInput=="haha" or userInput=="hahaha":
		print("haha :P")
		memory.append((userInput,"haha :P"))
	elif userInput in greetings:
		random_greeting = random.choice(greetings)
		print random_greeting
		memory.append((userInput,random_greeting))
	elif userInput in questions:
		random_response = random.choice(responses)
		memory.append((userInput,random_response))
		print random_response
	elif userInput in verifications:
		random_response = random.choice(validations)
		memory.append((userInput,random_response))
		print random_response

	elif userInput=="quit" or userInput=="stop":
		print("Ok, Thanks for Chatting "+name+" .Hope to see you soon")
		TALK=False
		
	elif userInput in abuse:
		ab=random.choice(abuse)
		print("Dont abuse me "+ab+":P")
		memory.append((userInput,"Dont abuse me "+ab+":P"))

	else:
		print("I did not understand what you said")
		
print("Here is the entire conversation between us :)")

for conversations in memory:
	print("CB:"+conversations[0])
	print(name+":"+conversations[1])

print("PS:I took your pic secretly :P, here it is!")
img = cv2.imread('your_pic.png',1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
sys.exit()


