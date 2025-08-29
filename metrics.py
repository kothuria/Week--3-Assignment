import time

def log_duration(start, end):
    duration = round(end - start, 2)
    print(f"\n⏱️ Runtime: {duration} seconds")
    return duration
