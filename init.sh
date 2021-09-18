sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:add
sudo gunicorn -c /home/box/web/etc/ask_conf.py wsgi:application