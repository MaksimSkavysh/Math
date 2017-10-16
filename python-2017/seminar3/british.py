import argparse
import re
import random
import collections as col


def shuffle(text, is_random):
    #print text
    all_words_and_delimiters = re.split('(\W+)', text)
    updated_text = list()
    ordered_dictionaries = [col.OrderedDict(zip(range(len(all_words_and_delimiters)), word)) for word in all_words_and_delimiters]
    for dictionary in ordered_dictionaries:
        dict_length = dictionary.__len__()
        if dict_length > 3 and not(re.match('\W+', dictionary.get(0))):
            seq = [dictionary.get(i) for i in xrange(1, len(dictionary)-1)]
            updated_text.append(''.join(dictionary.get(0)) + ''.join(letters_reshuffle(is_random, seq)) + ''.join(dictionary.get(len(dictionary)-1)))
        else:
            updated_text.append(''.join(dictionary.values()))
    return ''.join(updated_text)


def letters_reshuffle(is_random, seq):
    if is_random:
        random.shuffle(seq)
    elif not is_random:
        seq.sort()
    return seq


#some_text = 'I][{} Just?need!to|retrieve;the id;associated^to(the)last/insertion:Who;can.help?'
#print shuffle(some_text, False)

parser = argparse.ArgumentParser(description="shuffle letters in words")
#parser.add_argument('file', help="file with words which letters will be shuffled", type=argparse.FileType())
parser.add_argument("name", help="text for shuffle letters in each word", type=str)
parser.add_argument("is_random", help="random mode otherwise will be sorting", type=bool)
args = parser.parse_args()

print shuffle(args.name, args.is_random)

