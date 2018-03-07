# import twitter

# api = twitter.Api(consumer_key='consumer_key',
#     consumer_secret='consumer_secret',
#     access_token_key='access_token',
#     access_token_secret='access_token_secret')

# print(api.VerifyCredentials())

"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    our_file = open(file_path)
    #print our_file.read()
    return our_file.read()
    #string_of_file = str(file_path)





def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """
    chains = {}
    # Put str into list
    words = text_string.split()

    #iterate over words
    # for index in range(len(words)):
    #     if index <= len(words)-3:  # Make sure there is enough words to create values
    # # Put str into list
    #         words = text_string.split()
    #         print words
    #iterate over words
    for index in range(len(words)):
        if index <= len(words)-4:
            trigram_word1 = words[index]
            trigram_word2 = words[index + 1]
            trigram_word3 = words[index + 2]
    #     #add two words to a tuple
            words_in_tuple = (trigram_word1, trigram_word2, trigram_word3)
            next_word = words[index + 3]
            # check if words_in_tuple in dictionary:
            if words_in_tuple in chains:
            # if it is: update the value:
                chains[words_in_tuple].append(next_word)
            # create new key-value pair
            else:
                chains[words_in_tuple] = [next_word]
    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    keys_in_chains = chains.keys()
    #look up key in dictionary
    link = choice(keys_in_chains)  # a tuple from the dictionary chains
    # get a link - (pair_word_1, pair_word2) and append these words to the words list
    words.extend(link)
    #print "This is link", link
    #print "This is words before the while loop ", words
    # start of loop

    while len(words) < len(keys_in_chains):
        link = choice(keys_in_chains)
        #print "This is link after choice ", link
        words.extend(link)
        #print "This is words after link has been added ", words
        # get random_new_word from the list of words that follows the link by picking any index from the list that is equal to or less than the length.
        random_new_word = choice(chains[link])
        #append random_new_word to words list
        words.append(random_new_word)
        # create a new key, which is a tuple (pair_word2, random_new_word)
        link = (link[2], random_new_word, random_new_word)
        #print "This is link at end of while loop ", link

    #print "This is words list", words
    joined_words = " ".join(words)
    print "-------"
    sliced_words = joined_words[0:140]
    print sliced_words
    return sliced_words


################## The functions get called down below ####################
input_path = "Combined_text.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print random_text
