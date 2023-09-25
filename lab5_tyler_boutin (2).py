"""



"""



def main():
	
	encodedWord = "WBLARF8TTS"
	encodedWord = "L8KAOUL"
	encodedWord = "E8N8N8"
	encodedWord = "8TRA8DY T8LA"
	encodedWord = "8TT LHA TILLTA LIMAS"	
	encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	
	#encodedWord = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	print(DecodeWord(encodedWord))




#Your code goes here.
def DecodeWord(word):
	Decodeword = ""
	for letters in word:
#Making new connections		
		if letters == 'T':
			Decodeword += 'L'
		elif letters == 'L':
			Decodeword += 'T'
		elif letters == 'A':
			Decodeword += '8'
		elif letters == '8':
			Decodeword += 'B'
		elif letters == 'B':
			Decodeword += 'A'
		else:
			Decodeword += letters
	return Decodeword













#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()
