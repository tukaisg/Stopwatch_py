#Maa Saraswati Sahay

import time
import threading

class Timer:
    def __init__(self):
        self.start_time = time.time()
        self.lap_times = []
        self.display_thread = threading.Thread(target=self.display_time, daemon=True)
        self.display_thread.start()

    def lap(self):
        current_time = time.time()
        lap_time = current_time - self.start_time
        self.lap_times.append(lap_time)
        self.start_time = current_time
        return lap_time

    def display_time(self):
        while True:
            elapsed_time = time.time() - self.start_time
            formatted_time = format_time(elapsed_time)
            print(f"\rTime elapsed: {formatted_time}", end="")
            time.sleep(1)

def format_time(seconds):
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    result = ""
    if days > 0:
        result += f"{int(days)}d "
    if hours > 0 or days > 0:
        result += f"{int(hours)}h "
    if minutes > 0 or hours > 0:
        result += f"{int(minutes)}m "
    result += f"{seconds:.2f}s"
    return result

if __name__ == "__main__":
    timer = Timer()

    try:
        while True:
            input('Press Enter to record lap time or Ctrl+C to stop...')
            lap_time = timer.lap()
            lap_number = len(timer.lap_times)
            formatted_time = format_time(lap_time)
            print(f"\nLap {lap_number} -> time {formatted_time}")
    except KeyboardInterrupt:
        print("\nExiting stopwatch.")
