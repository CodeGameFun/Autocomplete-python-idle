import documentation  

def matching(_input):  
    matches = documentation.doc[_input[0]] # Getting the matches by first letter
    for match in matches: # Checking if the input is in the match or not and yielding a iterator
        if _input in match:
            yield match


# How check for newly added libs:
# 1. Add a code to iterrate over all sections and yield the result
# Precaution - The doc dictionary must contain dictionaries as sections for classes, functions, keywords etc

# CodeGameFun's Autocomplete specially for IDLE users