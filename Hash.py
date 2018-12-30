from hashing import hashingtxt
import hashlib
print (3*"\t","=============> Enjoy!  <=============")
text = str(input ("Enter a text: "))

while text == '':

	print ("[!] Please Enter A Text To Continue! ")

	text = str(input("Enter a text: "))

print ("Available hash types: \n ")

print (hashlib.algorithms_available)

hashtype = (input("Enter a Hash Type: "))

while hashtype == '':

	print ("[!] Please Enter a Hash type To Continue! ")

	hashtype = (input("Enter a Hash Type: "))

h = hashingtxt()
print ("[+] your Hash is: " + h.hashtext(text,hashtype))
