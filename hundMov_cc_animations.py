# ==== ANIMATIONS ==== #

import time
import sys


def animate_type(text, speed=.04) -> object:
  for char in str(text):
    sys.stdout.write(char)
    time.sleep(speed)
    sys.stdout.flush()


def timed_whitespace(amount_of_space_=2):
  for x in range(amount_of_space_):
    time.sleep(.2)
    print()


def ellipsis_animation(add_whitespace_=0):


    timed_whitespace(add_whitespace_)

    animate_type('... ', .2)

    time.sleep(.2)



def display_choices(choices_as_list_, speed=.1, add_whitespace_=0):

  timed_whitespace(add_whitespace_)

  animate_type("      CHOICES:\n")
  for choice in choices_as_list_:
    time.sleep(speed)
    print(f'    {choice}')

  timed_whitespace(0)

