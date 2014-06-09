import operator


def generate_alphabet():
    alphabet={}
    letters=range(ord('a'),ord('z')+1)
    for item in letters:
        alphabet[chr(item)]=0
    return alphabet


def read_text(text_file):
    f = open(text_file)
    filetext = f.read()
    file_text_lowercase=filetext.lower()
    char_list=list(file_text_lowercase)
    return char_list

def count_letters(char_list):
    letter_tallies=generate_alphabet()
    for char in char_list:
        if char in letter_tallies:
            letter_tallies[char]+=1
    return letter_tallies

def print_letters(letter_tallies):
    sorted_tallies = sorted(letter_tallies.iteritems(), key = operator.itemgetter(0))
    for tally in sorted_tallies:
        print tally[0], tally[1]

         
def main():
    char_list=read_text('twain.txt')

    letter_tallies=count_letters(char_list)

    print_letters(letter_tallies)




if __name__ == '__main__':
    main()
