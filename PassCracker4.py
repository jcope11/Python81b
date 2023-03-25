# Password Cracker - all keys on keyboard

import itertools, string, time
from datetime import datetime

color_white = '\033[0m'
color_red = '\033[91m'
color_green = '\033[92m'

def guess(secret):
    start_time = datetime.now()
    start_time_sec = time.time()
    print("Brute force attack has begun .....\n")
    print(f"Time started:", start_time.strftime("%H:%M:%S"))
    characters = string.printable[:95]
    attempts = 0
    for password_length in range(1, 9):
        for i in itertools.product(characters, repeat=password_length):
            # print(i)
            attempts += 1
            i = "".join(i)
            if i == secret:
                stop_time = datetime.now()
                stop_time_sec = time.time()
                total_time_sec = stop_time_sec - start_time_sec
                attempts_per_sec = attempts / total_time_sec
                print(f"Time stopped:", stop_time.strftime("%H:%M:%S"))
                print(f"\nThe password is {i} \nIt was found in {attempts:,} attempts.")
                print(f"It took \33[92m{round(total_time_sec, 2)} seconds\33[0m to find the password")
                print(f"I processed {round(attempts_per_sec):,} per second")

                exit()


secret_pwd = input("Enter your secret password: ")
guess(secret_pwd)
