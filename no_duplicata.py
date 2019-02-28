import collections
import os


def test(file):
    with open(file, "r") as f:

        l = ""

        for line in f.readlines():
            for word in line.split():
                l += word + ","

    y = collections.Counter(l.split(","))

    print("Duplicates for file %s:\n\t %s\n" % (file, y))


if __name__ == '__main__':
    for file in os.listdir("results/"):
        test("results/" + file)
