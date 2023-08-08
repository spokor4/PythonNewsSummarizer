import textwrap
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

# Title
title1 = customtkinter.CTkLabel(root, text="Skip Article", height=40, width=40, font=('tuple', 50))
title1.pack(padx=10, pady=10)


# Function to create and style text widgets
def create_text_widget(root, height, width, placeholder_text):
    entry = customtkinter.CTkEntry(root, placeholder_text=placeholder_text, height=height, width=width)
    entry.configure(state="disabled")
    return entry


# Function to create and style CTkTextBox
def create_text_box(root, height, width):
    box = customtkinter.CTkTextbox(root, height=height, width=width)
    box.configure(state="disabled")
    return box



# Function to update the text fields with generated data
def generate_data():
    article_url = link_input.get()
    article = Article(article_url)
    article.download()
    article.parse()
    article.nlp()


# Title
    title.configure(state='normal')
    title.delete(1, customtkinter.END)
    title.insert(customtkinter.END, article.title)
    title.configure(state='disabled')

# Author
    author.configure(state='normal')
    author.delete(1, customtkinter.END)
    author.insert(customtkinter.END, ", ".join(article.authors))
    author.configure(state='disabled')

# Pub Date
    pub_date.configure(state='normal')
    pub_date.delete(1, customtkinter.END)
    pub_date.insert(customtkinter.END, str(article.publish_date))
    pub_date.configure(state='disabled')

# Summary
    summary.config(state='normal')
    summary.delete('1.0', tk.END)
    summary.insert(tk.END, article.summary)
    summary.config(state='disabled')

# Media News
    media_news.configure(state='normal')
    media_news.delete(1, customtkinter.END)
    media_news.insert(customtkinter.END, str(article.is_media_news()))
    media_news.configure(state='disabled')


# Display article title
tlabel = customtkinter.CTkLabel(root, text="Title")
tlabel.pack()

title = create_text_widget(root, 30, 600, placeholder_text="Title")
title.pack()

# Display article author
alabel = customtkinter.CTkLabel(root, text="Author", height=30, width=400, )
alabel.pack()

author = create_text_widget(root, 30, 600, placeholder_text="Author/s")
author.pack()

# Display publication date
dlabel = customtkinter.CTkLabel(root, height=30, width=400, text="Publication Date", )
dlabel.pack()

pub_date = create_text_widget(root, height=30, width=600, placeholder_text="Publication date")
pub_date.pack()

# Display Summary
slabel = customtkinter.CTkLabel(root, height=30, width=400, text="Summary", )
slabel.pack()

summary = Text(root, height=10, width=68, wrap=WORD, bd=0, bg="#292929", fg="grey", font="tuple")
summary.pack()

# Display media news
m_label = customtkinter.CTkLabel(root, height=30, width=600, text="Media News", )
m_label.pack()

media_news = create_text_widget(root, 30, width=600, placeholder_text="Is Media News?")
media_news.pack()

# Input field for article link
link_label = customtkinter.CTkLabel(root, text="Paste Article Link Here", )
link_label.pack()

link_input = customtkinter.CTkEntry(root, height=30, width=400, placeholder_text="Link", )
link_input.pack(pady=(0, 10))

# Button to generate data
generate_button = customtkinter.CTkButton(root, text="Summarize", command=generate_data)
generate_button.pack()

root.mainloop()

