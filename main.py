from stats import get_num_words, get_num_chars, get_sorted_list_of_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(filepath,num_words,sorted_list):
    out = f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------"""
    print(out)
    for list_item in sorted_list:
        if list_item["char"].isalpha():
            print(f"{list_item["char"]}: {list_item["num"]}")
    print("============= END ===============")

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    dict_num_chars = get_num_chars(text)
    sorted_list = get_sorted_list_of_dicts(dict_num_chars)

    #print(f"Found {num_words} total words")
    #print(dict_num_chars)
    #print(get_sorted_list_of_dicts(dict_num_chars))
    print_report(filepath, num_words, sorted_list)
main()
