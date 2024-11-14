import random

def words_choice_level_easy() :

    selected_words = ["maison", "ville", "porte", "route", "homme", "femme", "amour", "voiture"]

    lenght_selected_word = len(selected_words)
    list_of_words_pool = []

    word_1 = selected_words[random.randint(0, lenght_selected_word - 1)]
    selected_words.remove(word_1)
    list_of_words_pool.append(word_1)
    
    word_2 = selected_words[random.randint(0,lenght_selected_word - 2)]
    selected_words.remove(word_2)
    list_of_words_pool.append(word_2)
    
    word_3 = selected_words[random.randint(0,lenght_selected_word - 3)]
    list_of_words_pool.append(word_3)

    return list_of_words_pool

def words_choice_level_medium() :
    
    with open('dictionnaire.txt') as dictionary:
        content = dictionary.read() 
        words = content.split()

    length_dictionary = len(words)

    selected_words = []

    index_word_1 = random.randint(0, length_dictionary - 1)
    index_word_2 = random.randint(0, length_dictionary - 1)
    index_word_3 = random.randint(0, length_dictionary - 1)
    
    word_1 = words[index_word_1]
    word_2 = words[index_word_2]
    word_3 = words[index_word_3]

    while len(word_1) < 4  or len(word_1) > 6 :
        index_word_1 = random.randint(0, length_dictionary - 1)
        word_1 = words[index_word_1]

    while len(word_2) < 4  or len(word_2) > 6 :
        index_word_2 = random.randint(0, length_dictionary - 1)
        word_2 = words[index_word_2]
    
    while len(word_3) < 4  or len(word_3) > 6 :
        index_word_3 = random.randint(0, length_dictionary - 1)
        word_3 = words[index_word_3]

    selected_words.append(word_1)
    selected_words.append(word_2)
    selected_words.append(word_3)
    return selected_words
    

def words_choice_level_hard() :
    
    with open('dictionnaire.txt') as dictionary:
        content = dictionary.read() 
        words = content.split()

    length_dictionary = len(words)

    selected_words = []

    index_word_1 = random.randint(0, length_dictionary - 1)
    index_word_2 = random.randint(0, length_dictionary - 1)
    index_word_3 = random.randint(0, length_dictionary - 1)
    
    word_1 = words[index_word_1]
    word_2 = words[index_word_2]
    word_3 = words[index_word_3]

    selected_words.append(word_1)
    selected_words.append(word_2)
    selected_words.append(word_3)
    return selected_words


def supp_exceed_letter(word_list):
    final_list = []
    
    for letter in word_list:
        if letter not in final_list:
            final_list.append(letter)
    
    return final_list


def merge_words(word_list) :

    merged_word_list = word_list[0] + word_list[1] + word_list[2]
    return merged_word_list


def mix_word(merge_word_list) :

    letter_list = list(merge_word_list)
    lenght_letter_list = len(letter_list)
    
    for i in range(lenght_letter_list) :

        new_placement = random.randint(0, lenght_letter_list - 1)

        letter_list[i], letter_list[new_placement] = letter_list[new_placement], letter_list[i]
        
    mixed_word_list = ''.join(letter_list)
    return mixed_word_list


def win_condition(word,mixed_words_list) :

    lenght = len(mixed_words_list)
    for i in range (0,lenght,1) :
        if mixed_words_list[i] == word :
            return True
    return False

#tester le choix de difficulté  
liste_de_mot = words_choice_level_easy()

def difficulty_choice(difficulty) :

    error_count = 1

    while difficulty != "easy" and  difficulty != "medium" and difficulty != "hard" and error_count < 5:

        difficulty = input()
        error_count = error_count + 1

        if error_count == 2 :
            print("Please tap : 'easy', 'medium' or 'hard'")
            print("Choose your difficulty :")
            print("easy, medium, hard")

        if error_count == 3 :
            print("Fait un effort frère c'est pas dur")
            print("Please tap : 'easy', 'medium' or 'hard'")
            print("Choose your difficulty :")
            print("easy, medium, hard")

        if error_count == 4 :
            print("p'tit con regarde ton écran quand t'écrit")
            print("Please tap : 'easy', 'medium' or 'hard'")
            print("Choose your difficulty :")
            print("easy, medium, hard")

        if error_count == 5 :
            print("t'es trop guez dégage")
            print("you loose")

    return difficulty


def game_round_easy() :
    
    words_to_guess = words_choice_level_easy()
    mix = merge_words(words_to_guess)
    mix = mix_word(mix)
    mix = supp_exceed_letter(mix)

    print("You choose the easy mode !")
    print("If you do not find the words, tap 'skip'")
    print("Find the tree words in this :")
    print(mix)

    points = 0

    while points < 3 :
        
        attempt = input()

        if attempt.lower() == "skip" :
            print("You skip the Round")
            break

        win_condition_result = win_condition(attempt, words_to_guess)
        
        if win_condition_result == True :
            print("Good job, you found a word !")
            points = points + 1 

        if win_condition_result == False :
            print("Wrong, try again")

    if points == 3 :
        print("Wonderfull, you found all the words !")
        return points
    
    else :
        print("You have guessed", points, "word out of 3 this round")
        return points


def game_round_medium() :
    
    words_to_guess = words_choice_level_medium()
    mix = merge_words(words_to_guess)
    mix = mix_word(mix)
    mix = supp_exceed_letter(mix)

    print("You choose the medium mode !")
    print("If you do not find the words, tap 'skip'")
    print("Find the tree words in this :")
    print(mix)

    points = 0

    while points < 3 :
        
        attempt = input()

        if attempt.lower() == "skip":
            print("Round skipped.")
            break

        win_condition_result = win_condition(attempt, words_to_guess)
        
        if win_condition_result == True :
            print("Good job, you found a word !")
            points = points + 1 
        if win_condition_result == False :
            print("Wrong, try again")

    if points == 3 :
        print("Wonderfull, you found all the words !")
        return points

    else :
        print("You have guessed", points, "word out of 3")
        return points
    

def game_round_hard() :
    
    words_to_guess = words_choice_level_hard()
    mix = merge_words(words_to_guess)
    mix = mix_word(mix)
    mix = supp_exceed_letter(mix)

    print("You choose the hard mode !")
    print("If you do not find the words, tap 'skip'")
    print("Find the tree words in this :")
    print(mix)

    points = 0

    while points < 3 :
        
        attempt = input()

        if attempt.lower() == "skip":
            print("Round skipped.")
            break

        win_condition_result = win_condition(attempt, words_to_guess)
        
        if win_condition_result == True :
            print("Good job, you found a word !")
            points = points + 1 
        if win_condition_result == False :
            print("Wrong, try again")

    if points == 3 :
        print("Wonderfull, you found all the words !")
        return points

    else :
        print("You have guessed", points, "word out of 3")
        return points


print("Try to guess the word in it !")
print("Select your difficulty :")
print("easy, medium, hard")

difficulty = input()
difficulty = difficulty_choice(difficulty)

points = 0

round_number = 1
if difficulty == "easy" :
    while round_number <= 3 :
        print("Easy mode round :",round_number)
        points += game_round_easy()
        print("round close")
        round_number = round_number + 1


if difficulty == "medium" :
    while round_number <= 3 :
        print("Medium mode round :",round_number)
        points += game_round_medium()
        print("round close")
        round_number = round_number + 1
        

if difficulty == "hard" :
    while round_number <= 3 :
        print("Hard mode round :",round_number)
        points += game_round_hard()
        print("round close")
        round_number = round_number + 1

if points == 9 :
    print("Congratulation, you win, with a perfect score of", points, "/9")

else :
    print("nice try, your score is ", points, "/9")