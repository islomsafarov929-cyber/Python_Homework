# Task 1.Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import datetime
from dateutil.relativedelta import relativedelta

try:
    birthdate_str = input("Enter your birth date (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()

    age = relativedelta(today, birthdate)
    print(f"Your age: {age.years} years, {age.months} months, {age.days} days")

except ValueError:
    print("Invalid date format! Use YYYY-MM-DD.")
except Exception as e:
    print("An unexpected error occurred:", e)


# Task 2.Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import datetime

try:
    birthdate_str = input("Enter your birth date (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()

    next_birthday = datetime(today.year, birthdate.month, birthdate.day)

    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)

    days_left = (next_birthday - today).days
    print("Days Until Next Birthday:", days_left)

except ValueError:
    print("Invalid date format! Use YYYY-MM-DD.")
except Exception as e:
    print("An unexpected error occurred:", e)



# Task 3.Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

try:
    current_datetime_str = input("Enter current date and time (YYYY-MM-DD, H(24):M): ").strip()
    dur_meeting_str = input("Enter meeting duration (H:M): ").strip()

    current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d, %H:%M")

    hours, minutes = map(int, dur_meeting_str.split(":"))
    meeting_duration = timedelta(hours=hours, minutes=minutes)

    end_datetime = current_datetime + meeting_duration

    print(f"The meeting will end at: {end_datetime.strftime('%Y-%m-%d %H:%M')}")

except ValueError:
    print("Invalid input! Check your date/time format.")
except Exception as e:
    print("An unexpected error occurred:", e)



# Task 4.Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

from datetime import datetime
from zoneinfo import ZoneInfo

try:
    current_datetime_str = input("Enter date and time (YYYY-MM-DD HH:MM): ").strip()
    current_timezone_str = input("Enter your current timezone (e.g., Asia/Tashkent): ").strip()
    target_timezone_str = input("Enter target timezone (e.g., Europe/London): ").strip()

    current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M")
    current_datetime = current_datetime.replace(tzinfo=ZoneInfo(current_timezone_str))

    converted_datetime = current_datetime.astimezone(ZoneInfo(target_timezone_str))

    print(f"Original datetime ({current_timezone_str}): {current_datetime.strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"Converted datetime ({target_timezone_str}): {converted_datetime.strftime('%Y-%m-%d %H:%M %Z')}")

except ValueError:
    print("Invalid date/time format! Use YYYY-MM-DD HH:MM.")
except Exception as e:
    print("Error:", e)



# Task 5.Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime
import time

try:
    future_str = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ").strip()
    future_datetime = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

    print("Countdown started...")

    while True:
        now = datetime.now()
        remaining = future_datetime - now

        if remaining.total_seconds() <= 0:
            print("Time's up!")
            break

        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Time remaining: {days} days {hours:02}:{minutes:02}:{seconds:02}", end="\r")
        time.sleep(1)

except ValueError:
    print("Invalid date/time format! Use YYYY-MM-DD HH:MM:SS.")
except KeyboardInterrupt:
    print("\nCountdown stopped manually.")
except Exception as e:
    print("Error:", e)


# Task 6.Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re

try:
    email = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        print("Valid email address")
    else:
        print("Invalid email address")

except Exception as e:
    print("Error:", e)


# Task 7.Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

def format_phone_number(phone):
    try:
        digits = ''.join(filter(str.isdigit, phone))
        if len(digits) == 9:
            return f"({digits[0:2]}) {digits[2:5]}-{digits[5:7]}-{digits[7:9]}"
        else:
            return "Invalid phone number length"
    except Exception:
        return "Error processing phone number"

try:
    phone_input = input("Enter a 9-digit phone number: ")
    print("Formatted phone number:", format_phone_number(phone_input))

except Exception as e:
    print("Error:", e)



# Task 8.Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

def check_password_strength(password):
    try:
        if len(password) < 8:
            return "Weak: Password must be at least 8 characters long."
        if not any(ch.isupper() for ch in password):
            return "Weak: Password must contain at least one uppercase letter."
        if not any(ch.islower() for ch in password):
            return "Weak: Password must contain at least one lowercase letter."
        if not any(ch.isdigit() for ch in password):
            return "Weak: Password must contain at least one digit."
        return "Strong password!"

    except Exception:
        return "Error checking password."

try:
    user_password = input("Enter your password: ")
    print(check_password_strength(user_password))

except Exception as e:
    print("Error:", e)



# Task 9.Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

import re

sample_text = """Python is powerful. Python is easy to learn.
Many developers love Python because it is versatile."""

try:
    word = input("Enter a word to search: ").strip()
    matches = [m.start() for m in re.finditer(rf"\b{word}\b", sample_text)]

    if matches:
        print(f"Occurrences of '{word}' found at positions: {matches}")
        print(f"Total occurrences: {len(matches)}")
    else:
        print(f"No occurrences of '{word}' found in the text.")

except Exception as e:
    print("Error:", e)



# Task 10.Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

import re

try:
    text = input("Enter a text: ")

    date_pattern = r'\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4})\b'
    dates = re.findall(date_pattern, text)

    if dates:
        print("Dates found:")
        for d in dates:
            print("-", d)
    else:
        print("No dates found.")

except Exception as e:
    print("Error:", e)
