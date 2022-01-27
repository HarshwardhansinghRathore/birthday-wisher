import random
import datetime as dt
import smtplib
import pandas

today = dt.datetime.now()
data = pandas.read_csv('birthdays.csv')

for index, value in data.iterrows():
    if value.month == today.month and value.day == today.day:
        letter = open(f'letter_templates\\letter_{random.randint(1,3)}.txt', mode='r')
        raw_letter = letter.read()
        final_letter = raw_letter.replace("[NAME]", value["name"])
        connection = smtplib.SMTP('smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(user='hr1566027@gmail.com', password='brodlyeytybyjwdx')
        connection.sendmail(from_addr='hr1566027@gmail.com', to_addrs=f'{value.email}',
                            msg=f"Subject:happy birthday {value['name']}\n\n{final_letter}")
        connection.close()
