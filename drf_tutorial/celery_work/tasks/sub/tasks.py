from celery_work.tasks.main import celery_app
import time


# 这个文件名必须叫tasks，celery会自动识别该文件中的任务
@celery_app.task
def sub_func1(a,b):
    time.sleep(5)
    print('sub_func1')
    return a-b


@celery_app.task
def sub_func2(a,b):
    time.sleep(5)
    print('sub_func2')
    return a-b