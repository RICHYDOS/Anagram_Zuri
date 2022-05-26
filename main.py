#Takes input from the user
word = input("Enter the Word: ")
anagram = input("Enter the word you think is its anagram: ")

def find_anagram(word, anagram):
    word_list = []
    count = 0

    for i in word:
        #Iterates over the string and adds each letter to the list
        word_list.append(i)

    for i in anagram:
        #Iterates over the string and checks to see if the word is in the list
        if i in word_list:
            continue
        else:
            count = 1

#True if the words are anagrams and False if the words are not anagrams
    if count == 1:
        return False
    else:
        return True

print(find_anagram(word, anagram))

