# First we will import the ChatBot module
from chatterbot import ChatBot
# Then we will need a way to train our chatbot so we will use ChatterBotCorpusTrainer for a general purpuse chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Now we will create an name our chatbot, I have named mine Lyra but feed free to play around
chatbot = ChatBot('Lyra')

# We need to create a trainer of type ChatterBotCorpusTrainer from the module that we imported and pass along our chatbot Lyra over to the class constructor
trainer = ChatterBotCorpusTrainer(chatbot)

# Next up we need to use the newly create trainer to train our chatbot we will use the provided training sets from github for english, you can change the language here as well if you wish
trainer.train("chatterbot.corpus.english")

# Now that our chatbot is created and trained we will construct an infinite while loop where you will be continually prompted to interact with Lyra by asking her various questions
# The accuracy of her answers will questionable but never the less you will be able to have some fun
while True:
    # You are prompted with a message "You: " to enter a question for Lyra
    request = input("You: ")
    # Then Lyra formulates a response based on your request
    response = chatbot.get_response(request)
    # And finally that response is printed out. Play around with this a little bit it can be fun!
    print("Lyra: ", response)
