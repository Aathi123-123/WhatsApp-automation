import os
import time

print("Testing WhatsApp Desktop Protocol...")
try:
    # Just open a draft message to a dummy number or just text
    # Note: 'phone' parameter is optional if you just want to test opening the app, 
    # but providing it makes it behave more like the real script.
    # Using a dummy text.
    url = "whatsapp://send?text=This_is_a_test_for_desktop_app_opening"
    
    print(f"Attempting to open: {url}")
    print("If your browser opens, the protocol association is wrong or WhatsApp Desktop is not installed/detected.")
    print("If WhatsApp Desktop opens, the fix worked.")
    
    os.startfile(url)
    
except Exception as e:
    print(f"Error executing os.startfile: {e}")
