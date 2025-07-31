import os
# os.system('clear')
os.system('cls')

# --------------------------------------------
print('')
from datetime import datetime, timedelta
# import locale

# locale.setlocale(locale.LC_TIME, 'es-VE.UTF-8')

now: datetime = datetime.now()
print(f'current date and time: {now}')

specific_datetime: datetime = datetime(2025, 7, 14, 14, 30, 00)
print(f'My birtday is: {specific_datetime}')

# --------------------------------------------
print('')
format_date: str = now.strftime('%d/%m/%Y')
format_date_two:str = now.strftime('%d/%m/%y')
format_date_time: str = now.strftime('%A; %B; %d/%m/%Y %H:%M:%S')

print(f'Format date: {format_date}')
print(f'Format date: {format_date_two}')
print(f'Format date time: {format_date_time}')

# --------------------------------------------
print('')
yesterday: datetime = now - timedelta(days=1)
print(f'Yesterday is:{yesterday}')

# --------------------------------------------
print('')
tomorrow: datetime = now + timedelta(days=1)
print(f'Tomorrow is: {tomorrow}')

# --------------------------------------------
print('')
one_hour_after = now + timedelta(hours=1)
print(f'One hour after is: {one_hour_after}')

# --------------------------------------------
print('')
year: int = now.year
month: int = now.month
day: int = now.day

print(f'year: {year} - month: {month} - day: {day}')

# --------------------------------------------
print('')
date1: datetime = now
date2: datetime = datetime(2025, 7, 14, 14, 00, 00)
difference = date1 - date2

print(f'The difference datetime is: {difference}')
