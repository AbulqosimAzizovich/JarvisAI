import openai
import pyttsx3
import speech_recognition as sr
import playsound

# Set your OpenAI API key
openai.api_key = "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"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)

def jarvis(query):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct", 
        prompt=query,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    speak("Hello! I'm Jarvis. How can I assist you today?")

    while True:
        try:
            user_input = listen()
            print("User: ", user_input)

            if "exit" in user_input.lower():
                speak("Goodbye!")
                break

            response = jarvis(user_input)
            print("Jarvis:", response)
            speak(response)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. Could you please repeat?")
        except sr.RequestError as e:
            print(f"Error connecting to the speech recognition service: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")