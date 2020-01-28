from datetime import datetime
import random
now = None
HOUR = 0
MINUTE = 0
SECOND = 0
correct = 0
total = 0
words_in_sentence = 0
sentence_words = []
words = []
sentence = ""
def set_original_time():
    global now, HOUR, MINUTE, SECOND
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    HOUR = int(now.strftime("%H"))
    MINUTE = int(now.strftime("%M"))
    SECOND = int(now.strftime("%S"))
    
def get_time():
    global HOUR, MINUTE, SECOND
    """
    Returns amount of time since the 'now' variable was set
    """
    current = datetime.now()
    current_time = current.strftime("%H:%M:%S")
    hour = int(current.strftime("%H"))
    minute = int(current.strftime("%M"))
    second = int(current.strftime("%S"))
    
    hours_gone = str(hour - HOUR)
    min_gone = str(minute - MINUTE)
    secs_gone = str(second - SECOND)
    
    return str(hours_gone + ":" + min_gone + ":" + secs_gone)

possible_words_lowercase = ["banana", "apple", "toyota", "canada", "monkey", "archbishop", "bishop", "and", "is", "or", "computer", "programming",
                            "asian","white","black","brown", "add", "more","word","words","sword","jewish","bored","eating","eats","english", "sucks"] #add more words for more difficult tests

def get_hour(string): #returns whole hours since the user started the test. This, by default will not return minutes or seconds, as they will not return whole hours.
    l = string
    hour = ""
    for i in range(len(l)):
        if l[i] == ":":
            return hour
        else:
            hour = hour + l[i]

def get_min(string): #returns minutes since the user started the test, does not transfer hours to minutes, or seconds to minutes
    l = string
    minute = ""
    shown = 0
    for i in range(len(l)):
        if l[i] == ":" and shown == 1:
            if int(minute) < 0:
                return 0
            return minute
        elif shown == 1:
            minute = minute + l[i]
        elif l[i] == ":":
            shown += 1

def get_sec(string): #returns seconds since the user started the test, does not transfer minutes or hours to seconds
    l = string
    sec = ""
    shown = 0
    for i in range(len(l)):
        if shown == 2:
            sec = sec + l[i]
        elif l[i] == ":":
            shown += 1
    return sec

def evaluate_input(string):
    global correct,total,words_in_sentence,sentence_words,words,sentence
    """ Check to see if it matches 100% """
    if string == sentence:
        correct = words_in_sentence
        for i in range(len(sentence_words)):
            current = sentence_words[i]
            for y in range(len(current)):
                total += 1
        return
    else:
        current = ""
        for i in range(len(string)):
            if string[i] == " ":
                words.insert(len(words),current)
                current = ""
                total += 1
            else:
                current = current + string[i]
                total += 1
                if i == len(string) - 1:
                    words.insert(len(words), current)
                    current = ""
        """ Evaluate the words which have been deciphered, ignoring whitespaces """
        for i in range(len(words)):
            if words[i] == sentence_words[i]:
                correct += 1
            else:
                # See if any part of the word, starting at beginning is the same, stopping when it is not.
                part = 0
                for x in range(len(words[i])):
                    c = words[i]
                    d = sentence_words[i]
                    if c[x] == d[x]:
                        part = x/len(words[i])
                    else:
                        break
                if part > 0:
                    correct += (part / len(c))
        print(correct)

def present_sentence(type_):
    global possible_words_lowercase, possible_words, correct, total, words_in_sentence, sentence_words, words, sentence
    location = 0 #default
    if type_ == 1: #lowercase
        words_in_sentence = 10
        for y in range(10):
            location = random.randint(0,len(possible_words_lowercase)-1) # location in the list of lowercase words
            if y != 9: 
                sentence = sentence + possible_words_lowercase[location] + " " #add the word from location above to the sentence, include a space.
                sentence_words.insert(len(sentence_words),possible_words_lowercase[location])
            else:
                sentence = sentence + possible_words_lowercase[location]
                sentence_words.insert(len(sentence_words),possible_words_lowercase[location])
        print(sentence)
        user_input = input(">> ") #ask user to type in the outputted sentence above
        print(f"{len(user_input)} : input length -- {len(sentence)} : sentence length")
        current_word = ""
        """  NEED TO GET HOW ACCURATE THE USER IS  """
        evaluate_input(user_input)
        time_ = get_time()
        print(f"You completed this test in {time_} (H/M/S)")
        print(f"You were {(correct/words_in_sentence)*100}% accurate!")
        print(f"Words entered: {words}")
        H = int(get_hour(time_))
        M = int(get_min(time_))
        S = int(get_sec(time_))
        seconds_taken = (H * 60 * 60) + (M * 60) + S
        print(f"Your WPM is: {(total/correct)/(seconds_taken/60)}") #WILL THROW ERROR
        

def start_test(type_): #is redundant
    if type_ == 1: #lowercase only
        set_original_time()
        present_sentence(1)
    elif type_ == 2: #Full sentences, punctuation, capitalisation
        set_original_time()
        present_sentence(2)
    else: #Full sentences, punctuation, lowercase
        set_original_time()
        present_sentence(3)

""" Only type 1 works, which is why it is hard-coded. """
start_test(1)
