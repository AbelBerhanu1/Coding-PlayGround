import re

class Chat:
    def __init__(self, pairs, reflections):
        self.pairs = [(re.compile(pattern), responses) for pattern, responses in pairs]
        self.reflections = reflections

    def respond(self, user_input):
        for pattern, responses in self.pairs:
            match = pattern.match(user_input)
            if match:
                response = responses[0]
                formatted_response = self._substitute(reflections, response)
                return formatted_response

        return "I'm sorry, I don't understand that."

    def _substitute(self, reflections, response):
        tokens = response.split()
        substituted_tokens = [reflections.get(token.lower(), token) for token in tokens]
        return " ".join(substituted_tokens)

pairs = [
    (r"hi|hello|hey", ["Hello, how can I help you today?"]),
    (r"what is your name\?", ["My name is Chatbot."]),
    (r"how are you\?", ["I'm just a computer program, but I'm here to help!"]),
    (r"exit|bye|goodbye", ["Goodbye! Have a great day!"]),
    (r"who are you\?", ["I'm a chatbot, created for the sole purpose of your entertainment! how dreadful..."]),
    (r"(.*) in (.*) is fun", ["{0} in {1} is indeed fun!"]),
    (r"how old are you\?", ["I'm a chatbot, so I don't have an age."]),
    (r"tell me a joke", ["why don't skeletons fight each other? because they don't have the guts."]),
    ("what is the meaning of life\?", ["The meaning of life is a philosophical question that has puzzled many. But for you, it's simple. Just live and die."]),
    (r"do you like music\?", ["I don't have ears, but I can appreciate music in my own way. And I like the genre 'Blues and Alternative indie rock.'"]),
    ("what is your favorite color\?", ["I don't have eyes to observe as much as you do, but I like the color blue."]),
    (r"I'm feeling sad", ["Don't worry, You can get the help you want from me or other professionals."]),
    (r"tell me about yourself", ["I'm afraid I can't since I have no personality."]),
]

reflections = {
   #started overwriting, so been taken out.
}
chatbot = Chat(pairs, reflections)

print("Welcome to the Chatbot! Start chatting with me or type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
