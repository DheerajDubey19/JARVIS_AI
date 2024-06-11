# Jarvis AI

Jarvis AI is a personal assistant built using Python. It provides a wide range of functionalities such as sending emails, optical text recognition, opening websites with voice commands, playing music, and performing Wikipedia searches.

## Features

- **Voice Command Recognition**: Open websites, play music, and perform searches using voice commands.
- **Email Sending**: Send emails through voice commands.
- **Optical Text Recognition (OCR)**: Recognize text from images.
- **Wikipedia Search**: Fetch information from Wikipedia.

## Technology Stack

- **Programming Language**: Python
- **Libraries**: `speech_recognition`, `pyttsx3`, `smtplib`, `cv2` (OpenCV), `pytesseract`, `wikipedia`, `webbrowser`, `os`, `sys`

## Installation

### Prerequisites

- Python 3.7+
- Install Tesseract-OCR for your OS:
  - **Windows**: Download the installer from [here](https://github.com/tesseract-ocr/tesseract/wiki) and add Tesseract to your PATH.
  - **macOS**: `brew install tesseract`
  - **Linux**: `sudo apt-get install tesseract-ocr`

### Install Required Python Libraries

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/jarvis-ai.git
    cd jarvis-ai
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Email Configuration**:
    - Update the `send_email` function with your email credentials.

    ```python
    EMAIL_ADDRESS = "your_email@example.com"
    EMAIL_PASSWORD = "your_password"
    ```

## Usage

1. **Run the Jarvis AI**:
    ```bash
    python jarvis.py
    ```

2. **Voice Commands**:
    - **Open Website**: "open [website name]"
    - **Play Music**: "play music"
    - **Send Email**: "send an email"
    - **OCR**: "read text from image"
    - **Wikipedia Search**: "search Wikipedia for [query]"

## Features Implementation

### Voice Command Recognition

```python
import speech_recognition as sr
import pyttsx3

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
```

### Send Email

```python
import smtplib

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, to, content)
    server.close()
```

### Optical Text Recognition (OCR)

```python
import cv2
import pytesseract

def read_text_from_image(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    print(text)
    return text
```

### Wikipedia Search

```python
import wikipedia

def search_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    print(results)
    return results
```

### Open Website

```python
import webbrowser

def open_website(site):
    webbrowser.open(site)
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [dheerajdubey600@gmail.com](mailto:your-email@example.com).

---

This README provides an overview of the Jarvis AI project, including setup instructions, key functionalities, and how to contribute. For further details, please refer to the project source code.
