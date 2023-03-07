dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary['swan'] = 'cygne'
print(dictionary)


# Example 2: Add a new item to a dictionary using the "update()" method
phonebook = {} # an empty dictionary
 
phonebook["Adam"] = 3456783958 # create/add a key-value pair
print(phonebook) # outputs: {'Adam': 3456783958}
 
del phonebook["Adam"]
print(phonebook) # outputs: {}
