from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Gameapp
import random
import string
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
image_list = ['correct1', 'correct2', 'correct3', 'correct4', 'correct5']
#my_file = os.path.join(THIS_FOLDER, 'car.txt')


def category(request):
    if request.method == 'POST':
        global file_name
        file_name = request.POST['category_key'].lower()
        global my_file
        my_file = os.path.join(THIS_FOLDER, file_name+".txt")
        return redirect('home/category='+file_name)
    return render(request, 'gameapp/category.html')

def get_word():
    global no_of_tries
    global alphabet_dict
    alphabet_dict = {}
    no_of_tries = 7
    file = open(my_file,'r')
    file_content = file.readlines()
    word = random.choice(file_content).strip().upper()
    return word

def home(request):
    if request.method == 'GET':
        random_word = get_word()
        #display_word = '_ '*len(random_word)
        display_word = get_display_word(random_word, [])
        game = Gameapp(random_word = random_word, display_word = display_word)
        game.image = "/static/images/start.jpg"
        game.save()
        return render(request, 'gameapp/home.html', {'game':game, 'no_of_tries':no_of_tries, 'file_name':file_name})
    else:
        return get_input(request)

def get_input(request):
    game_id = int(request.POST['game_id'])
    game = Gameapp.objects.get(id=game_id)

    guess = request.POST['alphabet_key']
    guessed = list(game.guessed)
    wrong = list(game.wrong)

    global alphabet_dict
    global alphabet_visibility_status

    alphabet_dict[guess+"disable"] = "true"

    global no_of_tries

    if game.status == "win" or game.status == "lose":
        generate_finished_game(game)
        #return render(request, 'gameapp/home.html', {'guessed':guessed, 'wrong': wrong, 'game':game})
        return redirect('home')
    else:
        if guess in game.random_word:
            guessed.append(guess)
            correct_choice_image = random.choice(image_list)
            game.image = "/static/images/" + correct_choice_image + ".gif"
        else:
            no_of_tries = no_of_tries - 1
            wrong.append(guess)
            game.image = "/static/images/" + str(no_of_tries) + ".gif"

        display_word = get_display_word(game.random_word, guessed)
        if no_of_tries > 0 and display_word.strip() == " ".join(game.random_word):
            game.status = "win"
            game.image = "/static/images/win.gif"
        elif no_of_tries == 0:
            game.status = "lose"

        game.display_word = display_word
        game.alphabet_key = guess
        game.guessed = "".join(guessed)
        game.wrong = "".join(wrong)
        game.save()
        return render(request, 'gameapp/home.html', {'guessed':guessed, 'wrong': wrong, 'no_of_tries':no_of_tries, 'alphabet_dict':alphabet_dict, 'file_name':file_name, 'game':game})

def get_display_word(random_word, guessed):
    display_word = ""
    for letter in random_word:
            if letter not in string.ascii_uppercase:
                display_word = display_word + letter + " "
            elif letter in guessed:
                display_word = display_word + letter + " "
            else:
                display_word = display_word + "_ "
    return display_word

def generate_finished_game(game):
    if game.status == "win":
        game.display_word = game.random_word
        game.save()
        return
    elif game.status == "lose":
        game.display_word = game.display_word
        game.save()
        return
