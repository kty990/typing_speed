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

possible_words_lowercase = ["banana", "apple", "toyota", "canada", "monkey", "archbishop", "bishop", "and", "is", "or", "computer", "programming"] #add more words for more difficult tests

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

def present_sentence(type_):
    global possible_words_lowercase, possible_words, correct, total, words_in_sentence, sentence_words, words
    location = 0 #default
    if type_ == 1: #lowercase
        words_in_sentence = 10
        sentence = ""
        for y in range(10):
            location = random.randint(0,len(possible_words_lowercase)-1) # location in the list of lowercase words
            if y != 9: 
                sentence = sentence + possible_words_lowercase[location] + " " #add the word from location above to the sentence, include a space.
                sentence_words.insert(len(sentence_words),possible_words_lowercase[location] + " ")
            else:
                sentence = sentence + possible_words_lowercase[location]
                sentence_words.insert(len(sentence_words),possible_words_lowercase[location])
        print(sentence)
        user_input = input(">> ") #ask user to type in the outputted sentence above
        print(f"{len(user_input)} : input length -- {len(sentence)} : sentence length")
        current_word = ""
        for i in range(0, len(user_input)):
            """
            Goes through the user's input to determine how accurate they were when typing the sentence, or string of words provided.
            """
            print(f"{i} : i -- {len(user_input)} : input")
            current_word = current_word + user_input[i]
            if (i == len(user_input) - 1): #redo section
                print(f"LIMIT")
                c_w = ""
                total = len(current_word)
                for i in range(len(current_word)):
                    print(i)
                    if current_word[i] != " " and i != len(current_word) - 1:
                        c_w = c_w + current_word[i]
                    else:
                        words.insert(len(words), c_w)
                        words.insert(len(words), " ")
                        print(f"Inserted {c_w} into words list!")
                        c_w = ""
                starting_index = 0
                for i in range(len(words)):
                    ending_index = len(words[i]) + starting_index
                    if words[i] == sentence[starting_index:ending_index] and len(words[i]) == len(sentence_words[i]):
                        correct += 1
                    elif words[i] == sentence[starting_index:ending_index]:
                        correct += (1/(len(sentence_words[i]) - len(words[i])))
                    starting_index = ending_index + 1
            elif user_input[i+1] == " ":
                print(f"SPACE")
                total += len(current_word)
                length = len(current_word)
                start = i - length
                end = i+1
                words.insert(len(words), current_word)
                if sentence[start:end] == current_word:
                    correct +=1
                    print(f"Is correct: {sentence[start:end]}")
                else:
                    print(f"{current_word} at location {start} - {end-1} is not found at that location in the sentence")
                current_word = ""
            elif user_input[i] == sentence[i] and user_input[i] != " ":
                print(f"NON SPACE {user_input[i]}")
        correct == correct//words_in_sentence
        time_ = get_time()
        print(f"You completed this test in {time_} (H/M/S)")
        print(f"You were {(correct/words_in_sentence) * 100}% accurate!")
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

start_test(1)