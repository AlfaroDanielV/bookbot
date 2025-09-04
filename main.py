import sys
from stats import get_word_count,get_char_count,get_sorted_dictionarie
def get_book_text(book_path):
    with open(book_path) as f:
        read_data = f.read()
    return read_data




def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(book_path)
    print("============ BOOKBOT ============") 
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(content)} total words")
    print("--------- Character Count -------""")
    for item in get_sorted_dictionarie(get_char_count(content)):
        char = item['character']
        num = item['num']
        if char.isalpha():
            print(f"{char}: {num}")
    print(f"============= END ===============")
if __name__ == '__main__':
    main()
