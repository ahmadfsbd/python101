#!/usr/bin/python3

# Script should be run from within the directory of script"""

import argparse


def parse_arguments():
    # Create a new parser
    parser = argparse.ArgumentParser(
        description="Parse the arguments to obtain the name",)
    # Store a value by providing a shot-flag/full-name
    # required=True means user must enter this value else exception will be given
    parser.add_argument('-n', '--name',
                    help='Name, e.g Bob, Martin, Jack etc.',
                    required=True)
    # Store a value if a flag is given by using action
    # required=False means the code does not force user for value
    # If this flag is not provided, default value will be set to False
    parser.add_argument('-is_human', '--is_human',
                        help='The entry is a human !',
                        action='store_true', required=False)

    # Add another parsing group to store some variables that fall in different catagory than original
    education = parser.add_mutually_exclusive_group()
    # Store Multiple arguments as a list using 'nargs'
    education.add_argument('-d', '--degrees', nargs="+",
                                help='Enter bs, ms',
                                required=False)

    """ :::::::::: nargs explained :::::::::::
    3: 3 values, can be any number you want
    ?: a single value, which can be optional
    *: a flexible number of values, which will be gathered into a list
    +: like *, but requiring at least one value
    argparse.REMAINDER: all the values that are remaining in the command line
    """

    # Execute the parse_args() method
    args, unknown = parser.parse_known_args()
    if len(unknown) > 0:
        parser.print_help()
        msg = "Invalid argument(s) :"
        for each in unknown:
            msg += " " + each + ";"
        raise AssertionError(msg)

    return args


# Main function
def main():
    args = parse_arguments()
    print(args)


if __name__ == "__main__":
    main()
