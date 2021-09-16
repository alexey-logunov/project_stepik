sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/ask_conf.py  /etc/gunicorn.d/ask_conf.py
sudo gunicorn -c /etc/gunicorn.d/ask_conf.py ask.wsgi:application
sudo /etc/init.d/gunicorn restart