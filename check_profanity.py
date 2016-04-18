from urllib import urlopen
import sys


# define a method to read text file
def read_file (text):
	words = open(text, 'rt')
	dictionary = words.read()
	words.close()
	return dictionary

# pass text to the service to detect profane words
def word_checker(text):
	dictionary = read_file(text)
	quotes = urlopen('http://www.wdylike.appspot.com/?q=' +  dictionary)
	response = quotes.read()
	quotes.close() 
	if response == "true":
		print('You have a profane word in the dictionary')
	else:
		print('You got no profane word in the dictionary')

def main(text):
	word_checker(text)

if __name__ == "__main__":
	main(sys.argv[1])