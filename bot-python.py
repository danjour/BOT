from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
#import telepot essa é usada para bot no telegram

bot = ChatBot('TW Chat Bot')

#Isso é para fazer o bot ler um arquivo de texto para treinar.
#conv=open('conversa.txt','r').readlines()
#saud=open('saudacao.txt','r').readlines()
#suge=open('sugestao.txt','r').readlines()
#prov=open('proverbio.txt','r').readlines()
#alea=open('aleatorio.txt','r').readlines()
#musi=open('musica.txt','r').readlines()
#bot.set_trainer(ListTrainer)

#bot.train(conv)
#bot.train(saud)
#bot.train(suge)
#bot.train(prov)
#bot.train(alea)
#bot.train(musi)

print("Vamos lá!!")
while True:
  resposta = input("Você : ")
  if float(resposta.confidence)>0.5: 
    print('TW Bot:', resposta)#Se a resposta for confiável, ela aparece, se não
  else:
    print('TW Bot: Ainda não sei responder esta pergunta')#Isso aparece

