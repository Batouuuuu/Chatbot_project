from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy


chatbot = ChatBot(
    "Chopin",
    tagger_language='fr_core_news_sm',  ## je cherche actuellement comment mettre le français sur chatterbot
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

conversation = [
    "Salut",
    "HSalut bg !",
    "Comment ça va ?",
    "Je vais bien",
    "C'est bon à entendre",
    "Merci",
    "Avec, plaisir"
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("Bonjour !")
print(response)