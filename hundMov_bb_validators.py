# ==== VALIDATORS ==== #


import hundMov_bb_errHndlr
import hundMov_cc_animations


all_letters = list('abcdefghijklmnopqrstuvxyz')


def make_sure_its_integer(rsp_) -> bool:
    valid_integer_responses_ = ['1', '2']
    res_: bool = (rsp_ in valid_integer_responses_)
    return res_


def is_one_number_only(rsp_) -> int:
    res_ = rsp_.isnumeric() and (len(rsp_) == 1)
    if res_:
        return int(rsp_)

    else:
        -1



def stndrd_validator(list_of_choices_):
    rsp_ = input("")

    rsp_ = rsp_.lower()
    test_single = hundMov_bb_errHndlr.strlength_error(rsp_)
    test_alphanum = hundMov_bb_errHndlr.digit_or_letter_error(rsp_)

    if test_single and test_alphanum:
        return rsp_ in list_of_choices_

    else:
        hundMov_cc_animations.ellipsis_animation()
        hundMov_cc_animations.animate_type("Is it possible you put something other than?"
                                           "\none letter or one digit?")


if __name__ == "__main__":
    print(all_letters)