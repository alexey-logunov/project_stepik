def add(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = "\n".join(environ.get('QUERY_STRING').split("&"))
    start_response(status, headers)
    return iter([body.encode('utf-8')])


sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart