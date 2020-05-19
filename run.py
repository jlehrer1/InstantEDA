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

    if not args["input"].endswith('.csv') or not args["input"].endswith('.xlsx'):
        raise TypeError("Error: input is not a .csv or .xlsx file")
    if args["write"] is not None and not os.path.isdir(args["write"]):
        raise NotADirectoryError(
            "Directory does not exist or not a valid file path")

    df = pd.read_csv(args["input"])

    num_nan_plot = visualization.num_nan_plot(df)
    percent_nan_plot = visualization.percent_nan_plot(df)

    df_clean = clean.impute_data(df) if key.lower() == 'y' else quit()

    corr_plot = visualization.corr_plot(df)

    if args["write"] is not None:
        try:
            os.makedirs(args["write"])
        except FileExistsError:
            pass