# ==== NARRATIVES, MAIN ==== #

import sys
import time

import hundMov_bb_validators


def save_progress():
    print("Would you like to save?")


def standard_question(list_):
    get_first_letter = lambda w: w[0]
    get_idx = lambda l, s: l.index(s) + 1

    letters = [get_first_letter(l) for l in list_]
    indexes = [get_idx(list_, elem) for elem in list_]


    rsp = input("which letter you like? ")


    try:
        idx = hundMov_bb_validators.is_one_number_only(rsp)
        valid_idx = idx if idx in indexes else None
        choice = list_[valid_idx - 1]

    except:
        if rsp.isalpha() and rsp in letters:
            letter_idx = letters.index(rsp)
            choice = list_[letter_idx]

        else:
            choice = None


    return choice

#
# def complex_letters(list_):
#     complex_letters = []
#
#
#     get_first_letter = lambda w: w[0]
#     letters = [get_first_letter(l) for l in list_]
#
#
#     leftover_letters = hundMov_bb_validators.all_letters
#
#     for idx, word in enumerate(list_):
#         word_idx = 0
#         time.sleep(.5)
#
#         letter = word[word_idx]
#         if letter in leftover_letters:
#             complex_letters.append(letter)
#             leftover_letters = list(filter(lambda x: x not in complex_letters, leftover_letters))
#             print(len(leftover_letters))
#
#         else:
#             word_idx += 1
#             letter = word[word_idx]
#             if letter in leftover_letters:
#                 complex_letters.append(letter)
#             leftover_letters = list(filter(lambda x: x not in complex_letters, leftover_letters))
#             print(len(leftover_letters))
#
#
#     leftover_letters = list(filter(lambda x: x not in letters, hundMov_bb_validators.all_letters ))
#     for l in complex_letters:
#         print(l)




def question_formatter(list_):
    get_first_letter = lambda w: w[0]
    get_idx = lambda l, s: l.index(s) + 1

    letters = [get_first_letter(l) for l in list_]
    indexes = [get_idx(list_, elem) for elem in list_]

    for idx, item in enumerate(list_):
        print(f"    [{item[0].upper()}] or [{idx+1}]   ->   {item.title()}")



if __name__ == "__main__":
    print(standard_question(["arie", "marie", "curie"]))
    # complex_letters(['abie', 'rie', 'carrie'])
