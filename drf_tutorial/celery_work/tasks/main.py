from celery import Celery # pip install celery
from celery_work.tasks import config


celery_app=Celery('test') # test 这个名字可以随便取


# 引入配置信息
celery_app.config_from_object(config)

# 自动搜寻异步任务
celery_app.autodiscover_tasks(["celery_work.tasks.add","celery_work.tasks.sub"])


# celery -A celery_work.tasks.main worker -l info  启动命令
# 参数解释
# -l info   设置日志级别


# 启动后后的界面说明
# -------------- celery @ qishi2 v4.3.0(rhubarb)
# ---- ** ** -----
# --- * ** * * -- Linux - 3.10.0 - 957.el7.x86_64 - x86_64 -with-centos - 7.6.1810-Core 2019-08-11 15:23: 30
# -- * - ** ** ---
# - ** ---------- [config]
# - ** ----------.> app: test:0x7fb49dcfc278  # test 是实例化Celery对象时取的名字，看第5行
# - ** ----------.> transport: redis: // 127.0.0.1: 6379 / 1  # 中间人
# - ** ----------.> results: redis: // 127.0.0.1: 6379 / 2
# - ** *--- * ---.> concurrency: 4(prefork)  # 进程数量
# -- ** ** ** *----.> task events: OFF(enable - E to monitor tasks in this worker)
# --- ** ** *-----
# -------------- [queues]
# .> celery exchange = celery(direct) key = celery
#
# [tasks]  # 异步任务
# .apptest.tasks.add.tasks.add_func
# .apptest.tasks.sub.tasks.sub_func1
# .apptest.tasks.sub.tasks.sub_func2
#


# celery beat -A apptest.tasks.main -l info  # 启动 beat触发celery的定时任务