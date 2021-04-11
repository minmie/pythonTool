from celery_work.tasks.add.tasks import add_func
from celery_work.tasks.sub.tasks import sub_func1,sub_func2

print(add_func.delay(3,5))

print(sub_func1.delay(3,5))
print(sub_func2.delay(3,5))