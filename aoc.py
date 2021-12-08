import sys
import json
import requests
from pathlib import Path

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def cprint(out, color):
    print(f'{color}{out}{colors.ENDC}')


def determine_date(args):
    if '--today' in args:
        from datetime import date
        today = date.today()
        y, d = today.year, today.day
    elif '--date' in args:
        try:
            y, d = args[args.index('--date') + 1].split('-')
        except:
            cprint('Format the "--date" value as <Year>-<Day>. E.g. 2021-5', colors.FAIL)
    else:
        cprint('HINT: Use the --date flag to specify a date, or use --today to fetch todays challenge.', colors.OKBLUE)
        cprint('Specify the year and day of the challenge you want to fetch:', colors.HEADER)
        y, d = input('Year: '), input('Day: ')
    return str(y), str(d)

        
def main(args):
    year, day = determine_date(args)
    folder = '{}/{}'.format(year, ('0' + str(day))[-2:])
    py_file = f'{folder}/day{day}.py'
    input_file = f'{folder}/input.txt'

    Path(folder).mkdir(parents=True, exist_ok=True) 

    with open('dayX.py') as f:
        template = f.read().replace('<INPUT>', input_file)

    with open(f'{folder}/day{day}.py', 'w+') as f:
        f.write(template)
    
    with open('aoc_cookie.json') as f:
        cookies = json.load(f)
    
    try:
        r = requests.post(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)
        with open(input_file, 'wb+') as f:
            f.write(r.content)
    except Exception as e:
        cprint('Problems fetching challenge for year: {year} with day: {day}.', colors.FAIL)
        raise e


if __name__ == '__main__':
    shorthand_flags = {'-d': '--date', '-t': '--today'}
    main([shorthand_flags[a] if a in shorthand_flags.keys() else a for a in sys.argv])
