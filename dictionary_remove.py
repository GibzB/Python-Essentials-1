dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
del dictionary['dog']
print(dictionary)

# An alternative is to use the "popitem()" method
dictionary.popitem()
print(dictionary)