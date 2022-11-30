import pyttsx3

book = open(r"2022\Nov\AudioBook\book.txt", "r")
book_text = book.readlines()

engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()