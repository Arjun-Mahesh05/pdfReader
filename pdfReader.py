import pyttsx3
import PyPDF2
import re
from tkinter.filedialog import *

book = askopenfilename()
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

speaker = pyttsx3.init()
def set_speed(speed):
    if speed.isdigit():
        speed = int(speed)
        if 1 <= speed <= 200:
            speaker.setProperty('rate', speed)
        else:
            print("Please enter a number between 1 and 200.")
    else:
        print("Invalid input. Please enter a number.")

set_speed(input("Enter speed: "))
speaker.setProperty('volume', 1)  # Set volume level (0.0 to 1.0)

full_text = ""
for num in range(pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    if text:
        full_text += text + " "

# Clean up text: remove extra whitespace and line breaks
clean_text = re.sub(r'\s+', ' ', full_text).strip()

# Split into sentences for smoother speech
sentences = re.split(r'(?<=[.!?]) +', clean_text)

if clean_text:
    for sentence in sentences:
        speaker.say(sentence)
        speaker.runAndWait()
    print(clean_text)
else:
    print("No text found in the PDF.")