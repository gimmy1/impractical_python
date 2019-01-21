from build_dictionary import BuildDictionary
import random
import pdb

def main():
    file_data = BuildDictionary()
    input_dict = file_data.get_data()
    before_pig_latin = PigLatin(input_dict)
    pig_latin = before_pig_latin.pig_latin()
    print(pig_latin)


class PigLatin:
    def __init__(self, input_dict):
        self.input_dict = input_dict
        self.vowels = 'AEIOU'
    
    def pig_latin(self):
        """ 
            Create a little pig latin for fun!
            What is pig latin?
            if the word begins with a consonant, 
                - take the first letter, add it to the end of the word, and append 'ay'
            else:
                - add 'way' to the end
        """
        before_pig_latin = self._get_random_word()
        # before_pig_latin = 'Anthony'
        if before_pig_latin[0] in self.vowels:
            pig_latin = before_pig_latin + 'way'
        else:
            pig_latin = before_pig_latin[1:] + before_pig_latin[0] + 'ay'
        return pig_latin

    
    def _get_random_word(self):
        return random.choice(list(self.input_dict))
    
if __name__ == '__main__':
    main()
