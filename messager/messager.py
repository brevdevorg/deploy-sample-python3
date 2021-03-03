import psutil

def get():
    return "Hello from Numpy! " + psutil.cpu_times()
