# ==== NARRATIVES, INTROS ==== #

import hundMov_bb_validators
import hundMov_cc_animations
from hundMov_cc_animations import animate_type


def intro_a():
    animate_type('\n\n', speed=.8)
    animate_type("CENTI FILM")
    animate_type('\n\n', speed=.8)


def intro_b():
    animate_type(
        "\nCenti Film is a Personal Film Database Program"
        "\nIt is designed to enhance film appreciation"
        "\nand celebrate the many kinds of creativity required"
        "\nfor any production."
    )



def intro_c():
    animate_type(
    "\nAnytime that you need to make a choice in this program,"
    "\nyou will be presented with a menu like this"
    )

    hundMov_cc_animations.ellipsis_animation()


def intro_d():
    hundMov_cc_animations.display_choices([
         "    [S]   ...   press 'S' (or 1)    S--START!"
        ,"    [L]   ...   press 'L' (or 2)    L--LEARN MORE"
        ,"    [R]   ...   press 'C' (or 3)    C--CONTEXT"
        ,"    [X]   ...   press 'X' (or 4)    X--SIMPLE MENUS"
        ,"    [Y]   ...   press 'Y' (or 5)    Y--HELP"
        ,"    [Z]   ...   press 'Z' (or 6)    Z--CREDITS"
    ], add_whitespace_=2)


def intro_e():
    animate_type(
        "\nPlease type a letter that corresponds to your choice"
        "\nfrom the options listed. (It is not case-sensitive.)"
    )
    hundMov_cc_animations.ellipsis_animation(True)
    h = (word[0] for word in ['start'])
    print(hundMov_bb_validators.stndrd_validator([ word[0] for word in ['start', 'learn', 'help']]))




