pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
 
print(len(pol_eng_dictionary)) # outputs: 3
del pol_eng_dictionary["zamek"] # remove an item
print(len(pol_eng_dictionary)) # outputs: 2
 
print(len(pol_eng_dictionary)) # outputs: 0
 
del pol_eng_dictionary # removes the dictionary
