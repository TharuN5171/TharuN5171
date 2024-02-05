import time

def send_message(number, message):
    while True:
        print(f"Sending message to {number}: {message}")
        time.sleep(1)

if __name__ == "__main__":
    try:
        number = input("Enter the phone number: ")
        message = input("Enter the message: ")
        send_message(number, message)
    except KeyboardInterrupt:
        print("\nMessage sending stopped.")
        exit()