import sys
import load_dictionary


def main():
    """ How it works"""
    word = "ethiopia"
    
    # using slicing 
    rev_word = word[::-1]
    
    if word == rev_word:
        print("Palindrome detected")
    else:
        print("Not a palindrome.")
    
    
if __name__=='__main__':
    main()