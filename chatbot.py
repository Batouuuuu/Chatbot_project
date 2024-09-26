from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



chatbot = ChatBot(
    "Chopin",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    #database_uri='mongodb://localhost:27017/chatterbot-database', ##connecter avec une db

    preprocessors=[
    'chatterbot.preprocessors.clean_whitespace',
    ],

    logic_adapters = [
        {
        'import_path': 'chatterbot.logic.BestMatch', 
        },
        {
        'import_path': 'chatterbot.logic.SpecificResponseAdapter',
        'input_text': 'Aide moi !',
        'output_text' : 'Euuuh non'
        }
    ]
)


conversation = [
    "Salut",
    "Salut bg !",
    "Je m'appelle Chopin",
    "Comment ça va ?",
    "Je vais bien",
    "C'est bon à entendre",
    "Merci",
    "Avec, plaisir"
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

#response = chatbot.get_response("Bonjour !")
#print(response)

while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break