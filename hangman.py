from getpass import getpass

print("Starting Hangman")

word = getpass("What is the to hide ? :")

word = word.upper()

characters = []
count = 0

for i in word:
	if(i not in characters):
		characters.append(i)


life = 6

while(life != 0 and characters):
	for x in word:
		if(x in characters):
			print(" _ ", end="")
		else :
			print(" ",x," ", end="")
		
	character = input("\nWhat is your character to propose ? :").upper()
	if(character in characters):
		print("Good character ! Remains :", life)
		characters.remove(character)
	else :
		life-=1
		print("Bad character ! Remains : ", life)


if(life > 0):
	print("WIN ! Stopping Hangman...")
else:
	print("LOSE ! Stopping Hangman...")