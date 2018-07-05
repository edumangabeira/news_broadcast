#-*-coding:utf-8-*-
'''
  I'm new to POO, so i will be trying to write code that helps me acquiring the necessary experience to deal with a huge amount of archives.

  This is originally only a simulation.
'''
class GraphAPI():
	pass

def data_limit(facebook, feed):
	facebook.feed_string = feed.split(' ')
	facebook.feed_size = len(facebook.feed_string)
	if facebook.feed_size > 25:
		facebook.feed_size = 25
	facebook.feed_text = feed 

message = 'Bem vindx ao portal de notícias da UFRJ, aqui estão as informações relevantes da sua universidade.'
ufrjnoticias = GraphAPI()
data_limit(ufrjnoticias,message)

text = open("texto.txt","w")
size = open("size.txt","w")
text.write(ufrjnoticias.feed_text)
size.write(str(ufrjnoticias.feed_size))

text.close()
size.close()


