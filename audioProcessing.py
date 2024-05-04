import speech_recognition as sr
import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up a GPIO pin as output
pin = 17
GPIO.setup(pin, GPIO.OUT)

# Initialize the speech recognition recognizer
r = sr.Recognizer()

def speech_to_text(audio_path):
    with sr.AudioFile(audio_path) as source:
        # Listen for data (load audio to memory)
        audio_data = r.record(source)
        # Attempt to recognize speech from the audio data
        try:
            text = r.recognize_google(audio_data)
            print("Detected speech:", text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")

def control_led(command):
    """ Control the LED based on the 'on' or 'off' command. """
    if 'on' in command.lower():
        GPIO.output(pin, GPIO.HIGH)
        # wait for 3 seconds
        time.sleep(3)
        print("LED turned ON")
    elif 'off' in command.lower():
        GPIO.output(pin, GPIO.LOW)
        print("LED turned OFF")

# Main program execution
try:
    led_on_command = speech_to_text('/home/zmn10/Desktop/7.2DRPiAudioProcessing/on.wav')
    led_off_command = speech_to_text('/home/zmn10/Desktop/7.2DRPiAudioProcessing/off.wav')

    if led_on_command:
        control_led(led_on_command)
    if led_off_command:
        control_led(led_off_command)
except KeyboardInterrupt:
    print("Program interrupted")
finally:
    # Clean up GPIO settings
    GPIO.cleanup()
    print("GPIO cleaned up and program terminated")

