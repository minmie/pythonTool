1. 虚拟环境  frame_test

2. 直接启动django
python manage.py runserver 192.168.249.128:8000

3.pip install uwsgi  服务器上安装

4. ps -ef|grep uwsgi |grep -v grep|awk '{print $2}'|xargs kill -9

5. 创建app命令,在app目录下执行
python ../manage.py startapp testapp


6.模拟前后端跨域问题，请查看drf_tutorial_pc 目录