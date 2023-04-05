text = "ukoajecuzoutakujalini"

# Define the length of the words
word_length = 3

# Initialize an empty list to store the separated words
words = []

# Loop through the text by the word length
for i in range(0, len(text), word_length):
    # Extract the word from the text
    word = text[i:i + word_length]
    # Add the word to the list of words
    words.append(word)

# Join the words with a space character
separated_text = " ".join(words)

print(separated_text)
