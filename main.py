#!/usr/bin/env python3


LIM = 50


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

        print(min_scores)

        if i < len(photos) - 1:
            index = min_scores.index(max(min_scores))
            index = i + 1 + index

            before = photos[:i]
            pair = [photos[i], photos[index]]
            middle = photos[i + 1:index]
            after = photos[index + 1:]

            aux = before + pair + middle + after
            # TODO: igual hace falta paso por valor list(photos)
            photos = aux

            # register used photo
            p = photos[index]
            used.append(p)

    return photos


def write_result(slides):
    with open('result.out', 'w') as w:
        w.write(str(len(slides)) + '\n')
        for slide in slides:
            if slide[0] == 'V':
                w.write(str(slide[1][0]) + ' ' + str(slide[1][1]) + '\n')
            else:
                w.write(str(slide[1]) + '\n')


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


def main():
    # photos = parse_input("data/a_example.txt")
    # photos = parse_input("data/c_memorable_moments.txt")
    # photos = parse_input("data/d_pet_pictures.txt")
    photos = parse_input("data/test")

    photos_h = photos[0]
    photos_v = photos[1]

    # for photo in photos_h:
    #     print(photo)
    #
    # print()
    #

    paired_v = pair_v(photos_v)

    photos = photos_h + paired_v

    photos_s = sort_photos(photos)

    for photo in photos_s:
        print(photo)

    print()

    print(get_score(prepare_slides(photos_s)))


if __name__ == '__main__':
    main()
