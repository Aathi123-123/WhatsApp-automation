import pywhatkit
import datetime

phone_number = input("Enter the phone number (with country code, e.g., +1234567890): ")
message = input("Enter the message to send: ")

print("Enter the time to send the message (24-hour format):")
scheduled_hour = int(input("Hour (0-23): "))
scheduled_minute = int(input("Minute (0-59): "))

# PyWhatKit takes care of opening WhatsApp Web and sending the message.
# It requires you to be logged into WhatsApp Web in your default browser.
print(f"Scheduling message to {phone_number} at {scheduled_hour}:{scheduled_minute}")

try:
    # sendwhatmsg schedules the message.
    # buffer_time is the time in seconds to wait before sending (default is usually fine)
    # The function automatically opens the browser and sends the message.
    pywhatkit.sendwhatmsg(phone_number, message, scheduled_hour, scheduled_minute)
    print("Message scheduled successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
