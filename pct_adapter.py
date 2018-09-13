import json
import datetime


def get_times(pomodoro):
    dt = datetime.datetime.fromtimestamp(pomodoro['_t'])
    date = str(dt.date())
    duration = int(pomodoro['_d'])

    date_nums = [int(x) for x in date.split('-')]
    midnight = int(datetime.datetime(*date_nums, 0, 0).timestamp())
    ptime = int(pomodoro['_t'])
    start_time = ptime - midnight
    end_time = start_time + duration

    return f'{date} {start_time} {end_time}\n'

def main():
    with open('pct_data/Backup_2018-09-13_15-14-04.json') as pct_backup:
        pomodoros = json.load(pct_backup)['pomodoros']

    with open('periods.txt', 'a') as periods:
        for pomodoro in pomodoros:
            periods.write(get_times(pomodoro))


if __name__ == '__main__':
    main()