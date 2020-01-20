#This Python project will generate a secure password for you based on your raw input.
import random
import string
print "This Secure Password Generator will create a secure password for you."
#Line 4 will take a passphrase input from the user.
phrase = raw_input("Please enter a phrase consisting of five to eight words: ")
#This will check to see if the phrase is at least 20 characters long and no more than 35.
if len(phrase) > 35:
    print "Please keep your phrase under 35 characters. You currently have %d characters." % (len(phrase))
elif len(phrase) < 20:
    print "Please enter at least 20 characters. You currently have %d characters." % (len(phrase))
else:
    print "Thanks!"
#This conditional check the input to see if it contains only alpha characters and spaces.
if len(phrase) > 0 and phrase.isalpha() or phrase.replace(' ','').isalpha():
    passphrase = phrase.lower()
#This command converts the entire phrase to lowercase and prints it to the console.
    print passphrase
else:
    print "Error! Please enter only letters."
def random_phrase(passlength = 8):
    letters = random.choice(passphrase)
    return ''.join(random.choice(letters) for i in range(passlength))
print ("Your password is ", random_phrase())
