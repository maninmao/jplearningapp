from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pygame

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        master.title("Nihonigiri - Learn Japanese")
        self.flip_interval = 10

        # Set up the homepage
        self.homepage = tk.Frame(master, bg="lightblue", width=800, height=600)
        self.homepage.pack_propagate(0)
        self.homepage.pack()

        # Load the logo image
        logo_image = tk.PhotoImage(file="applogo.png")

        # Display the logo on the homepage
        self.logo_label = tk.Label(self.homepage, image=logo_image, bg="lightblue")
        self.logo_label.image = logo_image
        self.logo_label.place(x=199, y=20, width=400, height=350)

        # Change the color of the start_button
        self.start_button = tk.Button(self.homepage, text="Start Learning", command=self.show_categories)
        self.start_button_radius = 25
        self.start_button.config(width=12, height=2, borderwidth=3, bg="lightpink2", fg="black" )  # Change the background color to red
        self.start_button.pack(pady=20)
        self.start_button.place(x=340, y=350)
        


        # Set up the categories page
        self.categories_page = tk.Frame(master, bg="lavender", width=800, height=600)
        self.categories_page.pack_propagate(0)

        self.hiragana_button = tk.Button(self.categories_page, text="Hiragana", command=lambda: self.show_flashcards("Hiragana"))
        self.katakana_button = tk.Button(self.categories_page, text="Katakana", command=lambda: self.show_flashcards("Katakana"))
        self.vocab_button = tk.Button(self.categories_page, text="Vocabulary", command=lambda: self.show_flashcards("Vocabulary"))
        self.back_button_categories = tk.Button(self.categories_page, text="Back", command=self.show_homepage)

        # Set up the flashcards page

        self.flashcards_page = tk.Frame(master, bg="slategray1", width=800, height=600)
        self.flashcards_page.pack_propagate(0)
        
        self.card_label = tk.Label(self.flashcards_page, text="", font=("Helvetica", 100))
        self.back_button_flashcards = tk.Button(self.flashcards_page, text="Back", command=self.show_categories)
        self.next_button = tk.Button(self.flashcards_page, text="Next", command=self.show_next_flashcard)

        # Add a boolean variable to track the flashcard side (front or back)
        self.showing_front = True

        # Bind the label to the flip function
        self.card_label.bind("<Button-1>", self.flip_flashcard)

        self.current_category = ""
        self.current_index = 0
    
        # Initialize Pygame mixer
        pygame.mixer.init()

        # Add a sound button
        self.sound_button = tk.Button(self.flashcards_page, text="Sound", command=self.play_sound)
        # self.sound_button.pack(pady=10)
        self.sound_button.config(bg="pink", fg="black" )
        self.sound_button.place(x=380, y=370)

    def flip_flashcard(self, event=None):
        if self.showing_front:
            self.flip_to_back()
        else:
            self.flip_to_front()

    def flip_to_back(self):
        self.showing_front = False
        self.card_label.config(text=self.get_flashcard_definition())
        self.master.after(self.flip_interval, self.flip_flashcard)

    def flip_to_front(self):
        self.showing_front = True
        self.card_label.config(text=self.get_flashcard_text())
        self.master.after(self.flip_interval, self.flip_flashcard)

    def play_sound(self):
        # Get the Japanese character based on the current category and index
        character = self.get_flashcard_text()

        # Load and play the corresponding sound file
        sound_file_path = f"sounds/{character}.mp3"  # Assuming sound files are in a 'sounds' folder
        pygame.mixer.music.load(sound_file_path)
        pygame.mixer.music.play()

    def show_homepage(self):
        self.flashcards_page.pack_forget()
        self.categories_page.pack_forget()
        self.homepage.pack()

    def show_categories(self):
        self.homepage.pack_forget()
        self.flashcards_page.pack_forget()
        self.categories_page.pack()
        self.hiragana_button.config(width=12, height=2, borderwidth=3, bg="lightpink1", fg="black" )
        self.katakana_button.config(width=12, height=2, borderwidth=3, bg="lightpink1", fg="black" )
        self.vocab_button.config(width=12, height=2, borderwidth=3, bg="lightpink1", fg="black" )
        self.back_button_categories.config(bg="mistyrose1", fg="black" )
        # Arrange widgets in the categories page
        self.hiragana_button.place(x=340, y=190)
        self.katakana_button.place(x=340, y=240)
        self.vocab_button.place(x=340, y=290)
        self.back_button_categories.place(x=371, y=345)

    def show_flashcards(self, category):
        # Set the current category and index to start from the beginning
        self.current_category = category
        self.current_index = 0

        # Update the flashcard label with the first flashcard
        self.card_label.config(text=self.get_flashcard_text(), bg="slategray1")
        self.flashcards_page.pack_forget()
        self.categories_page.pack_forget()
        self.homepage.pack_forget()
        self.flashcards_page.pack()
        self.back_button_flashcards.config(bg="mistyrose1", fg="black" )
        self.next_button.config(bg="mistyrose1", fg="black" )

        # Arrange widgets in the flashcards page
        # self.card_label.pack(pady=50)
        # self.back_button_flashcards.pack(pady=10)
        # self.next_button.pack(pady=10)
        if category == "Vocabulary":
            self.card_label.config(font=("Helvetica", 40), bg="slategray1")
            self.card_label.place(x=272, y=190)
            self.next_button.place(x=470, y=370)
            self.back_button_flashcards.place(x=300, y=370)
        else:
            self.card_label.config(font=("Helvetica", 100), bg="slategray1")
            self.card_label.place(x=335, y=160)
            self.next_button.place(x=470, y=370)
            self.back_button_flashcards.place(x=300, y=370)

    def show_next_flashcard(self):
        # Implement logic to handle next flashcard based on the current category and index
        # For simplicity, let's assume you have a list of flashcards for each category
        flashcards = {
            "Hiragana": ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", 
                         "さ", "し", "す", "せ", "そ", "た", "ち", "つ", "て", "と", 
                         "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", 
                         "ま", "み", "む", "め", "も", "や", "ゆ", "よ", 
                         "ら", "り", "る", "れ", "ろ", "わ", "を", "ん"],
            "Katakana": ["ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ", 
                         "サ", "シ", "ス", "セ", "ソ", "タ", "チ", "ツ", "テ", "ト", 
                         "ナ", "ニ", "ヌ", "ネ", "ノ", "ハ", "ヒ", "フ", "ヘ", "ホ", 
                         "マ", "ミ", "ム", "メ", "モ", "ヤ", "ユ", "ヨ", 
                         "ラ", "リ", "ル", "レ", "ロ", "ワ", "ヲ", "ン"],
            "Vocabulary": ["おはよう", "こんにちは", "こんばんは", "おやすみなさい", "ありがとう", "さようなら", "すみません", "ごめんなさい"]
        }

        if self.current_index < len(flashcards[self.current_category]) - 1:
            self.current_index += 1
            self.card_label.config(text=self.get_flashcard_text())
        else:
            messagebox.showinfo("Congratulations!", "You've completed the flashcards for this category.")
            self.show_categories()

    def flip_flashcard(self, event):
        # Toggle between front and back sides
        if self.showing_front:
            # Display the back side (definition)
            self.card_label.config(text=self.get_flashcard_definition(), bg="slategray1")
        else:
            # Display the front side (Japanese character)
            self.card_label.config(text=self.get_flashcard_text())

        # Toggle the boolean variable
        self.showing_front = not self.showing_front

    def get_flashcard_text(self):
        # Get the Japanese character based on the current category and index
        flashcards = {
            "Hiragana": ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", 
                         "さ", "し", "す", "せ", "そ", "た", "ち", "つ", "て", "と", 
                         "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", 
                         "ま", "み", "む", "め", "も", "や", "ゆ", "よ", 
                         "ら", "り", "る", "れ", "ろ", "わ", "を", "ん"
],
            "Katakana": ["ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ", 
                         "サ", "シ", "ス", "セ", "ソ", "タ", "チ", "ツ", "テ", "ト", 
                         "ナ", "ニ", "ヌ", "ネ", "ノ", "ハ", "ヒ", "フ", "ヘ", "ホ", 
                         "マ", "ミ", "ム", "メ", "モ", "ヤ", "ユ", "ヨ", 
                         "ラ", "リ", "ル", "レ", "ロ", "ワ", "ヲ", "ン"
],
            "Vocabulary": ["おはよう", "こんにちは", "こんばんは", "おやすみなさい", "ありがとう", "さようなら", "すみません", "ごめんなさい"]
        }
        return flashcards[self.current_category][self.current_index]

    def get_flashcard_definition(self):
        # Add definitions corresponding to the flashcards
        definitions = {
            "Hiragana": ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", 
                         "sa", "shi", "su", "se", "so", "ta", "chi", "tsu", "te", "to", 
                         "na", "ni", "nu", "ne", "no", "ha", "hi", "fu", "he", "ho", 
                         "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", 
                         "ra", "ri", "ru", "re", "ro", "wa", "wo", "n"],

            "Katakana": ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", 
                         "sa", "shi", "su", "se", "so", "ta", "chi", "tsu", "te", "to", 
                         "na", "ni", "nu", "ne", "no", "ha", "hi", "fu", "he", "ho", 
                         "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", 
                         "ra", "ri", "ru", "re", "ro", "wa", "wo", "n"],

            "Vocabulary": ["Good Morning", "Good Afternoon", "Good Evening", "Good Night", "Thank You", "Good  Bye", "Excuse Me", "I am sorry"]
        }
        return definitions[self.current_category][self.current_index]

root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()

