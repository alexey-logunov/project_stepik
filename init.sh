sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo gunicorn -c /home/alexey-logunov/PycharmProjects/web/etc/gunicorn.py hello:add
sudo gunicorn -c /home/box/web/etc/ask_conf.py ask.ask.wsgi:application

#sudo rm -rf /etc/nginx/sites-enabled/default
#sudo ln -sf /home/alexey-logunov/PycharmProjects/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
#sudo /etc/init.d/nginx restart
##sudo gunicorn -c /home/alexey-logunov/PycharmProjects/web/etc/gunicorn.py hello:add
#sudo gunicorn -c /home/alexey-logunov/PycharmProjects/web/etc/ask_conf.py ask.wsgi:application
