import random

TALK = True

memory = []
greetings = ['hola', 'hello', 'hi','hey!','Hello','Hi','yo','yoo','heyy','hii']
questions = ['How are you?','How are you doing?','what you upto?','whaddup','watcha doing']
responses = ['Okay','I am fine','nm..','bored']
validations = ['yes','yeah','yea','no','No','Nah','nah']
verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]

print("Hey! Im CB , whats your name?")
name=raw_input()
while TALK:

	userInput = raw_input(">>>"+name+": ")
	if userInput in greetings:
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
	elif 'sure' in userInput:
		response = "Sure about what?"
		memory.append(('sure',response))
		print response
		
	elif userInput=="quit" or userInput=="stop":
		print("Ok, Thanks for Chatting "+name+" .Hope to see you soon")
		TALK=False
	else:
		print("I did not understand what you said")
		
print("Here is the entire conversation between us :)")

for conversations in memory:
	print("CB:"+conversations[0])
	print(name+":"+conversations[1])

