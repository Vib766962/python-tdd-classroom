class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        reverse = input_str[::-1]
        return reverse
        

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        upper_char = character.upper()
        if(upper_char in ['A','E','I','O','U']):    
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        sentence_list = sentence.split(' ')
        word_length = [len(word) for word in sentence_list]
        max_index = word_length.index(max(word_length))
        return sentence_list[max_index]
        

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        sentence_list = text.split(' ')
        word_length = [len(word) for word in sentence_list]
        return word_length