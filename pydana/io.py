import matplotlib.pyplot as plt
import pandas as pd


def read_data(path):
    pd.read_csv(path, delimiter="\\s+")
    return


def plot_data(table):
    plt.plot(table)


def save_data(opath):
    plt.savefig(opath)
