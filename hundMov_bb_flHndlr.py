# ==== FILEHANDLER ==== #

import csv


fieldnames = ["RankNo.","MovieTitle"]

def unpack_a_csv(a_file_):
    centi_film_dict: dict[int, str] = {}
    with open(a_file_, 'r') as f:
        fluff_bunny_reader = csv.reader(f)

        for l in fluff_bunny_reader:
            movie_rank = l[0]
            movie_title = l[1]
            centi_film_dict[int(movie_rank)] = movie_title

    return centi_film_dict

def unpack_a_csv_2(a_file_):
    centi_film_asList: list = []
    with open(a_file_, 'r') as f:
        fluff_bunny_reader = csv.reader(f)

        next(fluff_bunny_reader)

        for l in fluff_bunny_reader:
            movie_rank_ = l[0]
            movie_title_ = l[1]
            centi_film_asList.append({fieldnames[0]: movie_rank_, fieldnames[1]: movie_title_})

    return sorted(centi_film_asList, key = lambda dict_ : int(dict_['RankNo.']) )


def write_a_csv(stuff_toAdd_, a_file_):
    with open(a_file_, 'r+', newline='') as f_:
        rank_no_ = "RankNo."
        movie_title_ = "MovieTitle"

        fieldnames_ = [rank_no_, movie_title_]
        wrtr = csv.DictWriter(f_, fieldnames=fieldnames_)

        first_line = f_.readlines(1)

        if not first_line:
            wrtr.writeheader()

        for k,v in stuff_toAdd_.items():
           wrtr.writerow(dict([(rank_no_, k), (movie_title_, v)]))

def write_a_csv_2(stuff_toAdd_, a_file_):
    with open(a_file_, 'r+', newline='') as f_:
        rank_no_ = fieldnames[0]
        movie_title_ = fieldnames[1]

        wrtr = csv.DictWriter(f_, fieldnames=fieldnames)

        first_line = f_.readlines(1)

        if not first_line:
            wrtr.writeheader()

        for dict_ in stuff_toAdd_:
           wrtr.writerow(dict_)


if __name__ == "__main__":
    print('printed from \'__main__\'')
    unpacked = unpack_a_csv_2('hundMov_csv_usrTopHund_DBrdr.csv')
    print(unpacked)
    write_a_csv_2(unpacked, 'hundMov_csv_usrTopHund_DBwrtr.csv')