# WhatsApp Auto Sender

Automate sending scheduled WhatsApp messages using either the **WhatsApp Desktop App** or **WhatsApp Web**.

## Features

- **Desktop App Automation (`whatsapp_sender.py`)**: 
  - Opens the installed WhatsApp Desktop application.
  - Schedules messages for a specific time.
  - Prevents computer sleep during the countdown.
  - Wakes the screen before sending.
  - *Note: Requires WhatsApp Desktop to be installed.*

- **Web Automation (`whatsapp_web_sender.py`)**:
  - Uses `pywhatkit` to send messages via WhatsApp Web in your browser.
  - Simpler setup if you don't use the Desktop app.

## Installation

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Method 1: Desktop App (Recommended)
1. Ensure WhatsApp Desktop is installed and you are logged in.
2. Run the script:
   ```bash
   python whatsapp_sender.py
   ```
3. Enter the phone number (with country code), message, number of repeats, and scheduled time.
4. **Keep the script running.** Do not close the terminal.
5. **Do not lock your computer (Win+L).** The monitor can turn off, but the PC must not be locked.

### Method 2: WhatsApp Web
1. Ensure you are logged into WhatsApp Web in your default browser.
2. Run the script:
   ```bash
   python whatsapp_web_sender.py
   ```

## Troubleshooting
- If `whatsapp_sender.py` opens a browser instead of the App, run `python test_config.py`. If that also opens a browser, change your Windows "Default Apps" settings for the `WHATSAPP` protocol.
