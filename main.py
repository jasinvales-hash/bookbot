def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
import sys

from stats import get_num_words

from stats import get_count_char

from stats import sort_on

from stats import sorted_dict

def main():
    if len(sys.argv) > 1:
        frank_text = get_book_text(sys.argv[1])
        num_words = get_num_words(sys.argv[1])
        char_count = get_count_char(sys.argv[1])
        sorted_char_count = sorted_dict(sys.argv[1])
#    sorted_char_count = s_char_count.sort(reverse=True, key=sort_on)
        words = f"Found {num_words} total words"
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(words)
        print("--------- Character Count -------")
#    print(char_count)
        for item in sorted_char_count:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
