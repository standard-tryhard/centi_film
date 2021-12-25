# ==== ERRORS ==== #


import hundMov_cc_animations

def strlength_error(rsp_):

    return len(rsp_) == 1


def digit_or_letter_error(rsp_):

    return str.isnumeric(rsp_) or str.isalpha(rsp_)





def integer_error(movie_name_):
    hundMov_cc_animations.animate_type(f"Would you try putting in an integer like:"
                                       f" 3, 17, -144 for this movie: ['{movie_name_}']?: ")