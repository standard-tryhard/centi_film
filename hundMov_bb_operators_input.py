# ==== OPERATORS, USERINPUT ==== #


import sys

import hundMov_cc_animations
import hundMov_bb_validators
import hundMov_cc_animations



def intro_answer_responder():
    is_valid_ = False

    while not is_valid_:
        is_valid_, rsp_ = intro_question_confirm()
        if is_valid_ and rsp_ == '1':
            break
        elif is_valid_ and rsp_ == '2':
            print("Ok, bdyeeee!")
            sys.exit(0)

        hundMov_cc_animations.animate_type(f"You entered: '{rsp_}' :(, try pressing [1] or [2]")


def intro_question_confirm():
    hundMov_cc_animations.display_choices([
         "[y]......yes"
        ,"[n]......no"
    ])

    tuple_rsp_ = input("... ")
    valid_rsp_ = hundMov_bb_validators.make_sure_its_integer(tuple_rsp_)

    if valid_rsp_:
        return True, tuple_rsp_
    else:
        return False, tuple_rsp_

def gimme_a_movie_name() -> str:
    rsp_ = input("K, name a movie then...\n")
    return rsp_



def gimme_a_integer(movie_):
    len_movie_list = "\'x\'"
    rsp_ = input(f"What rank then for ['{movie_}']?: ")

    if str.isnumeric(rsp_):
        print()
        print(f"{movie_.title()}, ranked {rsp_}/100; You now have {len_movie_list} ranked movies")
        return int(rsp_)
    else:
        print('the algorithm says would you put in a number?')
        return False



if __name__ == "__main__":
    print("from localfile run directly")

    print(hundMov_bb_validators.stndrd_validator(['s','l','r']))