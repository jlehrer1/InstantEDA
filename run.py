import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Data file in .csv form") #add other file types later
parser.add_argument("-w", "--write", help="Write pdf to specified directory if it exists, else writes to current")

if __name__ == "__main__":
    args = vars(parser.parse_args())
    if args["write"] is not None and not os.path.isdir(args["write"]):
        raise NotADirectoryError("Directory does not exist or not a valid file path")
    if not args["input"].endswith('.csv'):
        raise TypeError("Error: input is not a .csv file")

    