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
    g. Column 4: Zip Code. Five-digit format; pad with zeroes if < 5
    h. Column 5: Consumption (numeric value)
"""

import csv
from datetime import datetime


class CustomerData:

    fieldnames = [  'Account Number',
                    'Read Date',
                    'Address',
                    'Zip Code',
                    'Consumption'  ]

    def transform_data(self):
        """ Reads the input file and returns the data in a list of items.
        """

        seen = set() # To check for duplicates

        with open('output.csv', 'w') as output_file:
            writer = csv.writer(output_file)


            writer.writerow(self.fieldnames)

            # Open text file and loop through each row
            for row in open('input_data/example_input.txt'):

                if row not in seen: # Prevent adding duplicate row
                    seen.add(row)
                    new_line = []

                    # Strip each row of trailing whitespace characters
                    row = row.rstrip()

                    acct_num = row[:6]
                    date = row[6:17]
                    address = row[21:44]
                    zip_code = row[44:49]
                    consumption = row[54:]

                    new_line.append(self.pad_zeroes(acct_num, 6))
                    new_line.append(self.convert_date(date))
                    new_line.append(address.rstrip())
                    new_line.append(self.pad_zeroes(zip_code, 5))
                    new_line.append(self.convert_to_int(consumption))

                    writer.writerow(new_line)

        return


    def pad_zeroes(self, string, digits):
        """ Takes string and pads it with leading zeroes.

            Test:

            >>> cust = CustomerData()
            >>> cust.pad_zeroes('45', 6)
            '000045'

            >>> cust.pad_zeroes('1003', 5)
            '01003'
        """

        return str(int(string)).zfill(digits)

    def convert_to_int(self, string):
        """ Takes a string of a positive or negative number and converts it to
            an integer.

            Test:
            >>> cust = CustomerData()
            >>> cust.convert_to_int('1,232')
            1232

            >>> cust.convert_to_int('(121)')
            -121
        """

        return int(string.replace(',', '').replace(')', '').replace('(', '-'))

    def convert_date(self, string):
        """ Takes a string and converts it to a datetime object, then transforms
            the date format to YYYYMMDD.

            Test:

            >>> cust = CustomerData()
            >>> cust.convert_date('Feb 25 2017')
            '20170225'

            >>> cust.convert_date('Sep 2 2016 ')
            '20160902'
        """

        # Strip string of any trailing whitespaces
        string_date = string.rstrip()

        # Convert string to datetime object
        dt = datetime.strptime(string_date, '%b %d %Y')

        # Format datetime object
        return dt.strftime('%Y%m%d')
        


if __name__ == "__main__":
    import doctest
    
    cust = CustomerData()
    cust.transform_data()
    
    result = doctest.testmod()
    if result.failed == 0:
        print("\nALL TESTS PASSED\n")
