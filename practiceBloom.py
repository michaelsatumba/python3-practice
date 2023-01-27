# practice bloom

'''
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom")

model = AutoModel.from_pretrained("bigscience/bloom")

print(model)
'''
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

# Load the pre-trained model and tokenizer
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")

# Define the question and context
question = "What is the moon made of?"
context = "The moon is a natural satellite of the Earth. It is the fifth-largest satellite in the Solar System, and the largest among planetary satellites relative to the size of the planet that it orbits. The moon is made mostly of rock."

# Encode the input
input_ids = tokenizer.encode(question, context)

# Get the output
output = model(input_ids)

# Extract the answer from the output
answer = tokenizer.decode(output[0][0][0], skip_special_tokens=True)

print("Answer:", answer)

