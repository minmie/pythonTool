from celery_work.tasks.main import celery_app
import time


# 这个文件名必须叫tasks，celery会自动识别该文件中的任务
@celery_app.task
def time_task1(a,b):
    print('周期任务开始执行，等待5秒')
    time.sleep(5)
    print('周期任务执行完毕')
    return a-b

@celery_app.task
def time_task2(a,b):
    print('定时任务开始执行，等待5秒')
    time.sleep(5)
    print('定时任务执行完毕')
    return a-b