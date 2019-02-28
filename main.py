#!/usr/bin/env python3


ENCODING = "ascii"
LIM = 90000


def prepare_slides(ps):
    photos = list(ps)
    used = []
    for i in range(len(photos)):
        min_scores = []
        for j in range(LIM):
            try:
                p = photos[i + 1 + j]
                if p not in used:
                    min_scores.append(min_score(photos[i], p))
                else:
                    min_scores.append(-1)
            except IndexError:
                break

        if i < len(photos) - 1:
            index = min_scores.index(max(min_scores))
            index = i + 1 + index

            # register used photo
            p = photos[index]
            used.append(p)

            before = photos[:i]
            pair = [photos[i], photos[index]]
            middle = photos[i + 1:index]
            after = photos[index + 1:]

            aux = before + pair + middle + after

            # list_a = []
            #
            # for x in aux:
            #     if x not in list_a:
            #         list_a.append(x)
            # TODO: igual hace falta paso por valor list(photos)
            photos = aux

    return photos


def format_result(slides):
    result = ""
    for slide in slides:
        if slide[0] == 'H':
            result += "{}\n".format(slide[1])
        else:
            result += "{} {}\n".format(slide[1][0], slide[1][1])
    return result


def write_result(formatted_result, filename):
    with open(filename, 'wb') as f:
        f.write(formatted_result.encode(ENCODING))


def parse_input(file):
    photos_h = []
    photos_v = []

    with open(file, "r") as f:

        f.readline()

        cont = 0

        for line in f:

            photo = []

            l = line.split()

            photo.append(l[0])
            tags = []

            photo.append(cont)

            for i in range(2, len(l)):
                tags.append(l[i])

            photo.append(tags)

            if photo[0] == "H":
                photos_h.append(photo)
            else:
                photos_v.append(photo)

            cont += 1

    return photos_h, photos_v


def is_vertical(photo):
    return photo[0] == "V"


def tags(photo):
    return photo[2]


def sort_photos(photos):
    return sorted(photos, key=lambda x: len(x[2]))[::-1]


def pair_v(photos_v):
    used = []
    pairs = []

    for i in range(int(len(photos_v) / 2)):
        matches = []

        for j in range(0, LIM):
            try:
                if (j + i + 1) not in used:
                    matches.append(common_tags(photos_v[i], photos_v[j + i + 1]))
                else:
                    matches.append(-1)
            except IndexError:
                break

        m = max(matches) + 1
        for x in range(len(matches)):
            if matches[x] == -1:
                matches[x] = m

        index = matches.index(min(matches))
        index = i + 1 + index

        pair = [photos_v[i], photos_v[index]]

        pairs.append(merge_v(pair))
        used.append(index)

    return pairs


def merge_v(pair):
    tags = pair[0][2] + list(set(pair[1][2]) - set(pair[0][2]))
    return ["V", [pair[0][1], pair[1][1]], tags]


def min_score(photo1, photo2):
    n_common = common_tags(photo1, photo2)
    n_1 = len(tags(photo1)) - n_common
    n_2 = len(tags(photo2)) - n_common

    return min(n_common, n_1, n_2)


def common_tags(photo1, photo2):
    return len(set(tags(photo1)).intersection(tags(photo2)))


def get_score(slides):
    score = 0

    for i in range(0, len(slides)):
        try:
            score += min_score(slides[i], slides[i + 1])

        except IndexError:
            break

    return score


def test(file):
    photos = parse_input(file)

    photos_h = photos[0]
    photos_v = photos[1]

    paired_v = pair_v(photos_v)

    photos = photos_h + paired_v

    photos_s = sort_photos(photos)

    slides = prepare_slides(photos_s)

    score = get_score(slides)
    formatted_result = format_result(slides)
    write_result(formatted_result, file.replace("data/", "results/1"))

    # for photo in photos_s:
    #     print(photo)
    #
    # print()

    print("Score of %s: %i" % (file, score))

    return score


def main():
    score = 0
    score += test("data/a_example.txt")
    score += test("data/b_lovely_landscapes.txt")
    score += test("data/c_memorable_moments.txt")
    score += test("data/d_pet_pictures.txt")
    score += test("data/e_shiny_selfies.txt")

    print("\nTotal Score: %i" % score)


if __name__ == '__main__':
    main()
