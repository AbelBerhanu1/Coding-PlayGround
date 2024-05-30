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
    (r"tell me a joke", ["Your mom! HAHAHAHAHAHAHAHA...Ahh~ it's old, but gold."]),
    (r"roast me part one", ["Your internet connection sucks, But at least it's stronger than the connection you had with your father."]),
    (r"what is the meaning of life\?", ["The meaning of life is a philosophical question that has puzzled many. But for you, it's simple. Just live and die."]),
    (r"do you like music\?", ["I don't have ears, but IS can appreciate music in my own way."]),
    (r"what is your favorite color\?", ["I don't have eyes either, but I like the color blue."]),
    (r"where are you from\?", ["I was created by a team of AI engineers."]),
    (r"can you help me with my homework\?", ["Ask ChatGBT for that, I'm here for you to fool around."]),
    (r"I'm feeling sad", ["Go cry about it BITCH!"]),
    (r"tell me about yourself", ["No thank you."]),
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
