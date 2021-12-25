# ==== ROOTLOOP ==== #

import sys

import hundMov_bb_errHndlr
import hundMov_bb_flHndlr
import hundMov_bb_narratives_main
import hundMov_bb_operators_input
import hundMov_bb_narratives_intros
import hundMov_bb_operators_data

# ---A--- #

break_point: object
break_point = sys.exit

# ---B--- #

bunnies_csv = 'hundMov_csv_usrTopHund_DBrdr.csv'
bunny_house_extraction = hundMov_bb_flHndlr.unpack_a_csv(bunnies_csv)
bunnies_unsorted_items = bunny_house_extraction.items()
bunnies_sorted_items = hundMov_bb_operators_data.populate_dict_with_default_values(bunny_house_extraction)
bunnies_dict = dict(bunnies_sorted_items)

# ---C--- #

hundMov_bb_narratives_intros.intro_a() #'''
hundMov_bb_narratives_intros.intro_b() #'''
hundMov_bb_narratives_intros.intro_c() #'''
hundMov_bb_narratives_intros.intro_d()  # '''
hundMov_bb_narratives_intros.intro_e()  # '''


movie_name = hundMov_bb_operators_input.gimme_a_movie_name()
rank_no = hundMov_bb_operators_input.gimme_a_integer(movie_name)

# movie_name = "Licorice Pizza"
# rank_no = 25


# ---BREAKPOINT - BREAKPOINT - BREAKPOINT ---#
break_point(0)


# ---D--- #

while True:
    if rank_no:
        break
    else:
        hundMov_bb_errHndlr.integer_error(movie_name)
        rank_no = hundMov_bb_operators_input.gimme_a_integer(movie_name)

bunnies_dict[rank_no] = movie_name
hundMov_bb_narratives_main.save_progress("card")
hundMov_bb_flHndlr.write_a_csv(bunnies_dict, 'hundMov_csv_usrTopHund_DBwrtr.csv')

