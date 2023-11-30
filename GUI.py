#GUI


import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from Prototype_URL import get_articles
from Summarize_Function import summarize



class SummarizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Summarizer")

        self.search_label = ttk.Label(master, text="Search:")
        self.search_label.grid(row=0, column=0, padx=5, pady=5)

        self.search_entry = ttk.Entry(master, width=50)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = ttk.Button(master, text="Search", command=self.search)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.results_frame = ttk.Frame(master)
        self.results_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def search(self):
        query = self.search_entry.get()
        all_articles = get_articles(query)

        # Clear the results frame
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # Display the article titles as clickable links
        for article in all_articles:
            title_label = ttk.Label(self.results_frame, text=article['title'], foreground='blue', cursor='hand2')
            title_label.bind("<Button-1>", lambda event, summary=article['text'], url=article['url']: self.show_summary(summary, url))
            title_label.pack(side='top', fill='x', padx=5, pady=5)

    def show_summary(self, summary, url):
        # Clear the results frame
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # Display the summarized article
        summary_label = ttk.Label(self.results_frame, text=summary, wraplength=800)
        summary_label.pack(side='top', fill='both', expand=True, padx=5, pady=5)

        # Display the link to the original article
        url_label = ttk.Label(self.results_frame, text="LINK TO ORIGINAL ARTICLE:"+url, foreground='blue', cursor='hand2')
        url_label.bind("<Button-1>", lambda event, url=url: self.open_url(url))
        url_label.pack(side='bottom', fill='x', padx=5, pady=5)

        # Display the back button
        back_button = ttk.Button(self.results_frame, text="Back", command=self.search)
        back_button.pack(side='bottom', pady=5)

    def open_url(self, url):
        webbrowser.open_new(url)

root = tk.Tk()
app = SummarizerGUI(root)
root.mainloop()

