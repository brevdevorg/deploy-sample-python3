import psutil

def get():
    return "Hello from Numpy! " + str(psutil.cpu_times())
