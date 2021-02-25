import os
import time

def banner():
    banner1="""
    =======================
    Auto-open-CMD by iFanpS
    This program is useless
    =======================
    """
    print(banner1)

def awalan():
    os.system('start cmd')
    print("Your cmd has been opened")

if __name__ == "__main__":
    banner()
    time.sleep(2)
    awalan()