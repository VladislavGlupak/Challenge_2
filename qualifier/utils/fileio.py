# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(output_path, header, qualifying_loans):

    """Saves qualifying loans into CSV file.

    Args:
        output_path: the csv file path.
        header: list of columns names
        qualifying_loans: list of qualifying loans

    Result:
        Qualifing loans saved into new file. Abslute path is provided in the terminal output.
    """

    with open(output_path, "w") as output_file:
        csvwriter = csv.writer(output_file) # create writer instance

        csvwriter.writerow(header) # save header first
    
        for loan in qualifying_loans:
            csvwriter.writerow(loan) # save qualifying loans values
    
    print(f"Qualifying loans were saved to {output_path.absolute()}")