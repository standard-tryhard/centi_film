# ==== OPERATORS ==== #
import sys

from hundMov_bb_operators_input import intro_question_confirm
from hundMov_cc_animations import animate_type


def populate_dict_with_default_values(a_dict_, placeholder_='...'):
    for idx_ in range(1, 101):

        try:
            has_an_actual_movie_ = (a_dict_[idx_] != placeholder_)
            continue
        except:
            a_dict_.update({idx_: placeholder_})

    return sorted(a_dict_.items())


