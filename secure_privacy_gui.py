import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from search_engine import get_private_results
import webbrowser

# Function to open links in the default web browser
def open_link(url):
    webbrowser.open_new_tab(url)

def search():
    query = search_entry.get().strip()
    if not query:
        messagebox.showwarning("Empty Query", "Please enter something to search.")
        return

    result_area.config(state=tk.NORMAL)
    result_area.delete(1.0, tk.END)
    result_area.insert(tk.END, "🔍 Searching privately...\n\n")

    results = get_private_results(query)

    for i, (title, link) in enumerate(results[:10], 1):
        result_area.insert(tk.END, f"{i}. {title}\n", ("bold",))

        start_index = result_area.index(tk.INSERT)
        result_area.insert(tk.END, f"{link}\n\n")
        end_index = result_area.index(tk.INSERT)

        result_area.tag_add(f"link{i}", start_index, end_index)
        result_area.tag_config(f"link{i}", foreground="blue", underline=1)
        result_area.tag_bind(f"link{i}", "<Button-1>", lambda e, url=link: open_link(url))

    result_area.insert(tk.END, "🧹 Session cleared. No tracking, no cookies.\n")
    result_area.config(state=tk.DISABLED)

# Create root window
root = tk.Tk()
root.title("🔒 Secure Privacy Toolkit")
root.geometry("800x600")

# Tabs setup
tab_control = ttk.Notebook(root)

# Tab 1 - Search Tool
search_tab = ttk.Frame(tab_control)
tab_control.add(search_tab, text="Private Search")

search_label = tk.Label(search_tab, text="Enter your private search:")
search_label.pack(pady=5)

search_entry = tk.Entry(search_tab, width=80)
search_entry.pack(pady=5)

search_button = tk.Button(search_tab, text="Search Privately", command=search)
search_button.pack(pady=5)

result_area = scrolledtext.ScrolledText(search_tab, wrap=tk.WORD, height=25)
result_area.pack(expand=True, fill='both')
result_area.config(state=tk.DISABLED)

# Tab 2 - Disable Cookies Instructions
cookie_tab = ttk.Frame(tab_control)
tab_control.add(cookie_tab, text="Disable Cookies")

cookie_info = tk.Label(cookie_tab, text="📛 How to disable cookies in common browsers:", font=("Arial", 12, "bold"))
cookie_info.pack(pady=10)

cookie_text = """1. Google Chrome:
   - Go to Settings > Privacy and security > Cookies and other site data.
   - Select "Block third-party cookies".

2. Firefox:
   - Settings > Privacy & Security > Cookies and Site Data.
   - Choose "Strict" or customize to block all.

3. Microsoft Edge:
   - Settings > Cookies and site permissions.
   - Choose "Block third-party cookies".

🔗 More info:
"""
cookie_label = tk.Label(cookie_tab, text=cookie_text, justify="left", anchor="w")
cookie_label.pack(anchor="w", padx=15)

# Adding the clickable cookie link
cookie_link = tk.Label(cookie_tab, text="Disable Cookies Guide", fg="blue", cursor="hand2")
cookie_link.pack(anchor="w", padx=20)
cookie_link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.allaboutcookies.org/manage-cookies"))

# Tab 3 - Disable Google Tracking
google_tab = ttk.Frame(tab_control)
tab_control.add(google_tab, text="Stop Google Tracking")

google_info = """🛑 How to disable Google tracking:

1. Turn off Location History:
"""
google_link_1 = tk.Label(google_tab, text="Visit: https://myaccount.google.com/activitycontrols/location", fg="blue", cursor="hand2")
google_link_1.pack(anchor="w", padx=15)
google_link_1.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://myaccount.google.com/activitycontrols/location"))

google_info += """
2. Turn off Web & App Activity:
"""
google_link_2 = tk.Label(google_tab, text="Visit: https://myaccount.google.com/activitycontrols/webandapp", fg="blue", cursor="hand2")
google_link_2.pack(anchor="w", padx=15)
google_link_2.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://myaccount.google.com/activitycontrols/webandapp"))

google_info += """
3. Pause YouTube History:
"""
google_link_3 = tk.Label(google_tab, text="Visit: https://myaccount.google.com/activitycontrols/youtube", fg="blue", cursor="hand2")
google_link_3.pack(anchor="w", padx=15)
google_link_3.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://myaccount.google.com/activitycontrols/youtube"))

google_info += """
4. Review & Delete Past Activity:
"""
google_link_4 = tk.Label(google_tab, text="Visit: https://myactivity.google.com", fg="blue", cursor="hand2")
google_link_4.pack(anchor="w", padx=15)
google_link_4.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://myactivity.google.com"))

tk.Label(google_tab, text=google_info, justify="left", anchor="w").pack(padx=15, pady=10)

# Tab 4 - Non-Tracking Tools
privacy_tab = ttk.Frame(tab_control)
tab_control.add(privacy_tab, text="Privacy Tools")

tools_info = """🚫 Use These Privacy-Friendly Tools:

1. Search Engines:
   - DuckDuckGo: https://duckduckgo.com
   - Startpage: https://www.startpage.com

2. Browsers:
   - Brave: https://brave.com
   - Firefox (with privacy add-ons)

3. Email Services:
   - ProtonMail: https://proton.me
   - Tutanota: https://tutanota.com

4. Messaging:
   - Signal: https://signal.org
   - Session: https://getsession.org

5. VPNs:
   - ProtonVPN: https://protonvpn.com
   - Mullvad: https://mullvad.net
"""
# Adding clickable privacy tool links
privacy_link_1 = tk.Label(privacy_tab, text="DuckDuckGo", fg="blue", cursor="hand2")
privacy_link_1.pack(anchor="w", padx=15)
privacy_link_1.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://duckduckgo.com"))

privacy_link_2 = tk.Label(privacy_tab, text="Startpage", fg="blue", cursor="hand2")
privacy_link_2.pack(anchor="w", padx=15)
privacy_link_2.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.startpage.com"))

privacy_link_3 = tk.Label(privacy_tab, text="Brave", fg="blue", cursor="hand2")
privacy_link_3.pack(anchor="w", padx=15)
privacy_link_3.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://brave.com"))

privacy_link_4 = tk.Label(privacy_tab, text="ProtonMail", fg="blue", cursor="hand2")
privacy_link_4.pack(anchor="w", padx=15)
privacy_link_4.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://proton.me"))

tk.Label(privacy_tab, text=tools_info, justify="left", anchor="w").pack(padx=15, pady=10)

# Final UI setup
tab_control.pack(expand=1, fill="both")
root.mainloop()
