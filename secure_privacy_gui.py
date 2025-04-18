import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from search_engine import get_private_results
import webbrowser

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

root = tk.Tk()
root.title("🔒 Secure Privacy Toolkit")
root.geometry("900x650")

tab_control = ttk.Notebook(root)

# Tab 1 - Private Search
search_tab = ttk.Frame(tab_control)
tab_control.add(search_tab, text="Private Search")

search_label = tk.Label(search_tab, text="Enter your private search:", font=("Arial", 12))
search_label.pack(pady=5)

search_entry = tk.Entry(search_tab, width=80)
search_entry.pack(pady=5)

search_button = tk.Button(search_tab, text="Search Privately", command=search)
search_button.pack(pady=5)

result_area = scrolledtext.ScrolledText(search_tab, wrap=tk.WORD, height=25)
result_area.pack(expand=True, fill='both')
result_area.config(state=tk.DISABLED)

# Tab 2 - Disable Cookies
cookie_tab = ttk.Frame(tab_control)
tab_control.add(cookie_tab, text="Disable Cookies")

cookie_text = tk.Label(cookie_tab, text="📛 How to Disable Cookies in Your Browser", font=("Arial", 14, "bold"))
cookie_text.pack(pady=10, anchor="w", padx=20)

cookie_info = tk.Label(cookie_tab, text="""
🧠 Most browsers allow disabling or limiting cookies to protect your privacy.

1. Google Chrome:
   - Open Chrome and click on the 3 dots (⋮) > Settings.
   - Navigate to 'Privacy and security' > 'Cookies and other site data'.
   - Select “Block third-party cookies” or “Block all cookies”.

2. Mozilla Firefox:
   - Open Firefox > Settings > Privacy & Security.
   - Under 'Enhanced Tracking Protection', choose 'Strict' mode or manage custom settings to block all cookies.

3. Microsoft Edge:
   - Go to Settings > 'Cookies and site permissions'.
   - Click on 'Manage and delete cookies and site data'.
   - Turn OFF “Allow sites to save and read cookie data”.

🔗 Learn more:
""", justify="left", anchor="w")
cookie_info.pack(anchor="w", padx=20)

cookie_link = tk.Label(cookie_tab, text="👉 Disable Cookies Guide", fg="blue", cursor="hand2")
cookie_link.pack(anchor="w", padx=30)
cookie_link.bind("<Button-1>", lambda e: open_link("https://www.allaboutcookies.org/manage-cookies"))

# Tab 3 - Stop Google Tracking
google_tab = ttk.Frame(tab_control)
tab_control.add(google_tab, text="Stop Google Tracking")

google_title = tk.Label(google_tab, text="🛑 Disable Google Activity & Tracking", font=("Arial", 14, "bold"))
google_title.pack(pady=10, anchor="w", padx=20)

google_info = tk.Label(google_tab, text="""
1. Turn off Location History:
   - This prevents Google from storing your device’s GPS or location-based services.

""", justify="left", anchor="w")
google_info.pack(anchor="w", padx=20)

google_link_1 = tk.Label(google_tab, text="👉 Turn off Location History", fg="blue", cursor="hand2")
google_link_1.pack(anchor="w", padx=30)
google_link_1.bind("<Button-1>", lambda e: open_link("https://myaccount.google.com/activitycontrols/location"))

google_info2 = tk.Label(google_tab, text="""
2. Turn off Web & App Activity:
   - Stops Google from storing search history and activity from Google services.

""", justify="left", anchor="w")
google_info2.pack(anchor="w", padx=20)

google_link_2 = tk.Label(google_tab, text="👉 Turn off Web & App Activity", fg="blue", cursor="hand2")
google_link_2.pack(anchor="w", padx=30)
google_link_2.bind("<Button-1>", lambda e: open_link("https://myaccount.google.com/activitycontrols/webandapp"))

google_info3 = tk.Label(google_tab, text="""
3. Pause YouTube History:
   - Prevent YouTube from saving what you watch or search.

""", justify="left", anchor="w")
google_info3.pack(anchor="w", padx=20)

google_link_3 = tk.Label(google_tab, text="👉 Pause YouTube History", fg="blue", cursor="hand2")
google_link_3.pack(anchor="w", padx=30)
google_link_3.bind("<Button-1>", lambda e: open_link("https://myaccount.google.com/activitycontrols/youtube"))

google_info4 = tk.Label(google_tab, text="""
4. Delete Past Activity:
   - Clear all previously saved Google activity logs.

""", justify="left", anchor="w")
google_info4.pack(anchor="w", padx=20)

google_link_4 = tk.Label(google_tab, text="👉 Delete Past Google Activity", fg="blue", cursor="hand2")
google_link_4.pack(anchor="w", padx=30)
google_link_4.bind("<Button-1>", lambda e: open_link("https://myactivity.google.com"))

# Tab 4 - Use Non-Tracking Tools
privacy_tab = ttk.Frame(tab_control)
tab_control.add(privacy_tab, text="Privacy Tools")

privacy_title = tk.Label(privacy_tab, text="🧰 Recommended Privacy Tools", font=("Arial", 14, "bold"))
privacy_title.pack(pady=10, anchor="w", padx=20)

tools_info = tk.Label(privacy_tab, text="""
🛡️ Use these alternatives to reduce digital tracking:

🔎 Private Search Engines:
   - DuckDuckGo: No tracking, no personalized ads.
   - Startpage: Fetches Google results without logging you.

🌐 Secure Browsers:
   - Brave: Blocks trackers, ads, and fingerprints.
   - Firefox (customized with uBlock Origin, Privacy Badger).

📧 Encrypted Emails:
   - ProtonMail: End-to-end encrypted and based in Switzerland.
   - Tutanota: Open-source secure mail service.

📱 Private Messaging Apps:
   - Signal: Open-source, end-to-end encrypted.
   - Session: Decentralized, anonymous messaging.

🛡️ VPN Providers:
   - ProtonVPN: No logs, Swiss-based.
   - Mullvad: Anonymous account creation.
""", justify="left", anchor="w")
tools_info.pack(anchor="w", padx=20)

# Example clickable links
privacy_links = {
    "DuckDuckGo": "https://duckduckgo.com",
    "Startpage": "https://www.startpage.com",
    "Brave": "https://brave.com",
    "ProtonMail": "https://proton.me",
    "Tutanota": "https://tutanota.com",
    "Signal": "https://signal.org",
    "Session": "https://getsession.org",
    "ProtonVPN": "https://protonvpn.com",
    "Mullvad": "https://mullvad.net"
}

for name, url in privacy_links.items():
    link = tk.Label(privacy_tab, text=f"👉 {name}", fg="blue", cursor="hand2")
    link.pack(anchor="w", padx=30)
    link.bind("<Button-1>", lambda e, link_url=url: open_link(link_url))

# Display all tabs
tab_control.pack(expand=1, fill="both")
root.mainloop()
