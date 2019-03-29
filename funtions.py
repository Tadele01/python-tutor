def search4vowels(word:str) -> set:
    
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase : str , letter : str = "aeiou") -> set:
    """"Return a set of letters found in a phrase """
    return set(phrase).intersection(set(letter))

a = search4letters(letter = "ade", phrase = "Tadele ") #we can not use both positional and keyword argument passing at ehe smme time 
if bool(a) == 0:
    print("sorry we could not find it ")
          
else:
    
    for i in a :
        print(i)
    
