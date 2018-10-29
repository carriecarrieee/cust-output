""" Customer Output

    Customer provides a fixed-width input file that needs to be transformed to 
    meet data specifications.  This function takes an input file and writes an 
    output file matching the following specifications:

    a. File must be in valid CSV format
    b. File must not contain duplicate rows
    c. File must contain a header row with column names
    d. Column 1: Account Number. If less than six digits, padded with leading
        zeroes 
    e. Column 2: Read Date. Format: YYYYMMDD
    f. Column 3: Address (free text)
    g. Column 4: Zip Code. Five-digit format
    h. Column 5: Consumption (numeric value)
"""

from pprint import pprint


def parse_data():
    """ Reads the input file and returns the data in a list of items.
    """

    seen = set() # To check for duplicates

    d = {}
    acct_num = []
    date = []
    address = []
    zip_code = []
    consumption = []

    # Open file and loop through each row
    for row in open("input_data/example_input.txt"):

        if row in seen:
            continue # Skip duplicate
        else:
            seen.add(row)

            # Strip each row of trailing whitespace characters
            row = row.rstrip()

            acct_num.append(row[:6])
            date.append(row[6:17])
            address.append(row[21:44])
            zip_code.append(row[44:49])
            consumption.append(row[54:])

            d.update({
                'acct_num': acct_num,
                'date': date,
                'address': address,
                'zip_code': zip_code,
                'consumption': consumption
                })

    return d

        


pprint(parse_data())