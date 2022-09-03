"""palingrams program with timer added."""
import sys
import load_dictionary
import time
start_time = time.time()


def get_word():
    ''' get the name of the user!'''
    while True:
        try:
            word = input("Enter Your Name to get its Anagrams: ")
            return word
        except ValueError:
            sys.exit("Enter a single word (no-space) to get its Anagram!")
    

def get_anagram(word_list, users_word):
    """ Checking the users word against the list to find all the anagrams"""
    anagram_list = []
    
    for word in word_list:
        if sorted(word) == sorted(users_word):
            anagram_list.append(word)
    
    return anagram_list
        

def main():
    word_list = load_dictionary.load('2of4brif.txt')
    
    users_word = get_word()
    
    # find words that the inputs anagram
    print(f"Anagrams found for {users_word}: ")
    

    #display list of anagram list
    if not get_anagram(word_list,users_word):
        print(f"No anagram found for {users_word}: ")
    else:
        for _ in get_anagram(word_list,users_word):
            print("  ",_)
        
    
    end_time = time.time()
    print("Runtime for this program was {} seconds.".format(end_time - start_time))
        
            
if __name__ == "__main__":
    main()

