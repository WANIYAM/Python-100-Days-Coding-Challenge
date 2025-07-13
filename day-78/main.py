import time
import math

def countdown_timer(total_seconds):
    """
    A simple countdown timer that displays the remaining time.

    Args:
        total_seconds (int): The total number of seconds for the countdown.
    """
    if not isinstance(total_seconds, int) or total_seconds < 0:
        print("Please provide a non-negative integer for the countdown duration.")
        return

    print(f"Starting countdown for {total_seconds} seconds...")

    while total_seconds > 0:
        # Calculate minutes and seconds
        minutes = math.floor(total_seconds / 60)
        seconds = total_seconds % 60

        # Format the time for display (e.g., 05:09)
        timer_display = f"{minutes:02d}:{seconds:02d}"

        # Print the timer, overwriting the previous line
        # The '\r' character moves the cursor to the beginning of the line
        # 'end=""' prevents a newline character from being printed
        print(f"\rTime remaining: {timer_display}", end="")

        # Pause for 1 second
        time.sleep(1)

        # Decrement the total seconds
        total_seconds -= 1

    # After the loop, print a final message
    print("\rTime remaining: 00:00") # Ensure 00:00 is displayed clearly at the end
    print("Countdown finished! Time's up!")

if __name__ == "__main__":
    while True:
        try:
            duration_str = input("Enter the countdown duration in seconds (e.g., 60 for 1 minute): ")
            duration = int(duration_str)
            countdown_timer(duration)
            break # Exit loop if input is valid and countdown completes
        except ValueError:
            print("Invalid input. Please enter a whole number for seconds.")
        except KeyboardInterrupt:
            print("\nCountdown interrupted by user.")
            break
    print("Exiting timer application.")
