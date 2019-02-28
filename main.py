#!/usr/bin/env python3


LIM = 10


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


def main():
    photos = parse_input("data/a_example.txt")

    photos_h = photos[0]
    photos_v = photos[1]

    for photo in photos_h:
        print(photo)

    print()

    for photo in photos_v:
        print(photo)

    print()

    print(sort_photos(photos_h))


def group_v(photos_v):
    pairs = []
    for i in range(len(photos_v)/2):
        matches = [0] * LIM
        for j in range(i+1, i+1+LIM):
            matches[j] = common_tags(photos_v[i], photos_v[j])



def get_points(photo1, photo2):
    n_common = common_tags(photo1, photo2)
    n_1 = len(tags(photo1)) - n_common
    n_2 = len(tags(photo2)) - n_common

    return min(n_common, n_1, n_2)


def common_tags(photo1, photo2):
    return len(set(tags(photo1)).intersection(tags(photo2)))


if __name__ == '__main__':
    main()
