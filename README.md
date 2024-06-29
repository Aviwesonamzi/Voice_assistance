Overview
This project involves creating a voice-activated personal assistant using Python. The assistant is capable of performing various tasks, such as greeting the user, performing web searches, playing music, announcing the current time, and sending emails. The assistant interacts with the user through voice commands, leveraging speech recognition and text-to-speech technologies.

Key Features
Text-to-Speech (TTS): Converts text into speech using the pyttsx3 library.
Speech Recognition: Listens to and interprets voice commands using the speech_recognition library.
Time-Based Greeting: Greets the user appropriately based on the time of day (morning, afternoon, or evening).
Wikipedia Search: Searches Wikipedia for a given query and reads out a summary of the information.
Web Browsing: Opens popular websites like YouTube, Google, and Stack Overflow.
Music Playback: Plays music from a predefined directory on the user's computer.
Time Announcement: Announces the current time when requested.
Email Sending: Sends an email to a specified recipient using SMTP.
Libraries Used
pyttsx3: For text-to-speech conversion.
speech_recognition: For capturing and recognizing voice commands.
wikipedia: For fetching information from Wikipedia.
webbrowser: For opening websites in the default web browser.
os: For interacting with the operating system (e.g., listing files in a directory).
smtplib: For sending emails via SMTP.
datetime: For working with dates and times.
dotenv: For loading environment variables from a .env file (recommended for handling sensitive information like email credentials).
Functional Description
Initialization:

The assistant initializes the TTS engine and sets the desired voice property.
Greeting:

When started, the assistant greets the user based on the current time and introduces itself.
Command Handling:

The assistant listens for voice commands from the user and processes them to determine the appropriate action.
Actions:

Wikipedia Search: On detecting a Wikipedia search command, it fetches and reads out a summary.
Opening Websites: On detecting commands to open websites like YouTube, Google, or Stack Overflow, it launches the respective site in the default web browser.
Playing Music: On detecting a command to play music, it plays the first song from a specified directory.
Time Announcement: On detecting a request for the current time, it announces the time.
Sending Emails: On detecting an email command, it prompts the user for the email content and sends it to a predefined recipient.
Security Considerations:

Sensitive information such as email credentials should be stored securely using environment variables to prevent exposure.
Exit Command:

The assistant listens for an exit command to gracefully shut down the interaction.
Usage
To use the assistant, the user runs the script and speaks commands into the microphone. The assistant processes these commands and performs the corresponding actions, providing feedback through speech.

Future Enhancements
Enhanced Speech Recognition: Improve the accuracy and robustness of the speech recognition component.
Expanded Functionality: Add more features such as setting reminders, fetching weather information, controlling smart home devices, etc.
Improved User Interface: Develop a graphical user interface (GUI) for more user-friendly interaction.
