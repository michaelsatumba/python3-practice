'''
import nltk
nltk.download('punkt')


sentence = "This is a simple sentence."

# Tokenize the sentence into words
words = nltk.word_tokenize(sentence)

print(words)
'''

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Set up the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a database of pre-written responses
response_database = {
    "hello": "Hello! How can I help you today?",
    "thank you": "You're welcome! Is there anything else I can help with?",
    "goodbye": "Goodbye! Have a great day.",
    "h o": "hola bro"
}

# Define a function to process the user's input
def process_input(input_text):
    # Tokenize the input
    words = word_tokenize(input_text)

    # Lemmatize the words
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]


    return lemmatized_words

# Define a function to generate a response
def generate_response(input_text):
    # Process the input
    results = process_input(input_text)

    # print('results' + str(results))

    sentence = ' '.join(results)

    # print('sentence ' + sentence)

    array = [sentence]

    # print(array)

    # Look up a matching response
    response = None
    for e in array:
        # print('e ' + e)
        if e in response_database:
            response = response_database[e]
            
            return response

    # Return the response
    return response

# Main loop
while True:
    # Get user input
    input_text = input("Enter your message: ")

    # Generate a response
    response = generate_response(input_text)

    # Print the response
    if response:
        print(response)
    else:
        print("I'm sorry, I don't understand.")


'''
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('wordnet')
'''

