from random import randint

#Lists of english words for the game. Easy: 3 letters, medium: 4 letters, hard: 5 letters.
Easy_words = ['you','eat','tea','end','ask','bag','bed','bin','big','sad','cat','dog','cow','pet','fox','ape','sky','sun','sea','boy','law','pen','pan','pea','fat']
Medium_words = ['kiss','food','meat','tear','wolf','bird','bear','lion','pony','roof','blue','dark','pink','grey','duck','milk','book','moon','rain','luck','leaf','tree','shoe','foot','neck','ring','shop','coat','hawk','hand','foot','king','plum','vest','jedi','sith','girl','dirt']
Hard_words = ['happy','spoon','sushi','pizza','quick','pasta','eagle','table','brown','black','white','lunch','peach','shine','stone','space','earth','money','phone','light','heavy']
 
#Listes de mots français pour le jeu. Faciles : 3 lettres, moyens : 4 lettres, difficiles : 5 lettres.
Mots_faciles = ['lac','loi','moi','toi','roi','fou','lui','nez','mon','ton','son','dur','mou','fin','fil','eau','riz','bas','air','bar','sol','ski','rue','vie','nez','lin','las','lys']
Mots_moyens = ['tour','dame','pion','haut','loup','nuit','jour','ciel','lune','chat','paon','lion','ours','toit','suie','tutu','pull','luge','gris','bleu','noir','rose','vert','brun','roux','lait','kiwi','paix','chou','pois','cuir','jupe','mere','pere','fils','moto','velo','pull','yoyo','rond','jedi','sith','pale','bois']
Mots_difficiles = ['pluie','coeur','livre','pomme','ferme','barre','plume','prune','poire','bille','tuile','chien','puits','stylo','bisou','blanc','beige','rubis','lilas','lasse','lisse']

 
#En: Main menu.
#Fr : Menu principal.
def main_menu():
    print("\n\nEn: Do you want to play right away or read the rules first ? Enter 'P' or 'J' to play and 'R' to read the rules.")
    print("Fr : Voulez-vous jouer tout de suite ou lire les règles d'abord ? Tapez 'P' ou 'J' pour jouer et 'R' pour lire les règles.")
    choice = ""
    while choice != "P" and choice != "J" and choice != "R" :
        choice = input()
        choice = choice.upper()
    if choice == "R" :
        return rules()
    else :    
        return language_menu()


#En: Short explanation of the game's rules.
#Fr : Courte explication des règles du jeu.
def rules():
    print("\nEn: Rules \nThis game counts three levels. Each round, you will be given letters and will have to find three words using those letters - and only those. The same letter can be used several times. You can also write 'quit' to give up the round. If you have found at least one word, you rise to the next level. You win one point for each word you found.")
    print("\nFr : Règles \nCe jeu comporte trois niveaux. À chaque manche, il vous sera proposé une liste de lettres et vous devrez trouver trois mots à partir de ces lettres - et uniquement celles-là. Les lettres avec accent ne sont pas prises en compte. La même lettre peut être utilisée plusieurs fois. Vous pouvez aussi écrire 'quit' pour abandonner la manche. Si vous avez trouvé au moins un mot, vous passez au niveau suivant. Vous gagnez un point pour chaque mot trouvé.\n")
    return language_menu()


#En: Menu letting the player choose the game language.
#Fr : Menu permettant de choisir la langue de jeu.
def language_menu():
    language = 'choose'
    while language != "english" and language != "francais" :
        print("En: In which language do you want to play? english / francais (mind the orthograph)")
        print("Fr : En quelle langue voulez vous jouer ? english / francais (attention à l'orthographe)")
        language = input()
    if language == "english" :
        return game_english()
    else :
        return game_french()


#En: This function checks whether an element is present in an array.
#Fr : Cette fonction vérifie si un élément est présent dans une liste.
def is_it_in_the_array(element,array):
    if array == "" :
        return False
    i = 0
    while i < len(array):
        if element == array[i]:
            return True
        else:
            i = i + 1
    return False



#En: This function shuffles the letters making the hidden words and remove those which appear twice.
#Fr : Cette fonction mélange les lettres des mots cachés et retire celles qui apparaissent deux fois.
def shuffle_and_remove_doubles(words_array):
    #En: I stick the hidden words together into one string, in order to separate the letters afterwards.
    #Fr : Je colle les mots cachés à la suite dans une chaîne de caractères, pour isoler les lettres ensuite.
    words_in_a_string = ""
    i = 0
    while i < len (words_array):
        words_in_a_string = words_in_a_string + words_array[i]
        i = i + 1
    #En: I put the letters back into an array because the "del" function doesn't work on strings.
    #Fr : Je remets les lettres dans une liste car la fonction "del" ne fonctionne pas sur les chaînes de caractères.
    full_array =[]
    j = 0
    while j < len (words_in_a_string):
        full_array.append(words_in_a_string[j])
        j = j + 1
    #En: I shuffle the letters from full_array and delete the doubles.
    #Fr : Je mélange les lettres de full_array et je supprime les doublons.
    shuffled_short_array = []
    while len(full_array) >= 1:
        L = len(full_array)
        random_index = randint(0, L-1)
        if not is_it_in_the_array(full_array[random_index],shuffled_short_array):
            shuffled_short_array.append(full_array[random_index])
        del(full_array[random_index])
    #En: I stick the letters together into one string so that it will look better when shown to the player.
    #Fr : Je colle les lettres dans une chaîne de caractères, pour que ce soit plus joli à afficher.
    shuffled_short_string = ""
    k = 0
    while k < len (shuffled_short_array):
        shuffled_short_string = shuffled_short_string + shuffled_short_array[k]
        k = k + 1
    return shuffled_short_string



#En: Game's main function, in english. All comments for this function will be in english.
#Fr : Fonction principale du jeu, en anglais. Tous les commentaires pour cette fonction seront en anglais.
def game_english():
    level = 1
    total_points = 0
    while level <= 3 :
        level_points = 0
        print("\nLevel", level)
        #The array in which the words are selected depends on the level reached by the player. I add a new variable because I am going to delete words from it and I don't want them to be deleted from the original array.
        if level == 1 :
            big_array = Easy_words
        elif level == 2 :
            big_array = Medium_words
        else :
            big_array = Hard_words
        secret_words =[]
        i = 0
        while i < 3:
            L = len(big_array)
            random_index = randint(0,L-1)                   #Hidden words are picked randomly among the words from big_array.
            secret_words.append(big_array[random_index])    #They are stored in the array secret_words.
            del(big_array[random_index])                    #I delete them from big_array to be sure that the same one won't be picked twice.
            i = i + 1
        letters = shuffle_and_remove_doubles(secret_words)  #Those are the letters that will be shown to the player.
        quit = 0
        while secret_words != [] and quit == 0 :            #The round is over when the player finds all three hidden words or quits. The number of tries is unlimited.
            print("You have to find", len(secret_words),"word(s) using those letters:",letters)
            print("Try a",len(secret_words[0]),"letters word.")
            guess = input()
            guess = guess.lower()                           #I switch the player's proposition to lowercase to compare it with the hidden words.
            j = 0
            good_guess = 0
            while j < len(secret_words) :                   #I compare the player's proposition with the hidden words.
                if guess == secret_words[j]:
                    #When the player finds a hidden word, he earns one point and the word is deleted from the array. This way, he can't earn points twice with the same word and I can show him the remaining words if he quits the round.
                    level_points = level_points + 1
                    del(secret_words[j])
                    print("Yes! Congrats! There is", len(secret_words),"word(s) left to find.")
                    good_guess = 1
                elif guess == "quit":
                    quit = quit + 1
                    good_guess = 1                          #I set good_guess at 1 so as not to activate the "if good_guess == 0 :" below.
                j = j + 1
            if good_guess == 0 :
                print("Sorry. This word isn't among the hidden ones.")      
        total_points = total_points + level_points
        if level_points == 3 :
            print("Congratulations! You found every word of this level. Next level. The words will be longer and, therefore, harder to find.")
            level = level + 1
        elif level_points == 0 :                            #The player doesn't rise to the next level if he didn't find a single word.
            print("You have given up without finding a single word. The hidden words were:",secret_words)
            print("You can stop playing or try this level again. In that case, we will give you new hidden words.")
            try_again = ""
            while try_again != "0" and try_again != "1" :
                try_again = input("Enter 0 to stop playing or 1 to try again.")
                if try_again == "0" :
                    print("End of game. You scored", total_points,"point(s).")
                    return "See you soon!"
        else :
            print("Congratulations! You found", level_points, "word(s) among the three of this level. You still had to find the following word(s):",secret_words)
            level = level + 1
            if level <= 3 :
                print("Next level. The words will be longer and, therefore, harder to find.")
    if level == 4 :             #When the player finishes level 3, the level goes up to 4. It is necessary to leave the first loop of the program.
        level = 3               #I then put it back down to 3 because, if I don't, the text "You reached level 4" will be shown below.
    print("Game is over. You reached level", level,"and found", total_points,"word(s) in total.")
    new_game = ""
    while new_game != "0" and new_game != "1" :
        new_game = input("Do you want to start a new game? Enter 0 to stop playing and 1 to play again.")
    if new_game == "1" :
        return game_english()
    else :
        return "See you soon!"



#En: Game's main function, in french. All comments for this function will be in french.
#Fr : Fonction principale du jeu, en français. Tous les commentaires pour cette fonction seront en français.
def game_french():
    level = 1
    total_points = 0
    while level <= 3 :
        level_points = 0
        print("\nNiveau", level)
        #La liste dans laquelle les mots sont sélectionnés dépend du niveau atteint par le joueur. J'ajoute une nouvelle variable car je vais supprimer des mots de cette liste et je ne veux pas les supprimer de la liste originale.
        if level == 1 :
            big_array = Mots_faciles
        elif level == 2 :
            big_array = Mots_moyens
        else :
            big_array = Mots_difficiles
        secret_words =[]
        i = 0
        while i < 3:
            L = len(big_array)
            random_index = randint(0,L-1)                   #Les mots cachés sont piochés au hasard dans big_array.
            secret_words.append(big_array[random_index])    #Ils sont stockés dans secret_words.
            del(big_array[random_index])                    #Je les supprime de big_array au fur et à mesure pour ne pas avoir 2 fois le même.
            i = i + 1
        letters = shuffle_and_remove_doubles(secret_words)  #Ce sont les lettres qui seront montrées au joueur.
        quit = 0
        while secret_words != [] and quit == 0 :            #La manche se termine quand le joueur a trouvé tous les mots ou quand il quitte. Il a donc un nombre infini d'essais.
            print("Vous devez trouver", len(secret_words),"mot(s) en utilisant ces lettres :",letters)
            print("Proposez un mot de",len(secret_words[0]),"lettres, sans accent.")
            guess = input()
            guess = guess.lower()                           #Je mets la proposition du joueur en minuscules pour comparer avec les mots secrets.
            j = 0
            good_guess = 0
            while j < len(secret_words) :                   #Je compare la proposition du joueur aux mots secrets (leur nombre diminue à chaque fois).
                if guess == secret_words[j]:
                    #Quand le joueur trouve un mot caché, il gagne un point et je supprime le mot de la liste. Ainsi, il ne peut pas gagner 2 points avec le même mot et je peux afficher les mots restants s'il quitte la manche.
                    level_points = level_points + 1
                    del(secret_words[j])
                    print("Oui ! Bravo ! Il vous reste", len(secret_words),"mot(s) à trouver.")
                    good_guess = 1
                elif guess == "quit":
                    quit = quit + 1
                    good_guess = 1                          #Je mets good_guess à 1 pour ne pas activer le "if good_guess == 0 :" plus bas.
                j = j + 1
            if good_guess == 0 :
                print("Désolé. Ce mot ne fait pas partie des mots cachés.")      
        total_points = total_points + level_points
        
        if level_points == 3 :
            print("Bravo ! Vous avez trouvé tous les mots de ce niveau. Niveau suivant. Les mots seront un peu plus longs, donc plus durs à trouver.")
            level = level + 1
        elif level_points == 0 :                            #Le joueur ne monte pas de niveau s'il n'a trouvé aucun mot.
            print("Vous avez abandonné sans trouver le moindre mot. Les mots à trouver étaient :",secret_words)
            print("Vous pouvez arrêter de jouer ou retenter ce niveau. Nous vous proposerons alors de nouveaux mots.")
            try_again = ""
            while try_again != "0" and try_again != "1" :
                try_again = input("Entrez 0 pour arrêter ou 1 pour réessayer.")
                if try_again == "0" :
                    print("Fin du jeu. Vous avez marqué", total_points,"point(s).")
                    return "Au revoir !"
        else :
            print("Bravo ! Vous avez trouvé", level_points, "mot(s) parmi les trois de ce niveau. Vous deviez encore trouver le(s) mot(s) suivant(s) :",secret_words)
            level = level + 1
            if level <= 3 :
                print("Niveau suivant. Les mots seront un peu plus longs, donc plus durs à trouver.")
    if level == 4 :             #Quand on termine le niveau 3, le niveau passe à 4. C'est nécessaire pour sortir de la 1ère boucle du programme.
        level = 3               #Je le redescends à 3 car sinon, la ligne suivante affichera "Vous avez atteint le niveau 4".
    print("Le jeu est terminé. Vous avez atteint le niveau", level,"et trouvé", total_points,"mots en tout.")
    new_game = ""
    while new_game != "0" and new_game != "1" :
        new_game = input("Voulez-vous faire une nouvelle partie ? Entrez 0 pour arrêter ou 1 pour rejouer.")
    if new_game == "1" :
        return game_english()
    else :
        return "Au revoir !"



print(main_menu())
