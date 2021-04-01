from log_setting import FileLogger
import threading


def func(a):
    print(a)
    FileLogger.info(a)
try:

    for i in range(5):
        threading.Thread(target=func, args=(i,)).start()
    FileLogger.error("error")
    FileLogger.critical("CRITICAL")
except Exception as e:
    FileLogger.error(e)