import multiprocessing
import random
import time
from datetime import datetime

def process_function():
    wait_time = random.random()
    time.sleep(wait_time)
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Process {multiprocessing.current_process().name}: Current time is {current_time}", flush=True)

if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=process_function)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()