from celery_work.tasks.main import celery_app
import time


# 这个文件名必须叫tasks，celery会自动识别该文件中的任务
@celery_app.task
def add_func(a,b):
    time.sleep(5)
    print('执行完毕')
    return a+b