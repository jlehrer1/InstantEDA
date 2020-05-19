import os
import argparse
import pandas as pd

from cleaning import clean
from visualization import visualization

parser = argparse.ArgumentParser()
# add other file types later
parser.add_argument("input", help="Path to .csv or .xlsx data file")
parser.add_argument(
    "-w", "--write", help="Write images to specified directory if it exists, else writes to current")

if __name__ == "__main__":
    args = vars(parser.parse_args())

    dir_w = args["write"]
    if not args["input"].endswith('.csv') or not args["input"].endswith('.xlsx'):
        raise TypeError("Error: input is not a .csv or .xlsx file")
    if dir_w is not None and not os.path.isdir(dir_w):
        raise NotADirectoryError(
            "Directory does not exist or not a valid file path")
    else:
        try:
            os.makedirs(dir_w)
        except FileExistsError:
            print("Write location exists, continuing...")

    df = pd.read_csv(args["input"])
    num_nan_plot = visualization.num_nan_plot(df)
    percent_nan_plot = visualization.percent_nan_plot(df)

    df_clean = clean.impute_data(df)
    corr_plot = visualization.corr_plot(df)

    num_nan_plot.write_image(os.path.join(dir_w, 'num_nan.png'))
    percent_nan_plot.write_image(os.path.join(dir_w, 'percent_nan.png'))
    corr_plot.write_image(os.path.join(dir_w, 'correlations.png'))