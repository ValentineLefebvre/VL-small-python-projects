from random import randint

#Lists of english words for the game. Easy: 4 letters, medium: 6 letters, hard: 8 letters.
Easy_words = ['wolf','bird','roof','blue','dark','pink','grey','duck','milk','book','moon','rain','luck','leaf','tree','shoe','foot','neck','ring','shop','coat','hawk','hand','foot','king','plum','vest','jedi','sith']
L4 = len(Easy_words)
Medium_words = ['purple','monday','friday','sunday','lawyer','mirror','citrus','orange','tomato','coffee','burger','brunch','kitten','monkey','pillow','violin','flower','sponge','pencil','finger','mother','father','parent','sister','falcon','second','minute','hour','disney','hobbit','memory','bottle']
L6 = len(Medium_words)
Hard_words = ['saturday','thursday','elephant','hogwarts','sunlight','werewolf','hairclip','hairband','children','mountain','souvenir','necklace','question','aircraft','handball','triangle','football','kangaroo','baseball','swimming','hogwarts','calendar','daughter']
L8 = len(Hard_words)

#Listes de mots français pour le jeu. Faciles : 4 lettres, moyens : 6 lettres, difficiles : 8 lettres.
Mots_faciles = ['loup','nuit','jour','chat','toit','gris','bleu','noir','rose','vert','brun','roux','lait','kiwi','paix','chou','ciel','lune','cuir','jupe','mere','pere','fils','moto','velo','pull','yoyo','rond','jedi','sith']
T4 = len(Mots_faciles)
Mots_moyens = ['violet','ananas','orange','citron','fraise','agrume','legume','quiche','samedi','poulet','python','brosse','miroir','oiseau','chaton','boucle','camion','maison','tennis','basket','marron','soleil','etoile','souris','violon','disney','hobbit','foudre','bonnet','raisin','casque','walabi','masque','gouter','chaise','gateau','bateau','rateau','mouton','girafe','faucon','enfant','minute']
T6 = len(Mots_moyens)
Mots_difficiles = ['peinture','elephant','vendredi','mercredi','dimanche','chouchou','portable','pantalon','chausson','dejeuner','baguette','capuchon','pingouin','chouette','montagne','lunettes','souvenir','triangle','question','albatros','handball','football','poudlard','baseball']
T8 = len(Mots_difficiles)

#En: Ascci-art used to show the hangman and complete it after each mistake.
#FR : Ascii-art utilisé pour afficher le pendu et le compléter au fur et à mesure des erreurs.
hangman = ['''
      
      
      
      
      
      
=========''','''
      +
      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


#En: This function checks whether a letter is present in a string. It can also check whether an element is present in an array.
#Fr : Cette fonction vérifie si une lettre est présente dans une chaine de caractères. Elle peut également vérifier si un élément est présent dans une liste.
def is_it_in_the_string(letter,string):
    if string == "" :
        return False
    i = 0
    while i < len(string):
        if letter == string[i]:
            return True
        else:
            i = i + 1
    return False

#En: This function counts the number of occurences of a letter in a string.
#Fr : Cette fonction compte le nombre d'apparitions d'une lettre dans une chaîne de caractères.
def how_many(letter,string) :
    count = 0
    i = 0
    while i < len(string):
        if letter == string[i]:
            count = count + 1
        i = i + 1
    return count

#En: This functions shows the number of letters composing the secret word, as well as the letters already discovered.
#FR : Cette fonction affiche le nombre de lettres du mots à deviner, ainsi que les lettres déjà découvertes.
def show_word(word,good_guesses):
    i = 0
    show = ''
    while i < len(word) :
        if is_it_in_the_string(word[i],good_guesses) :
            show = show + word[i] + ' '
        else :
            show = show + '_ '
        i = i + 1
    return show


#En: Main menu letting the player choose the game language.
#Fr : Menu principal permettant de choisir la langue de jeu.
def hangman_game_language_menu():
    language = 'choose'
    while language != "english" and language != "francais" :
        print("In which language do you want to play? english / francais (mind the orthograph)")
        print("En quelle langue voulez vous jouer ? english / francais (attention à l'orthographe)")
        language = input()
    if language == "english" :
        return hangman_english()
    else :
        return hangman_french()





#En: game's main function, in english
#Fr : fonction principale du jeu, en anglais
def hangman_english():      #En: All comments for this function will be in english. / Fr : Tous les commentaires pour cette fonction seront en anglais.
    #Choice of the level, determined by the number of letters in the hidden word.
    level = 0
    while not is_it_in_the_string(level, ["1","2","3"]) :
        level = input("Which level do you want to try ? 1 : 4-letter words / 2 : 6-letter words / 3 : 8-letter words (Type the corresponding digit)\n")
    level = int(level)
    if level == 1 :
        words_list = Easy_words
        L_list = L4
        L_words = 4
    elif level == 2 :
        words_list = Medium_words
        L_list = L6
        L_words = 6
    else :
        words_list = Hard_words
        L_list = L8
        L_words = 8

    #Beginning of the game, initializing.
    secret_word = words_list[randint(1,L_list-1)]
    errors = 0
    wrong_guesses = ""
    good_guesses = ""
    guesses = ""                    #This variable will contain every letter proposed by the player, whether it was a good or wrong guess.
    hidden = L_words
    print("You lose if you make 10 mistakes.")

    #Body of the game.
    while errors < 10 and hidden > 0 :
        #We show useful informations to the player before asking him for a letter.
        print(show_word(secret_word,good_guesses))
        if guesses != "" :                                              #We don't show the letters already tried during the first turn, as the string is empty.
            print('You have made', errors, 'mistake(s) until now.')
            if errors != 0 :                                            #We don't show the hangman if the player hasn't made a mistake yet.
                print (hangman[errors-1])
            print("you have already tried those letters: " + guesses)
        
        #Time to ask the player for a letter.
        guess = '  '
        while len(guess) != 1 :
            guess = input("Which letter do you want to try out? Type one letter.\n")
            guess = guess.lower()
        
        #We check whether the letter is part of the hidden word or not.
        if is_it_in_the_string(guess, guesses) == False :
            if is_it_in_the_string(guess, secret_word) :
                print("\n\nYes! Good guess!")
                good_guesses = good_guesses + ' ' + guess               #We add the new letter to the string of good guesses.
                hidden = hidden - how_many(guess,secret_word)
            else :
                print("\n\nSorry, wrong guess.")
                wrong_guesses = wrong_guesses + ' ' + guess             #We add the new letter to the string of wrong guesses.
                errors = errors + 1
        else :
            print("\n\nYou have already tried this letter.")            #Submitting the same letter again doesn't count as a mistake.
        guesses = wrong_guesses + good_guesses                          #We update the string of guesses.
    
    #End of game, when the player has done 10 mistakes or found the hidden word.
    if errors == 10 :
        result = "\nYou're dead. The hidden word was " + secret_word + "."
    elif hidden <= 0 :
        result = "\nYou won! The hidden word was indeed " + secret_word + "."
    else :
        result = "\n\nError: shouldn't have left the 'while'.\n"
    print(result)

    #We offer to play again.
    new_game = -1
    while new_game != 0 and new_game != 1 :
        new_game = int(input("Do you want to play again? Enter 0 for No and 1 for Yes. (You have to quit to change language.)\n"))
    if new_game == 1 :
        return hangman_english()
    else :
        return "End of game."







#En: game's main function, in french
#Fr : fonction principale du jeu, en français
def hangman_french():               #En: All comments for this function will be in french. / Fr : Tous les commentaires pour cette fonction seront en français.
    #Choix du niveau, determiné par le nombre de lettres du mot à trouver.
    level = 0
    while not is_it_in_the_string(level, ["1","2","3"]) :
        level = input("Quel niveau voulez-vous tenter ? 1 : mots de 4 lettres / 2 : mots de 6 lettres / 3 : mots de 8 lettres (Entrez le chiffre correspondant.)\n")
    level = int(level)
    if level == 1 :
        words_list = Mots_faciles
        L_list = T4
        L_words = 4
    elif level == 2 :
        words_list = Mots_moyens
        L_list = T6
        L_words = 6
    else :
        words_list = Mots_difficiles
        L_list = T8
        L_words = 8

    #Début du jeu, initialisation.
    secret_word = words_list[randint(1,L_list-1)]
    errors = 0
    wrong_guesses = ""
    good_guesses = ""
    guesses = ""                    #Cette variable contiendra toutes les lettres proposées par le joueur, les bonnes comme les mauvaises.
    hidden = L_words
    print("Vous perdez si vous faites 10 erreurs.")
    
    #Corps du jeu.
    while errors < 10 and hidden > 0 :
        #On affiche les informations utiles au joueur avant de lui demander une lettre.
        print(show_word(secret_word,good_guesses))
        if guesses != "" :                                              #On n'affiche pas les lettres proposées au premier tour, puisque la chaine de caractères est vide.
            print('Vous avez fait', errors, 'erreur(s) pour le moment.')
            if errors != 0 :                                            #On n'affiche pas le pendu si le joueur n'a pas encore fait d'erreur.
                print (hangman[errors-1])
            print("Vous avez essayé les lettres suivantes : " + guesses)
        
        #Il est temps de demander une lettre au joueur.
        guess = '  '
        while len(guess) != 1 :
            guess = input("Quelle lettre voulez-vous proposer ? Tapez une seule lettre, sans accent.\n")
            guess = guess.lower()
        
        #On teste si la lettre proposée fait partie du mot caché ou non.
        if is_it_in_the_string(guess, guesses) == False :
            if is_it_in_the_string(guess, secret_word) :
                print("\n\nOui ! Cette lettre est dans le mot !")
                good_guesses = good_guesses + ' ' + guess               #On ajoute la lettres à la chaine des lettres devinées.
                hidden = hidden - how_many(guess,secret_word)
            else :
                print("\n\nDésolé, cette lettre n'est pas dans le mot.")
                wrong_guesses = wrong_guesses + ' ' + guess             #On ajoute la lettres à la chaine des lettres erronées.
                errors = errors + 1
        else :
            print("\n\nVous avez déjà essayé cette lettre.")            #Proposer plusieurs fois la même lettre ne compte pas comme une erreur.
        guesses = wrong_guesses + good_guesses                          #On met à jour la chaine des lettres proposées.
    
    #Fin du jeu, quand le joueur a fait 10 erreurs ou a trouvé le mot caché.
    if errors == 10 :
        result = "\nVous êtes mort. Le mot caché était " + secret_word + "."
    elif hidden <= 0 :
        result = "\nVous avez gagné ! Le mot caché était bien " + secret_word + "."
    else :
        result = "\n\nHeu... Houston, nous avons un problème.\n"
    print(result)
    
    #On propose de rejouer.
    new_game = -1
    while new_game != 0 and new_game != 1 :
        new_game = int(input("Voulez-vous continuer à jouer ? Entrez 0 pour Non et 1 pour Oui. (Vous devez quitter pour changer de langue.)\n"))
    if new_game == 1 :
        return hangman_french()
    else :
        return "\nFin de jeu."



print(hangman_game_language_menu())