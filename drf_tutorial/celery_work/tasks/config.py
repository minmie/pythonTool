# coding:utf-8
from datetime import timedelta
from celery.schedules import crontab

REDIS_IP = '192.168.249.128'
REDIS_PORT = '6379'
REDIS_PASS = 'arvin'

BROKER_URL = f'redis://{REDIS_PASS}@{REDIS_IP}:{REDIS_PORT}/1'

# 保存结果
CELERY_RESULT_BACKEND = f'redis://{REDIS_PASS}@{REDIS_IP}:{REDIS_PORT}/2'

# 设置时区
CELERY_TIMEZONE = 'Asia/Shanghai'

# 允许root 用户运行celery
C_FORCE_ROOT = True

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_work.tasks.time_task.tasks',
)

# 定时任务
CELERYBEAT_SCHEDULE = {
    'time_task1': { # 这个名字可以随便取名
        'task': 'celery_work.tasks.time_task.taskstime_task1',  # 任务名
        'schedule': timedelta(seconds=10),  # 设置每10秒执行一次任务
        'args': (10, 100)
    },
    'time_task2': {
        'task': 'celery_work.tasks.time_task.tasks.time_task2',
        'schedule': crontab(hour=15, minute=35),  # 设置每天定时任务22:57执行
        'args': (10, 200)
    }
}

# crontab()  每分钟
#
# crontab(minute=0, hour=0)  每天的0时0分
#
# crontab(minute=0, hour='*/3')  每三小时
#
# crontab(day_of_week='sunday')  周日的每一小时
#
# crontab(minute='*',hour='*', day_of_week='sun') 与上面相同
#
# crontab(minute=0, hour='*/3,8-17') 每三个小时  8时到17时的每小时
