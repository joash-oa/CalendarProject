import sys


def get_year():
    y = int(input('Enter the year: '))
    if y < 1:
        print('Year must be positive.')
        sys.exit()
    else:
        return y


def get_starting_day():
    d = int(input('Enter the day of the week for January 1st (0 for Sunday, 1 for Monday, ...): '))
    if not 0 <= d <= 6:
        print('Day must be 0-6.')
        sys.exit()
    else:
        return d


def is_leap_year(yr):
    if yr % 4 != 0:
        return False
    elif yr % 100 != 0:
        return True
    elif yr % 400 != 0:
        return False
    else:
        return True


def print_month(month, num_days, day_one):
    print(month)
    print('   ' * day_one, end='')
    for num in range(1, num_days + 1):
        print(f'{num}'.rjust(3), end='')
        day_one += 1
        if day_one == 7:
            print()
            day_one = 0
    print('\n')
    return day_one


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


year = get_year()
start_day = get_starting_day()

if is_leap_year(year):
    days[1] = 29

for index, m in enumerate(months):
    c = print_month(m, days[index], start_day)
    start_day = c
 
