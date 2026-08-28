##################### Extra Hard Starting Project ######################


# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import smtplib
import random
import os
now=dt.datetime.now()
print(now)
day=now.day
month=now.month
with open("birthdays.csv","r") as file:
    row=file.readlines()
    print(row)
for i in range(len(row)):
    day_of_birthday =row[i].split(",")[4].replace("\n","")
    print(day_of_birthday)
    if day_of_birthday=="day":
        continue


    if int(day_of_birthday) == day:
        name_of_birthday=row[i].split(",")[0]
        rand=random.randint(1,3)

        with open(f"./letter_templates/letter_{rand}.txt", "r") as file1:
            read = file1.read()
            first_line = read.replace("[NAME]", name_of_birthday)
            print(first_line)
        my_email=os.environ.get("MY_EMAIL")
        password=os.environ.get("MY_PASSWORD")

        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="smariy98@yahoo.com",
                            msg=f"subject:Happy Birthday!\n\n{first_line} ")
        connection.close()
print("EMAIL:", EMAIL)
print("PASSWORD:", PASSWORD)
        









# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.







