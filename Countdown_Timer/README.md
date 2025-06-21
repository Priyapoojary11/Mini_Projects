# Countdown Timer App

This Python script implements a simple countdown timer that allows users to input a time in seconds and displays the countdown in minutes and seconds format. The timer will countdown until it reaches zero and display a message when the timer is completed. Users can also interrupt the countdown at any time using `Ctrl+C`.

## Features
- Accepts user input for the countdown duration (in seconds).
- Displays the countdown in the format `MM:SS`.
- Handles invalid inputs (non-numeric or negative values).
- Gracefully handles keyboard interrupts (`Ctrl+C`).
- Provides feedback when the timer completes.

## How It Works
1. The user is prompted to enter the number of seconds for the countdown.
2. The timer will count down from the entered time in `MM:SS` format.
3. If the user interrupts the timer with `Ctrl+C`, the script will gracefully handle it and exit.
4. When the countdown finishes, it prints "Timer Completed!"

## Example Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Priyapoojary11/Projects/Countdown-Timer.git
