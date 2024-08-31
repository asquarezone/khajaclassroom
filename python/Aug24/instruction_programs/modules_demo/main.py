"""This module will act as executable
"""
import utils


def main():
    """Main function
    """
    choice = 'y'
    while choice == 'y':
        principle = float(input('Enter principle amount: '))
        rate = float(input('Enter rate of intrest: '))
        time = float(input('Enter time period in years: '))
        print(f'Compound Intrest: {utils.compound_intrest(principle, rate, time)}')
        print(f'Simple Intrest: {utils.simple_intrest(principle, rate, time)}')
        choice = input('Do you want to continue? (y/n): ').lower()



if __name__ == '__main__':
    main()
