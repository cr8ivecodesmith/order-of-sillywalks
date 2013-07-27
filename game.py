#!/usr/bin/python -tt

import story
from re import compile
from random import randint
from time import sleep


def do_battle():

    if randint(1, 10) % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    play_again = True
    no_pattern = compile(r'^n.*')

    # Game loop
    while (play_again):
        print story.intro()
        sleep(1)

        print story.first_scene()
        check_choice = raw_input('Do you fight back? [Y/n]: ')
        fight_back = False if no_pattern.match(check_choice.lower()) else True

        if fight_back:
            print story.first_scene_yes()
        else:
            print story.first_scene_no()

        # this randomly chooses the result whether or not you win the battle!
        result = do_battle()

        sleep(1)
        if result:
            print story.first_scene_win()
        else:
            print story.first_scene_lose()

        sleep(1)
        print story.tbc()

        reset_game = raw_input('Play again? [Y/n]: ')
        play_again = False if no_pattern.match(reset_game.lower()) else True
