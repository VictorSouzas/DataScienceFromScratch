# -*- coding: utf-8 -*-

from matplotlib import pyplot


def chap_3_1():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gpd = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    # create a line chart, years on x-axis, gpd on y-axis
    pyplot.plot(years, gpd, color='green', marker='o', linestyle='solid')

    # add a title
    pyplot.title("Nominal GPD")

    # add a label
    pyplot.ylabel("Bilions of $")
    pyplot.xlabel("years")
    pyplot.show()


def chap_3_2():
    movies = ["Annie Hall", "Ben-Hur", "CasaBlanca", "Gandhi",
              "West Side Story"]
    num_of_oscars = [5, 11, 3, 8, 10]

    # bars are by default width 0.8, so well add 0.1 to the left
    # coordinates so that each bar is centered
    xs = [i + 0.1 for i, _ in enumerate(movies)]

    # plot bars with left x-coordinates [xs], heights [num_of_oscars]
    pyplot.bar(xs, num_of_oscars)

    pyplot.ylabel("# of Academy Awards")
    pyplot.title("Movies")

    # label x-axis with movie at bar centers
    pyplot.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
    pyplot.show()


# chap_3_1()
chap_3_2()
