from stats import get_num_words, get_num_chars, get_sorted_list_of_dicts

import sys, os

def get_book_text(file_path):
    if os.path.exists(file_path):
        with open(file_path) as f:
            return f.read()
    else:
       return "-1"
       
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
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    if text == "-1":
        print("File error: file does not exist")
        sys.exit(1)
        
    num_words = get_num_words(text)
    dict_num_chars = get_num_chars(text)
    sorted_list = get_sorted_list_of_dicts(dict_num_chars)
    print_report(filepath, num_words, sorted_list)

main()
