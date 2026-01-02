def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    result = {}
    for c in text:
        c_lowerkey = c.lower()
        if c_lowerkey in result:
            result[c_lowerkey] += 1
        else:
            result[c_lowerkey] = 1
    return result

def sort_on(items):
    return items["num"]

def get_sorted_list_of_dicts(text_dict):
    result = [{"char": key, "num": value} for key, value in text_dict.items()]
    result.sort(reverse=True, key=sort_on)
    return result
