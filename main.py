import tkinter as tk
import nltk
from newspaper import Article



nltk.download('punkt')

# Create a tkinter GUI with CTk
root = tk.Tk()
root.title("Skip Article")
root.geometry("1200x800")

# # Define colors
bg_color = "#E6F3FF"  # Light blue
text_color = "#333333"  # Dark gray
accent_color = "#007BFF"  # Blue



# Set background color
root.config(bg=bg_color)

# Helper function to create and style text widgets
def create_text_widget(root, height, width):
    widget = tk.Text(root, height=height, width=width, bg=bg_color, fg=text_color, wrap=tk.WORD)
    widget.config(state='disabled')
    return widget

# Function to update the text fields with generated data
def generate_data():
    article_url = link_input.get()

    article = Article(article_url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    title.delete('1.0', tk.END)
    title.insert(tk.END, article.title)
    title.config(state='disabled')

    author.config(state='normal')
    author.delete('1.0', tk.END)
    author.insert(tk.END, ", ".join(article.authors))
    author.config(state='disabled')

    pub_date.config(state='normal')
    pub_date.delete('1.0', tk.END)
    pub_date.insert(tk.END, str(article.publish_date))
    pub_date.config(state='disabled')

    summary.config(state='normal')
    summary.delete('1.0', tk.END)
    summary.insert(tk.END, article.summary)
    summary.config(state='disabled')

    media_news.config(state='normal')
    media_news.delete('1.0', tk.END)
    media_news.insert(tk.END, str(article.is_media_news()))
    media_news.config(state='disabled')

# Display article title
tlabel = tk.Label(root, text="Title", bg=bg_color, fg=accent_color, font=("Helvetica", 14, "bold"))
tlabel.pack()

title = create_text_widget(root, 2, 90)
title.pack()

# Display article author
alabel = tk.Label(root, text="Author", bg=bg_color, fg=accent_color, font=("Helvetica", 14, "bold"))
alabel.pack()

author = create_text_widget(root, 1, 90)
author.pack()

# Display publication date
dlabel = tk.Label(root, text="Publication Date", bg=bg_color, fg=accent_color, font=("Helvetica", 14, "bold"))
dlabel.pack()

pub_date = create_text_widget(root, 1, 90)
pub_date.pack()

# Display article summary
slabel = tk.Label(root, text="Summary", bg=bg_color, fg=accent_color, font=("Helvetica", 14, "bold"))
slabel.pack()

summary = create_text_widget(root, 15, 90)
summary.pack()

# Display media news
m_label = tk.Label(root, text="Media News", bg=bg_color, fg=accent_color, font=("Helvetica", 14, "bold"))
m_label.pack()

media_news = create_text_widget(root, 1, 90)
media_news.pack()

# Input field for article link
link_label = tk.Label(root, text="Paste Article Link Here", bg=bg_color, fg=accent_color, font=("Helvetica", 14, "bold"))
link_label.pack()

link_input = tk.Entry(root, width=100, bg='white', fg=text_color)
link_input.pack()

# Button to generate data
generate_button = tk.Button(root, text="Summarize", command=generate_data, bg=accent_color, fg='white', font=("Helvetica", 12, "bold"))
generate_button.pack()

root.mainloop()
