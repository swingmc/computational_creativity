import random
import re

# Load and preprocess the data
def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = re.sub('[^a-z\’\'\n]', ' ', text)
    text = re.sub('[\s]+', ' ', text)
    return text

# Build the Markov chain
def build_markov_chain(text, order=1):
    words = text.split()
    index = order
    markov_chain = {}
    while index < len(words):
        key = tuple(words[index-order:index])
        if key in markov_chain:
            markov_chain[key].append(words[index])
        else:
            markov_chain[key] = [words[index]]
        index += 1
    return markov_chain

# Generate a poem
def generate_poem(markov_chain, length=50):
    seed = random.randint(0, len(markov_chain.keys()) - 1)
    keys = list(markov_chain.keys())
    key = keys[seed]
    poem = ' '.join(key)
    for _ in range(length):
        next_word = random.choice(markov_chain[key])
        poem += ' ' + next_word
        key = tuple((list(key) + [next_word])[1:])
    return poem

# Example usage
text = load_text('path_to_your_poem_corpus.txt')
markov_chain = build_markov_chain(text, order=2)
print(generate_poem(markov_chain))
