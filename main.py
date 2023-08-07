import tkinter as tk
import nltk
from newspaper import Article
from tkinter import *
import customtkinter

nltk.download('punkt')

# Create a tkinter GUI with CTk
root = customtkinter.CTk()
root.title("Skip Article")
root.geometry("800x660")

# Define colors
bg_color = "#E6F3FF"  # Light blue
text_color = "#333333"  # Dark gray
accent_color = "#007BFF"  # Blue
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

title1 = customtkinter.CTkLabel(root, text="Skip Article", height=40, width=40, font=('tuple', 50))
title1.pack(padx=10, pady=10)


# Helper function to create and style text widgets
def create_text_widget(root, height, width):
    entry = customtkinter.CTkEntry(root, placeholder_text="CTkEntry", height=height, width=width)
    entry.configure(state="disabled")
    return entry


# Function to update the text fields with generated data
def generate_data():
    article_url = link_input.get()
    article = Article(article_url)
    article.download()
    article.parse()
    article.nlp()



    title.configure(state='normal')
    title.delete(1, customtkinter.END)
    title.insert(customtkinter.END, article.title)
    title.configure(state='disabled')

    author.configure(state='normal')
    author.delete(1, customtkinter.END)
    author.insert(customtkinter.END, ", ".join(article.authors))
    author.configure(state='disabled')

    pub_date.configure(state='normal')
    pub_date.delete(1, customtkinter.END)
    pub_date.insert(customtkinter.END, str(article.publish_date))
    pub_date.configure(state='disabled')

    summary.configure(state='normal')
    summary.delete(1, customtkinter.END)
    summary.insert(customtkinter.END, article.summary)
    summary.configure(state='disabled')

    media_news.configure(state='normal')
    media_news.delete(1, customtkinter.END)
    media_news.insert(customtkinter.END, str(article.is_media_news()))
    media_news.configure(state='disabled')




# Display article title
tlabel = customtkinter.CTkLabel(root, text="Title")

tlabel.pack()

title = create_text_widget(root, 30, 600)
title.pack()

# Display article author
alabel = customtkinter.CTkLabel(root, text="Author", height=30, width=400)
alabel.pack()

author = create_text_widget(root, 30, 600)
author.pack()

# Display publication date
dlabel = customtkinter.CTkLabel(root, height=30, width=400, text="Publication Date", )
dlabel.pack()

pub_date = create_text_widget(root, height=30, width=600)
pub_date.pack()

# Display article summary
slabel = customtkinter.CTkLabel(root, height=30, width=400, text="Summary", )
slabel.pack()

summary = create_text_widget(root, height=180, width=600)
summary.pack()

# Display media news
m_label = customtkinter.CTkLabel(root, height=30, width=600, text="Media News", )
m_label.pack()

media_news = create_text_widget(root, 30, width=600)
media_news.pack()

# Input field for article link
link_label = customtkinter.CTkLabel(root, text="Paste Article Link Here", )
link_label.pack()

link_input = customtkinter.CTkEntry(root, height=30, width=400, )
link_input.pack()

# Button to generate data
generate_button = customtkinter.CTkButton(root, text="Summarize", command=generate_data)
generate_button.pack()

root.mainloop()

# # Display publication date
# dlabel = tk.Label(root, text="Publication Date", bg=bg_color, fg=accent_color, font=("Helvetica", 14, "bold"))
# dlabel.pack()
#
# pub_date = create_text_widget(root, 1, 90)
# pub_date.pack()
#
# # Display article summary
# slabel = tk.Label(root, text="Summary", bg=bg_color, fg=accent_color, font=("Helvetica", 14, "bold"))
# slabel.pack()
#
# summary = create_text_widget(root, 15, 90)
# summary.pack()
#
# # Display media news
# m_label = tk.Label(root, text="Media News", bg=bg_color, fg=accent_color, font=("Helvetica", 14, "bold"))
# m_label.pack()
#
# media_news = create_text_widget(root, 1, 90)
# media_news.pack()
#
# # Input field for article link
# link_label = tk.Label(root, text="Paste Article Link Here", bg=bg_color, fg=accent_color, font=("Helvetica", 14, "bold"))
# link_label.pack()
#
# link_input = tk.Entry(root, width=100, bg='white', fg=text_color)
# link_input.pack()
#

# root.mainloop()
