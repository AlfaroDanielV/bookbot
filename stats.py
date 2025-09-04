def get_word_count(content:str):
    count = content.split()
    return len(count)

def get_char_count(content:str):
    lowered = content.lower()
    no_spaces = lowered.replace(" ", "")
    no_newlines = no_spaces.replace("\n", "")
    caracters = {}
    for char in no_newlines:
        if char in caracters:
            caracters[char] += 1
        else:
            caracters[char] = 1
    return caracters  

def get_sorted_dictionarie(items:dict):
    new_dict = []
    for k in items.keys():
        new_dict.append({f"character":k,f"num":items[k]})

    new_dict.sort(key=lambda x: x['num'], reverse=True)
    return new_dict
