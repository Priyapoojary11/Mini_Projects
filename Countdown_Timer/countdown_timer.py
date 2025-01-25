import time

def countdown(t):
    try:
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print("Timer Completed!")
    except KeyboardInterrupt:
        print("\nTimer interrupted! Exiting...")

def get_input():
    while True:
        try:
            t = int(input("Enter the time in seconds: "))
            if t <= 0:
                print("Please enter a positive integer.")
            else:
                return t
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    t = get_input()
    countdown(t)