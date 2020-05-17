import os
import argparse
import pandas pd

from cleaning import clean

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Path to .csv or .xlsx data file") #add other file types later
parser.add_argument("-w", "--write", help="Write pdf to specified directory if it exists, else writes to current")

if __name__ == "__main__":
    args = vars(parser.parse_args())

    if not args["input"].endswith('.csv') or not args["input"].endswith('.xlsx'):
        raise TypeError("Error: input is not a .csv file")
    if args["write"] is not None and not os.path.isdir(args["write"]):
        raise NotADirectoryError("Directory does not exist or not a valid file path")
    
    df = pd.read_csv(args["input"])

    # impute the data
    df = clean.impute_data(df)

