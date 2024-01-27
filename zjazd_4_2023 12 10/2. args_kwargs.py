import matplotlib.pyplot as plt


def plot_based_on_x_y_arrays():
    points = [(0, 0), (0, 3), (2, 3), (2, 4)]

    print(list(zip(*points)))

    plt.scatter(*zip(*points))
    plt.plot(*zip(*points))
    plt.show()


def basic_args_example():
    def multiply(x, y):
        return x*y


def summarize_person(name:str ="Noname", pesel: str = "00000000000", age: int = 18):
    print(f"{name=}, {pesel=}, {age=}")


def basic_kwargs_example():
    summarize_person(name="Hubert", pesel="9512045694", age=44)

    person = {
        "name": "Halibut",
        "pesel": "547896512",
        "age": 69
    }

    summarize_person(**person)

plot_based_on_x_y_arrays()