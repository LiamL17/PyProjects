import time

from datetime import datetime as dt

def main():
    hosts_path="etc/hosts"

    while True:
        a = dt(2019, 12, 29, 9, 10, 10, 0)
        #dt(dt.now().year(), dt.now().month(), dt.now().day, 8)
        if dt(dt.now().year(), dt.now().month(), dt.now().day, 8) < dt.now() < dt(dt.now().year(), dt.now().month(), dt.now().day, 16):
            print("Working time...!")
        else:
            print("Do what you want baby!!!")
        time.sleep()

if __name__ == "__main__":
    main()