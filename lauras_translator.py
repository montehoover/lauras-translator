'''
Laura's Translator
Translates from Spanish to English
'''
# To Do: read and write from file to save dict

# a bidirectional dict with a one-to-one relationship between words in
# lang1 and lang2, implemented with two dicts
class LanguageDict(object):
    
    def __init__(self, lang1, lang2, file_name='my_dict.txt'):
        self.lang1 = lang1
        self.lang2 = lang2
        self.file_name = file_name
        self.l1_to_l2 = {} #dict mapping words in lang1 to words in lang2
        self.l2_to_l1 = {} #dict mapping words in lang2 to words in lang1
        self.read_from_file()
        
    # insert a pair of words so that there is a one-to-one relationship     
    def insert(self, lang1word, lang2word):
        # To Do: check to ensure one-to-one relationship remains intact
        self.l1_to_l2[lang1word] = lang2word
        self.l2_to_l1[lang2word] = lang1word
        
    # returns the translation of a word, and the str representation of
    # the language it is returned in    
    def get_word(self, word):
        # To Do: appropriately deal with cases where a word is in both
        # languages (esp. if it means different things in each)
        if word in self.l1_to_l2:
            return self.l1_to_l2[word], self.lang2
        elif word in self.l2_to_l1:
            return self.l2_to_l1[word], self.lang1
        else:
            return '', ''
        
    def get_lang1(self):
        return self.lang1
        
    def get_lang2(self):
        return self.lang2
        
    def read_from_file(self):
        # TODO: Ensure read file is in correct format for this
        with open(self.file_name, 'r') as f:
            s = f.read()
            if ('\n\n' in s) & ('>>' in s):
                self.l1_to_l2 = {w.split('>>')[0]: w.split('>>')[1]
                                 for w in s.split('\n\n')[0].split('\n')}
                self.l2_to_l1 = {w.split('>>')[0]: w.split('>>')[1]
                                 for w in s.split('\n\n')[1].split('\n') if w}
            
    def save_to_file(self):
        if self.l1_to_l2:
            with open(self.file_name, 'w') as f:
                for k in self.l1_to_l2:
                    f.write('{0}>>{1}\n'.format(k, self.l1_to_l2[k]))
                f.write('\n')
                for k in self.l2_to_l1:
                    f.write('{0}>>{1}\n'.format(k, self.l2_to_l1[k]))


def do_translation(d):
    w = input('Enter the word to tranlsate: ').strip().lower()
    trans, lang = d.get_word(w)
    if trans:
        print('The ' + lang + ' word for "' + w + '" is ' + trans)
    else:
        print('Sorry, we could not find a translation for "' + w + '"')

    
def get_word(language):
    get_input = True
    while get_input:
        word = input('Enter the word in ' + language + ': ').strip()
        if word == '1':
            break
        confirm = input('You entered "' + word
                        + '".  Is this correct?').strip().lower()
        if confirm not in ['y', 'yes']:
            print('Ok, "' + word + '" is not correct. Let\'s try again.')
        else: 
            get_input = False    
    return word.lower()    

def add_to_dict(d):
    print('\nYou chose to add a word to the translator.')
    print('Type "1" at any time to cancel and return to the main menu.')
    l1word = get_word(d.get_lang1())
    if l1word == '1':
        return d
    l2word = get_word(d.get_lang2())
    if l2word == '1':
        return d
    d.insert(l1word, l2word)
    return d
    
        
def main_menu(lang_dict):
    while True:
        command = input("""\nEnter a number 1-3 for your choice from the menu: 
        1. Translate a word 
        2. Add a word to the {0}-{1} translator
        3. Exit
        >>""".format(lang_dict.get_lang1(), lang_dict.get_lang2()))
        if command.strip() in ['1', '1.']:
            do_translation(lang_dict)
        elif command.strip() in ['2', '2.']:
            lang_dict = add_to_dict(lang_dict)
        elif command.strip() in ['3', '3.']:
            print("Thank you for using the translator!\n")
            lang_dict.save_to_file()
            break
        else:
            print("Did not recognize your choice.  Please enter a number 1-3.")
    
print("\nWelcome to the Spanish-English Translator!")
print("You can translate a word from Spanish to English or vice versa.")
d = LanguageDict("Spanish", "English")
main_menu(d)
        