import webbrowser
import time
import datetime
import pyautogui
import os
import ctypes
from urllib.parse import quote
import pygetwindow as gw

# Constants for preventing sleep
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def prevent_sleep():
    """Prevent the computer from going to sleep while the script waits."""
    print("Preventing system sleep...")
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )

def allow_sleep():
    """Allow the computer to sleep again."""
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

def wake_screen():
    """Simulate activity to wake the screen."""
    print("Waking screen...")
    pyautogui.press('shift')
    pyautogui.moveRel(1, 0)
    pyautogui.moveRel(-1, 0)

def send_whatsapp_desktop(phone_number, message, count=1):
    # Quote the message for URL
    encoded_message = quote(message)
    
    # WhatsApp Desktop URL scheme
    url = f"whatsapp://send?phone={phone_number}&text={encoded_message}"
    
    print("Opening WhatsApp Desktop...")
    # Use os.startfile on Windows to force protocol handler instead of browser
    try:
        os.startfile(url)
    except AttributeError:
        # Fallback for non-Windows assuming webbrowser might work
        webbrowser.open(url)
    except Exception as e:
        print(f"Error opening URL with os.startfile: {e}")
        webbrowser.open(url)
    
    # Wait for the app to open and load the chat
    print("Waiting 20 seconds for WhatsApp to load...")
    time.sleep(20)
    
    # Attempt to focus the window
    try:
        # Get all windows with 'WhatsApp' in the title
        windows = gw.getWindowsWithTitle('WhatsApp')
        # Filter out browser windows if possible (heuristic)
        app_window = None
        for w in windows:
            # WhatsApp Desktop usually just says "WhatsApp" or "WhatsApp - Name"
            # Browser tabs usually have "WhatsApp - Google Chrome" etc.
            if "Chrome" not in w.title and "Edge" not in w.title and "Firefox" not in w.title and "Opera" not in w.title:
                app_window = w
                break
        
        if app_window:
            print(f"Found window: {app_window.title}")
            if app_window.isMinimized:
                app_window.restore()
            
            try:
                app_window.activate()
            except Exception as e:
                print(f"Error activating window directly: {e}")
                # Fallback: minimize and restore to force focus
                app_window.minimize()
                time.sleep(0.5)
                app_window.restore()

            # Ensure focus by clicking in the middle of the window
            # This handles cases where the window is active but focus isn't in the input box
            time.sleep(1)
            try:
                center_x = app_window.left + (app_window.width // 2)
                center_y = app_window.top + (app_window.height // 2)
                # Click slightly lower than center, as chat box is usually at the bottom
                # But actually, if the URL pre-fills, the cursor is usually already there.
                # A click might DE-FOCUS if we click the wrong spot.
                # Safer: Click the title bar? No.
                # Let's just trust activate first, but if it fails, the user might need to click.
                pass 
            except:
                pass

            time.sleep(1)
        else:
            print("Could not specifically identify WhatsApp Desktop window. Assuming it is focused by open command.")
            
    except Exception as e:
        print(f"Focus attempt warning: {e}")

    # Press Enter to send the first message (pre-filled by URL)
    print("Sending message 1...")
    
    # Sometimes one Enter isn't enough if there's a slight lag or a "Draft" buffer
    pyautogui.press('enter')
    time.sleep(1)
    # Press again just in case the first one was consumed by window focus
    pyautogui.press('enter') 
    
    # Send remaining messages if count > 1
    if count > 1:
        import pyperclip
        for i in range(count - 1):
             # Wait a bit between messages
            time.sleep(2)
            
            # Copy message to clipboard and paste
            pyperclip.copy(message)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1) # Wait for paste
            
            pyautogui.press('enter')
            print(f"Message {i+2} sent!")

    print("Task completed.")

if __name__ == "__main__":
    print("--- WhatsApp Desktop Automation ---")
    phone = input("Enter phone number (with country code, e.g., +123...): ")
    msg = input("Enter message: ")
    
    try:
        n_str = input("How many times to send (default 1): ")
        n = int(n_str) if n_str.strip() else 1
    except ValueError:
        n = 1
    
    print("\n--- Schedule ---")
    print("Enter the time to send the message (24-hour format).")
    try:
        s_hour = int(input("Hour (0-23): "))
        s_minute = int(input("Minute (0-59): "))
        
        now = datetime.datetime.now()
        scheduled_time = now.replace(hour=s_hour, minute=s_minute, second=0, microsecond=0)
        
        # If time is in the past, schedule for tomorrow
        if scheduled_time < now:
            scheduled_time += datetime.timedelta(days=1)
            
        wait_seconds = (scheduled_time - now).total_seconds()
        
        print(f"\nMessage scheduled for {scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Waiting for {int(wait_seconds)} seconds...")
        print("NOTE: The computer must remain UNLOCKED. The monitor can be off, but do not Lock (Win+L).")
        
        # Prevent sleep mode
        prevent_sleep()
        
        # Wait until scheduled time
        time.sleep(wait_seconds)
        
        # Allow sleep again and wake screen
        allow_sleep()
        wake_screen()
        
        print("\nTime arrived. Sending message...")
        send_whatsapp_desktop(phone, msg, n)
        
    except ValueError:
        print("Invalid time input. Run script again.")
