#!/usr/bin/env python3


def parse_input(file):
    photos = []

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

            photos.append(photo)

            cont += 1

    return photos


def is_vertical(photo):
    return photo[0] == "V"


def tags(photo):
    return photo[2]


def main():
    photos = parse_input("data/a_example.txt")

    for photo in photos:
        print(photo)

    print()

    print(get_points(photos[2], photos[3]))


def get_points(photo1, photo2):
    n_common = common_tags(photo1, photo2)
    n_1 = len(tags(photo1)) - n_common
    n_2 = len(tags(photo2)) - n_common

    return min(n_common, n_1, n_2)


def common_tags(photo1, photo2):
    return len(set(tags(photo1)).intersection(tags(photo2)))


if __name__ == '__main__':
    main()
